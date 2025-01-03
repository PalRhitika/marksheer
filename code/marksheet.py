import re
import json
import pymupdf
from bs4 import BeautifulSoup
from rgb8 import replace_colors_with_black_or_white
from scores_rows import scores_rows
from libraries import fc, fw, compact_html
from fill import fill_pdf_image_background

marksheet_html = fc("../themes/marksheet.html")
marksheet_html = marksheet_html.replace(
    "<!-- #header-html -->", fc("../themes/_header.html")
)
marksheet_html = marksheet_html.replace(
    "<!-- #scores-table -->", fc("../themes/_scores.html")
)
marksheet_html = marksheet_html.replace(
    "<!-- #summary-table -->", fc("../themes/_summary.html")
)
marksheet_html = marksheet_html.replace(
    "<!-- #gradings-table -->", fc("../themes/_gradings.html")
)
marksheet_html = marksheet_html.replace(
    # must match exactly
    # we are modifying and providing same css as parameter
    '<link rel="stylesheet" href="marksheet.css" />', ""
)


css = fc("../themes/marksheet.css")
css = replace_colors_with_black_or_white(css)


fw("../individuals/marksheet.css", css)
fw(
    "../individuals/full.html",
    marksheet_html.replace(
        "<!-- #css -->", '<link rel="stylesheet" href="marksheet.css" />'
    ),
)


def generate_marksheet(student={}, sequence: int = 0):
    doc = pymupdf.open()
    page = doc.new_page(width=595, height=842)

    # Optional
    page = fill_pdf_image_background(page, "../themes/logo-001.png")

    # Replace the data
    soup = BeautifulSoup(marksheet_html, "html.parser")
    tbody = soup.find("tbody", id="scores")
    tbody.clear()
    tbody.append(BeautifulSoup(scores_rows(student["subjects"]), "html.parser"))
    marksheet = soup.prettify()
    marksheet = marksheet.replace("__SEQUENCE__", sequence)
    marksheet = marksheet.replace("__STUDENT_FULL_NAME__", student.get("student", {}).get("name", ""))
    marksheet = marksheet.replace("__SCHOOL_NAME__", student.get("school", {}).get("name", ""))
    marksheet = marksheet.replace("__SCHOOL_ADDRESS__", student.get("school", {}).get("address", ""))
    marksheet = marksheet.replace(
        " __SCHOOL_DISTRICT__", student.get("school", {}).get("district", "")
    )

    fw(
        f"../individuals/individual-{sequence}.html",
        compact_html(marksheet.replace(
        "<!-- #css -->", '<link rel="stylesheet" href="marksheet.css" />'
    ))
    )  # Remove this line

    xy = [50, 50]
    wh = [590, 600] # dimension of the html area
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


# student = json.loads(fc("../samples/student.json"))
students = json.loads(fc("../samples/students.json"))

bulk_pdf = pymupdf.open()

batch = ""
# for sequence in range(1, 10+1):  # Loop through the students and produce PDF
for sequence, student in enumerate(students):
    doc = generate_marksheet(student, str(sequence).zfill(4))
    bulk_pdf.insert_pdf(doc)


bulk_pdf.save(
    "../pdfs/combined.pdf",
    garbage=4,
    clean=2,
    deflate=True,
    deflate_images=True,
    deflate_fonts=True
)

if __name__ == "__main__":
    print("Marksheets combined successfully!")
