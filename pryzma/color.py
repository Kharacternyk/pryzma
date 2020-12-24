def pprint(r, g, b):
    """Reproduce a color via the terminal escape sequences."""
    switchfg = f"\x1b[38;2;{round(r*255)};{round(g*255)};{round(b*255)}m"
    blocks = "███"
    switchnull = "\x1b[0m"
    print(switchfg + blocks + switchnull, end="")


def to_hex(r, g, b):
    """Return the hexadecimal representation of a color."""
    return f"#{round(r*255):02X}{round(g*255):02X}{round(b*255):02X}"


def from_hex(s):
    """Parse the hexadecimal representation of a color."""
    s = s.lstrip("#")
    return tuple(int(s[i : i + 2], 16) / 255 for i in (0, 2, 4))


def hue_normalize(hue):
    """Normalize an angle to fit within [0; 360)."""
    while hue >= 360:
        hue -= 360
    while hue < 0:
        hue += 360
    return hue


def relative_luminance(r, g, b):
    """Compute the relative luminance of a color.

    The algorithm is described in https://www.w3.org/TR/WCAG20/#relativeluminancedef.
    """

    def normalize(c):
        if c <= 0.03928:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    return normalize(r) * 0.2126 + normalize(g) * 0.7152 + normalize(b) * 0.0722


def contrast(rgb1, rgb2):
    """Compute the contrast ratio of two colors.

    The algorithm is described in https://www.w3.org/TR/WCAG20/#contrast-ratiodef.
    """
    contrast = (relative_luminance(*rgb1) + 0.05) / (relative_luminance(*rgb2) + 0.05)
    return contrast
