import json
import pymupdf  # PyMuPDF
import re
from bs4 import BeautifulSoup
from rgb8 import replace_colors_with_black_or_white
from scores_rows import scores_rows
# from students import students

student = {}
with open("samples/student.json") as f:
    student = json.loads(f.read())


html_text = """"""
with open("marksheet.html") as f:
    html_text = f.read()
    marksheet = html_text = html_text.replace(
        '<link rel="stylesheet" href="marksheet.css" />', ""
    )

css_content = """"""
with open("marksheet.css") as f:
    css_content = f.read()
    css_content = replace_colors_with_black_or_white(css_content)


def generate_marksheet(student):
    doc = pymupdf.open()
    page = doc.new_page(width=595, height=842)

    # Replace the data
    soup = BeautifulSoup(html_text, "html.parser")
    tbody = soup.find("tbody", id="scores")
    tbody.clear()
    tbody.append(BeautifulSoup(scores_rows(student["subjects"]), "html.parser"))
    marksheet = soup.prettify()

    xy = [50, 50]   # @todo Caclulate
    wh = [545, 550] # @todo Calculate dimensions of the table
    page.insert_htmlbox(
        pymupdf.Rect(xy[0], xy[1], wh[0] + xy[0], wh[1] + xy[1]),
        marksheet,
        css=css_content,
        scale_low=0,
        archive=False,
        rotate=0,
        oc=0,
        opacity=1,
        overlay=True,
    )

    return doc


final_doc = pymupdf.open()
# for student in students:
doc = generate_marksheet(student)
final_doc.insert_pdf(doc)


final_doc.save("marksheets-combined.pdf", garbage=4, deflate=True, clean=2, deflate_images=True)
print("Marksheets generated and combined successfully!")
