# Fill background image over a pdf

import pymupdf # PyMuPDF

__all__ = ["fill_pdf_image_background"]


def fill_pdf_image_background(page, logo_image):
    page_width = page.rect.width
    page_height = page.rect.height

    # Get the logo's dimensions
    logo = pymupdf.open(logo_image)
    # logo.putalpha(128)  # 0 - 255
    logo_width = logo[0].rect.width
    logo_height = logo[0].rect.height

    # Calculate the number of logos to tile horizontally and vertically
    num_logos_x = int(page_width / logo_width) + 1  # Add 1 to cover the full page
    num_logos_y = int(page_height / logo_height) + 1  # Add 1 to cover the full page

    # Draw the image repeatedly across the entire page
    for i in range(num_logos_x):
        for j in range(num_logos_y):
            # Position each logo on the page
            x_pos = i * logo_width
            y_pos = j * logo_height

            # Insert the image at the calculated position
            page.insert_image(
                pymupdf.Rect(x_pos, y_pos, x_pos + logo_width, y_pos + logo_height),
                filename=logo_image,
                # opacity=50
            )

    return page