import asyncio
from playwright.async_api import async_playwright
import json

# Import the function that generates the score rows
from scores_rows import scores_rows

async def html_to_pdf(html_content, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.pdf(path=output_path)
        await browser.close()

def fc(filename: str):
    contents = """"""
    with open(filename,'r', encoding="utf-8") as f:
        contents = f.read()

    return contents
# Sample subject data for testing (you can replace this with real data)
marksheet = json.loads(fc("samples/marksheet.json"))
# Read the template HTML file
html_file_path = "theme/marksheettest.html"
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Generate the dynamic score rows
score_rows = scores_rows(marksheet[0].get("subjects"))

# Inject the dynamic rows into the HTML content
html_content = html_content.replace("{{ scores_rows }}", score_rows)

# Output path for the PDF
output_path = "output.pdf"

# Generate the PDF from the modified HTML
asyncio.run(html_to_pdf(html_content, output_path))
