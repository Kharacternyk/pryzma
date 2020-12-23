#!/usr/bin/env python

from colorsys import hls_to_rgb
from pryzma.color import contrast


def generate_palette(
    bg=(1, 1, 1), saturation=1, hue_offset=0, contrast_ratio=5, sample_rate=100
):
    yield bg
    hues = ((hue * 60 + hue_offset) / 360 for hue in range(6))
    for hue in hues:
        lightness_contrast = (
            (lightness, contrast(*hls_to_rgb(hue, lightness, saturation), *bg))
            for lightness in (x / (sample_rate - 1) for x in range(sample_rate))
        )
        best_lightness, best_contrast = min(
            lightness_contrast, key=lambda p: abs(p[1] - contrast_ratio)
        )
        yield hls_to_rgb(hue, best_lightness, saturation)
