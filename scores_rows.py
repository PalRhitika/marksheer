import re

__all__ = ["scores_rows"]


# Mind the number of columns: 11
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
    <td class="c gpa bl2">__GPA__</td>
    <td class="r grade bl2">__GRADE__</td>
</tr>
"""


def scores_rows(subjects=[]):
    row = """"""
    counter = 0
    for subject in subjects:
        counter += 1

        hs = html_snippet
        hs = hs.replace("__SN__", str(counter))
        hs = hs.replace("__SUBJECT__", str(subject.get("name", "n/a")))
        hs = hs.replace("__CREDIT_HOUR__", str(subject.get("ch", "n/a")))
        hs = hs.replace("__TH_FM__", str(subject.get("thfm", "n/a")))
        hs = hs.replace("__PR_FM__", str(subject.get("prfm", "n/a")))
        hs = hs.replace("__TH_PM__", str(subject.get("thpm", "n/a")))
        hs = hs.replace("__PR_PM__", str(subject.get("prpm", "n/a")))
        hs = hs.replace("__TH_MO__", str(subject.get("thmo", "n/a")))
        hs = hs.replace("__PR_MO__", str(subject.get("prmo", "n/a")))
        hs = hs.replace("__GPA__", str(subject.get("gpa", "n/a")))
        hs = hs.replace("__GRADE__", str(subject.get("grade", "n/a")))
        row += hs

    # 12 lines of total rows, to leave a vertical space
    if(len(subjects)<12):
        for i in range(12 - len(subjects)):
            row += re.sub(r'\_\_[A-Z0-9\_]+\_\_', '', html_snippet)

    return row
