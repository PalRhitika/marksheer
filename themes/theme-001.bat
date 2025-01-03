SET $marksheet = Get-Content "marksheet.html"

SET $header = Get-Content "_header.html"
SET $scores = Get-Content "_scores.html"
SET $summary = Get-Content "_summary.html"
SET $gradings = Get-Content "_gradings.html"

sed -i -e 's/few/asd/g' hello.txt