#!/usr/bin/env python3

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date


def generate_report(data):
    report = SimpleDocTemplate("processed.pdf")
    styles = getSampleStyleSheet()
    report_title = Paragraph(
        f"Processed Update on {date.today().strftime('%b %d, %Y')}<br/><br/>", styles["h1"])
    body = ''
    for item in data:
        body += f"name: {item['name']}<br/>weight: {item['weight']}<br/><br/>"
    report_body = Paragraph(body)
    report.build([report_title, report_body])
