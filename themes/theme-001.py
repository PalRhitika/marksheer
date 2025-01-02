# Read content from HTML files
with open("marksheet.html", "r") as file:
    marksheet = file.read()

with open("_header.html", "r") as file:
    header = file.read()

with open("_scores.html", "r") as file:
    scores = file.read()

with open("_summary.html", "r") as file:
    summary = file.read()

with open("_gradings.html", "r") as file:
    gradings = file.read()

# Replace placeholders with content
theme = marksheet
theme = theme.replace("<!-- #header-html -->", header)
theme = theme.replace("<!-- #scores-table -->", scores)
theme = theme.replace("<!-- #summary-table -->", summary)
theme = theme.replace("<!-- #gradings-table -->", gradings)

# Write the final output to a new file
with open("theme-000.html", "w") as file:
    file.write(theme)
