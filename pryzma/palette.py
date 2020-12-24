#!/usr/bin/env python

from colorsys import hls_to_rgb

from pryzma.color import contrast, hue_normalize, pprint, to_hex


class Palette:
    def __init__(
        self,
        bg=(0, 0, 0),
        fg=(0.8, 0.8, 0.8),
        saturation=1,
        hue_offset=0,
        sample_rate=256,
    ):
        self.__colors = [bg] + [None] * 6 + [fg]
        contrast_ratio = contrast(bg, fg)
        hues = (hue_normalize(hue * 60 + hue_offset) / 360 for hue in range(6))
        colors = [1, 3, 2, 6, 4, 5]
        for hue, color in zip(hues, colors):
            lightness_contrast = (
                (lightness, contrast(bg, hls_to_rgb(hue, lightness, saturation)))
                for lightness in (x / (sample_rate - 1) for x in range(sample_rate))
            )
            best_lightness, best_contrast = min(
                lightness_contrast, key=lambda p: abs(p[1] / contrast_ratio - 1)
            )
            self.__colors[color] = hls_to_rgb(hue, best_lightness, saturation)

    def show(self):
        for c in self.__colors:
            pprint(*c)
        print()

    def print(self):
        for c in self.__colors:
            print(to_hex(*c))
