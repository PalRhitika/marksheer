import re

__all__ = ["scores_rows"]


# Master HTML: marksheet.html
html_snippet = """
<tr class="bt2">
    <td class="r sn">__SN__</td>
    <td class="l subject bl2">__SUBJECT__</td>
    <td class="c ch bl2">__CREDIT_HOUR__</td>
    <td class="r fm bl2">__TH_FM__</td>
    <td class="r fm bl2">__PR_FM__</td>
    <td class="r pm bl2">__TH_PM__</td>
    <td class="r pm bl2">__PR_PM__</td>
    <td class="r mo bl2">__TH_MO__</td>
    <td class="r mo bl2">__PR_MO__</td>
    <td class="r gpa bl2">__GPA__</td>
    <td class="c grade bl2">__GRADE__</td>
</tr>
"""


def scores_rows(subjects=[]):
    na = "n/a"
    html_row = """"""
    counter = 1
    for subject in subjects:
        hs = html_snippet
        hs = hs.replace("__SN__", str(counter))
        hs = hs.replace("__SUBJECT__", str(subject.get("name", na)))
        hs = hs.replace("__CREDIT_HOUR__", str(subject.get("ch", na)))
        hs = hs.replace("__TH_FM__", str(subject.get("thfm", na)))
        hs = hs.replace("__PR_FM__", str(subject.get("prfm", na)))
        hs = hs.replace("__TH_PM__", str(subject.get("thpm", na)))
        hs = hs.replace("__PR_PM__", str(subject.get("prpm", na)))
        hs = hs.replace("__TH_MO__", str(subject.get("thmo", na)))
        hs = hs.replace("__PR_MO__", str(subject.get("prmo", na)))
        hs = hs.replace("__GPA__", str(subject.get("gpa", na)))
        hs = hs.replace("__GRADE__", str(subject.get("grade", na)))
        html_row += hs
        counter += 1

    # multi lines of total rows to leave a vertical space in the scores area
    if(counter<13):
        for i in range(0, 13 - counter):
            html_row += re.sub(r"\_\_[A-Z0-9\_]+\_\_", "", html_snippet)

    return html_row
