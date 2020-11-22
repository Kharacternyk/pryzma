#!/usr/bin/env python

class Color():
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r / 255, g / 255, b / 255

    def relative_luminance(self):
        def normalize(c):
            if c <= 0.03928:
                return c / 12.92
            return ((c + 0.055) / 1.055)**2.4
        return normalize(self.r) * 0.2126 + \
               normalize(self.g) * 0.7152 + \
               normalize(self.b) * 0.0722
