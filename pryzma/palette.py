#!/usr/bin/env python

from math import floor, ceil
from PIL import Image
from tqdm import tqdm
from pryzma.color import saturation, hue


def generate_palette(image_path):
    image = Image.open(image_path)
    pixels = ((r / 255, g / 255, b / 255) for (r, g, b) in image.getdata())
    huemap = {i: [[0, 0, 0], 0] for i in range(6)}
    for (r, g, b) in tqdm(pixels, total=(image.width * image.height)):
        if saturation(r, g, b) < 0.3:
            continue

        neighbour1 = floor(hue(r, g, b) / 60)
        neighbour2 = ceil(hue(r, g, b) / 60)
        weight1 = 1 - (hue(r, g, b) / 60 - neighbour1)
        weight2 = 1 - weight1
        if neighbour2 == 6:
            neighbour2 = 0

        huemap[neighbour1][1] += weight1
        huemap[neighbour2][1] += weight2
        for i in range(3):
            huemap[neighbour1][0][i] += (r, g, b)[i] * weight1
        for i in range(3):
            huemap[neighbour2][0][i] += (r, g, b)[i] * weight2

    for i in range(6):
        for c in range(3):
            huemap[i][0][c] /= huemap[i][1]

    return huemap
