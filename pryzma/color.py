#!/usr/bin/env python

from cached_property import cached_property
from math import sqrt, nan
from PIL import Image


class Color:
    def __init__(self, r, g, b):
        self.__r = r
        self.__g = g
        self.__b = b

    r = property(lambda self: self.__r)
    g = property(lambda self: self.__g)
    b = property(lambda self: self.__b)
    rgb = property(lambda self: [self.r, self.g, self.b])

    def __str__(self):
        switchred = (
            f"\x1b[38;2;{round(self.r*255)};{round(self.g*255)};{round(self.b*255)}m"
        )
        blocks = "███"
        switchnull = "\x1b[0m"
        return switchred + blocks + switchnull

    @cached_property
    def hue(self):
        def normalize(angle):
            if angle < 0:
                return angle + 360
            return angle

        maxchannel = max(self.rgb)
        minchannel = min(self.rgb)
        if maxchannel == minchannel:
            return nan
        if self.r == maxchannel:
            return normalize((self.g - self.b) / (maxchannel - minchannel) * 60)
        if self.g == maxchannel:
            return normalize((2.0 + (self.b - self.r) / (maxchannel - minchannel)) * 60)
        if self.b == maxchannel:
            return normalize((4.0 + (self.r - self.g) / (maxchannel - minchannel)) * 60)

    @cached_property
    def relative_luminance(self):
        def normalize(c):
            if c <= 0.03928:
                return c / 12.92
            return ((c + 0.055) / 1.055) ** 2.4

        return (
            normalize(self.r) * 0.2126
            + normalize(self.g) * 0.7152
            + normalize(self.b) * 0.0722
        )

    def compute_contrast(self, color):
        contrast = (self.relative_luminance + 0.05) / (color.relative_luminance + 0.05)
        if contrast < 1:
            return 1 / contrast
        return contrast

    def compute_difference(self, color):
        redmean = (self.r + color.r) / 2
        weighted_dr = (self.r - color.r) ** 2 * (2 + redmean)
        weighted_dg = (self.g - color.g) ** 2 * 4
        weighted_db = (self.b - color.b) ** 2 * (3 - redmean)
        return sqrt(weighted_dr + weighted_dg + weighted_db) / 3


def generate_palette(image_path):
    pixels = (
        Color(r / 255, g / 255, b / 255)
        for (r, g, b) in Image.open(image_path).getdata()
    )
    huemap = {
        hue: list() for hue in ("red", "yellow", "green", "cyan", "blue", "magenta")
    }
    for color in pixels:
        if color.hue is nan:
            continue
        elif round(color.hue) in range(31, 90):
            huemap["yellow"].append(color)
        elif round(color.hue) in range(91, 150):
            huemap["green"].append(color)
        elif round(color.hue) in range(151, 210):
            huemap["cyan"].append(color)
        elif round(color.hue) in range(211, 270):
            huemap["blue"].append(color)
        elif round(color.hue) in range(271, 330):
            huemap["magenta"].append(color)
        else:
            huemap["red"].append(color)
    return huemap
