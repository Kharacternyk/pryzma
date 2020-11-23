#!/usr/bin/env python

from cached_property import cached_property


class Color:
    def __init__(self, r, g, b):
        self.__r = r / 255
        self.__g = g / 255
        self.__b = b / 255

    r = property(lambda self: self.__r)
    g = property(lambda self: self.__g)
    b = property(lambda self: self.__b)

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
