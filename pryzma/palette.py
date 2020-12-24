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

    def wal(self):
        print(
            f"""
            {{
                "special": {{
                    "background": "{to_hex(*self.__colors[0])}",
                    "foreground": "{to_hex(*self.__colors[7])}",
                    "cursor":     "{to_hex(*self.__colors[7])}"
                }},

                "colors": {{
                    "color0":  "{to_hex(*self.__colors[0])}",
                    "color1":  "{to_hex(*self.__colors[1])}",
                    "color2":  "{to_hex(*self.__colors[2])}",
                    "color3":  "{to_hex(*self.__colors[3])}",
                    "color4":  "{to_hex(*self.__colors[4])}",
                    "color5":  "{to_hex(*self.__colors[5])}",
                    "color6":  "{to_hex(*self.__colors[6])}",
                    "color7":  "{to_hex(*self.__colors[7])}",

                    "color8":  "{to_hex(*self.__colors[0])}",
                    "color9":  "{to_hex(*self.__colors[1])}",
                    "color10": "{to_hex(*self.__colors[2])}",
                    "color11": "{to_hex(*self.__colors[3])}",
                    "color12": "{to_hex(*self.__colors[4])}",
                    "color13": "{to_hex(*self.__colors[5])}",
                    "color14": "{to_hex(*self.__colors[6])}",
                    "color15": "{to_hex(*self.__colors[7])}"
                }}
            }}"""
        )
