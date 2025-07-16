import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

def create_pdf(therapy):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("therapy_report.html")
    html_out = template.render(
        name=therapy["name"],
        ECOG=therapy["eligibility"]["ECOG"],
        age=therapy["eligibility"]["age"],
        pfs=therapy["efficacy"]["PFS"],
        os=therapy["efficacy"]["OS"],
        schedule=therapy["schedule"],
        price="{:,}".format(therapy["price_per_cycle"]),
        side_effects=therapy["side_effects"]
    )
    output_path = "/tmp/therapy_report.pdf"
    pdfkit.from_string(html_out, output_path)
    return output_path
