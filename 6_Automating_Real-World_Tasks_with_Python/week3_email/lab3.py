#!/usr/bin/env python3

import json
import locale
import sys
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import getpass
import smtplib
import mimetypes
from email.message import EmailMessage
import os.path


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    max_sales = {"car_model": "", "total_sales": 0}
    years_frequency = {}
    total_sales_per_year = {}
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        # TODO: also handle max sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales["total_sales"] = item["total_sales"]
            max_sales["car_model"] = format_car(item["car"])
        # TODO: also handle most popular car_year
        car_year = item["car"]["car_year"]
        years_frequency[car_year] = years_frequency.get(car_year, 0)+1
        total_sales_per_year[car_year] = total_sales_per_year.get(
            car_year, 0)+item["total_sales"]

    # Create a list of year occurences and sort it to find the most popular year
    years_freq_sorted = list(years_frequency.items())
    years_freq_sorted.sort(reverse=True, key=lambda x: x[1])
    most_popular_year = years_freq_sorted[0][0]

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        f"The {max_sales['car_model']} had the most sales: {max_sales['total_sales']}",
        f"The most popular year was {most_popular_year} with {total_sales_per_year[most_popular_year]} sales.",
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(
            item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    print(summary)

    # TODO: turn this into a PDF report
    report = SimpleDocTemplate("cars.pdf")
    styles = getSampleStyleSheet()

    report_title = Paragraph("Car sales report", styles["h1"])
    report_summary = Paragraph(
        f"{summary[0]}<br/>{summary[1]}<br/>{summary[2]}<br/><br/>", styles["h4"])

    table_data = []
    table_headers = ['ID', 'Car', 'Price', 'Total Sales']
    table_data.append(table_headers)

    for entry in data:
        # print(entry)
        table_data.append([entry['id'], format_car(
            entry['car']), entry['price'], entry['total_sales']])
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    report.build([report_title, report_summary, report_table])

    # TODO: send the PDF report as an email attachment
    message = EmailMessage()
    sender = 'automation@example.com'
    recipient = '<user>@example.com'
    subject = 'Sales summary for last month'
    body = 'The same summary from the PDF, but using \n between the lines'
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    attachment_path = 'cars.pdf'
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as attachment:
        message.add_attachment(attachment.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
    mail_server = smtplib.SMTP('localhost')
    mail_pass = getpass.getpass('Password? ')
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()


if __name__ == "__main__":
    main(sys.argv)
