#!/usr/bin/env python

from math import nan


def pprint(r, g, b):
    switchred = f"\x1b[38;2;{round(r*255)};{round(g*255)};{round(b*255)}m"
    blocks = "███"
    switchnull = "\x1b[0m"
    print(switchred + blocks + switchnull, end="")


def saturation(r, g, b):
    maxchannel = max((r, g, b))
    minchannel = min((r, g, b))
    luminance = (maxchannel + minchannel) / 2
    # FIXME
    if maxchannel + minchannel in (0, 2):
        return 0
    if luminance > 0.5:
        return (maxchannel - minchannel) / (2 - maxchannel - minchannel)
    return (maxchannel - minchannel) / (maxchannel + minchannel)


def hue(r, g, b):
    def normalize(angle):
        if angle < 0:
            return angle + 360
        return angle

    maxchannel = max((r, g, b))
    minchannel = min((r, g, b))
    if maxchannel == minchannel:
        return nan
    if r == maxchannel:
        return normalize((g - b) / (maxchannel - minchannel) * 60)
    if g == maxchannel:
        return normalize((2.0 + (b - r) / (maxchannel - minchannel)) * 60)
    if b == maxchannel:
        return normalize((4.0 + (r - g) / (maxchannel - minchannel)) * 60)


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
