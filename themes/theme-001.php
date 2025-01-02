<?php
$marksheet = file_get_contents("marksheet.html");
$header = file_get_contents("_header.html");
$scores = file_get_contents("_scores.html");
$summary = file_get_contents("_summary.html");
$gradings = file_get_contents("_gradings.html");

$css = '<link rel="stylesheet" href="marksheet.css" />';
$theme = $marksheet;
$theme = str_replace("<!-- #header-html -->", $header, $theme);
$theme = str_replace("<!-- #scores-table -->", $scores, $theme);
$theme = str_replace("<!-- #summary-table -->", $summary, $theme);
$theme = str_replace("<!-- #gradings-table -->", $gradings, $theme);
$theme = str_replace($css, '', $theme);
$theme = str_replace('<!-- #css -->', $css, $theme);

file_put_contents("theme-000.html", $theme);
