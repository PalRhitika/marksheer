import re


# File Contents
def fc(filename: str):
    contents = """"""
    with open(filename, encoding="utf8") as f:
        contents = f.read()

    return contents


# File Write
def fw(filename: str, contents: str):
    with open(filename, "w", encoding="utf8") as f:
        f.write(contents)


# Compact the HTML
def compact_html(html: str):
    ch = re.sub(r"\s+", " ", html).strip()
    ch = ch.replace("> <", "><")
    return ch
