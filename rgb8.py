import re

"""
Purpose: Replace RGB or HEX colors to monochromatic (printer ready)
Author: with AI/ChatGPT assisted
"""

__all__ = ["replace_colors_with_black_or_white"]

def rgb_to_black_or_white(r, g, b):
    # Normalize the RGB values to [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Calculate luminance using the standard formula
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

    # If luminance is greater than 0.5, return white (255, 255, 255), else black (0, 0, 0)
    if luminance > 0.5:
        return 255, 255, 255  # White
    else:
        return 0, 0, 0  # Black


def hex_to_rgb(hex_color):
    # Remove the '#' and convert hex to RGB
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    # Convert RGB to hex format
    return f"#{r:02X}{g:02X}{b:02X}"


def replace_colors_with_black_or_white(text):
    # Regular expression to find rgb(r, g, b) and hex color values
    rgb_pattern = r"rgb\((\d+), (\d+), (\d+)\)"
    hex_pattern = r"#[0-9A-Fa-f]{6}"

    # Function to replace the RGB color with black or white
    def replace_rgb(match):
        r = int(match.group(1))
        g = int(match.group(2))
        b = int(match.group(3))

        # Get black or white based on the color luminance
        black_or_white = rgb_to_black_or_white(r, g, b)

        # Return the new color in hex format
        return rgb_to_hex(*black_or_white)

    # Function to replace the hex color with black or white
    def replace_hex(match):
        hex_color = match.group(0)
        r, g, b = hex_to_rgb(hex_color)

        # Get black or white based on the color luminance
        black_or_white = rgb_to_black_or_white(r, g, b)

        # Return the new color in hex format
        return rgb_to_hex(*black_or_white)

    # Replace all RGB and Hex colors in the text
    text = re.sub(rgb_pattern, replace_rgb, text)
    text = re.sub(hex_pattern, replace_hex, text)

    return text


if __name__ == "main":

    # Example usage
    input_text = (
        "This is a test text with colors rgb(100, 150, 200), #FF5733, and rgb(0, 0, 0)."
    )
    output_text = replace_colors_with_black_or_white(input_text)

    print(f"Original text: {input_text}")
    print(f"Modified text: {output_text}")
