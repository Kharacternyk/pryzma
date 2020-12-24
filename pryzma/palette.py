#!/usr/bin/env python
from colorsys import hls_to_rgb
from typing import Optional
from typing import Tuple

from typeguard import typechecked

from pryzma.color import contrast
from pryzma.color import from_hex
from pryzma.color import hue_normalize
from pryzma.color import pprint
from pryzma.color import to_hex


class Palette:
    @typechecked
    def __init__(
        self,
        bg: str = "#EEE8D5",
        fg: str = "#484848",
        saturation: float = 1,
        hue_offset: float = 0,
        hues: Optional[Tuple[float, float, float, float, float, float]] = None,
        sample_rate: int = 256,
    ):
        bg = from_hex(bg)
        fg = from_hex(fg)
        self.__colors = [bg] + [None] * 6 + [fg]
        contrast_ratio = contrast(bg, fg)
        if hues is None:
            hues = (hue * 60 + hue_offset for hue in range(6))
        hues = (hue_normalize(hue) / 360 for hue in hues)
        colors = (1, 3, 2, 6, 4, 5)
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
        print(f"{'Colors:': <16}", end="")
        for c in self.__colors:
            pprint(*c)
        print()
        print(f"{'Contrast ratios:': <20}", end="")
        for c in self.__colors[1:]:
            ratio = contrast(self.__colors[0], c)
            if ratio < 1:
                print(f"{1/ratio:>4.1f}", end="")
            else:
                print(f"{ratio:>4.1f}", end="")
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
