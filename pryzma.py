#!/usr/bin/env python

from cached_property import cached_property
from math import sqrt


class Color:
    def __init__(self, r, g, b):
        self.__r = r / 255
        self.__g = g / 255
        self.__b = b / 255

    r = property(lambda self: self.__r)
    g = property(lambda self: self.__g)
    b = property(lambda self: self.__b)

    def __str__(self):
        switchred = f"\x1b[38;2;{round(self.r*255)};{round(self.g*255)};{round(self.b*255)}m"
        blocks = "███"
        switchnull = "\x1b[0m"
        return switchred + blocks + switchnull

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
