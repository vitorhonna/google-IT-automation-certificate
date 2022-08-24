from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

# Create report object and stylesheet
report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

# Create flowable (component, a paragraph in this case) for the report title
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# Organize data in a table and create flowable for the table, with styles
table_data = []

for k, v in fruit.items():
    table_data.append([k, v])

table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# Organiza data and labels and create a flowable (drawing) for a pie chart
report_pie = Pie()
report_pie.data = []
report_pie.labels = []

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

# Build PDF using the flowables created
report.build([report_title, report_table, report_chart])