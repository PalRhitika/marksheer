import json
import pymupdf  # PyMuPDF
import re
from bs4 import BeautifulSoup
from rgb8 import replace_colors_with_black_or_white
from scores_rows import scores_rows
# from students import students


# File Contents
def fc(filename: str):
    contents = """"""
    with open(filename, encoding="utf8") as f:
        contents = f.read()

    return contents


student = json.loads(fc("samples/student.json"))

marksheet_html = fc("marksheet.html")
grading_html = fc("gradings.html")
marksheet_html = marksheet_html.replace("<!-- #gradings-table -->", grading_html)
marksheet_html = marksheet_html.replace(
    # must match exactly
    # we are modifying and providing same css as parameter
    '<link rel="stylesheet" href="marksheet.css" />', ""
)


css = fc("marksheet.css")
css = replace_colors_with_black_or_white(css)


def generate_marksheet(student):
    doc = pymupdf.open()
    page = doc.new_page(width=595, height=842)

    # Replace the data
    soup = BeautifulSoup(marksheet_html, "html.parser")
    tbody = soup.find("tbody", id="scores")
    tbody.clear()
    tbody.append(BeautifulSoup(scores_rows(student["subjects"]), "html.parser"))
    marksheet = soup.prettify()

    xy = [50, 50]
    wh = [590, 520] # dimension of the table
    page.insert_htmlbox(
        pymupdf.Rect(xy[0], xy[1], wh[0] + xy[0], wh[1] + xy[1]),
        marksheet,
        css=css,
        scale_low=0,
        archive=False,
        rotate=0,
        oc=0,
        opacity=1,
        overlay=True,
    )

    return doc


bulk_pdf = pymupdf.open()
# Loop through the students and produce PDF
doc = generate_marksheet(student)
bulk_pdf.insert_pdf(doc)


bulk_pdf.save(
    "marksheets-combined.pdf", garbage=4, deflate=True, clean=2, deflate_images=True
)

if __name__ == "__main__":
    print("Marksheets combined successfully!")
