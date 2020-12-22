#!/usr/bin/env python

from colorsys import hls_to_rgb
from pryzma.color import contrast


def generate_palette(bg=(1, 1, 1), saturation=1, hue_offset=0, contrast_ratio=5):
    hues = ((hue * 60 + hue_offset) / 360 for hue in range(6))
    for hue in hues:
        print(hue)
        lightness_upper_bound = 1
        lightness_lower_bound = 0
        lightness = (lightness_upper_bound + lightness_lower_bound) / 2
        while lightness_upper_bound - lightness_lower_bound > 0.01:
            # Changing bg is unsupported currently
            if contrast(*hls_to_rgb(hue, lightness, saturation), *bg) >= contrast_ratio:
                lightness_lower_bound = lightness
                lightness = (lightness_upper_bound + lightness_lower_bound) / 2
            else:
                lightness_upper_bound = lightness
                lightness = (lightness_upper_bound + lightness_lower_bound) / 2
            print(lightness_lower_bound, lightness_upper_bound, lightness)
        yield hls_to_rgb(hue, lightness, saturation)
