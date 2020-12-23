def pprint(r, g, b):
    switchfg = f"\x1b[38;2;{round(r*255)};{round(g*255)};{round(b*255)}m"
    blocks = "███"
    switchnull = "\x1b[0m"
    print(switchfg + blocks + switchnull, end="")


def hue_normalize(hue):
    """Normalize an angle to fit within [0; 360)"""
    while hue >= 360:
        hue -= 360
    while hue < 0:
        hue += 360
    return hue


def relative_luminance(r, g, b):
    def normalize(c):
        if c <= 0.03928:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    return normalize(r) * 0.2126 + normalize(g) * 0.7152 + normalize(b) * 0.0722


def contrast(r1, g1, b1, r2, g2, b2):
    contrast = (relative_luminance(r1, g1, b1) + 0.05) / (
        relative_luminance(r2, g2, b2) + 0.05
    )
    if contrast < 1:
        return 1 / contrast
    return contrast
