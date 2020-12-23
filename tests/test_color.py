from pryzma.color import hue_normalize, relative_luminance, contrast
from hypothesis import given
from hypothesis.strategies import floats
from strategies import channel, color


@given(floats(min_value=-1e4, max_value=1e4))
def test_normalized_hue_within_0_360(hue):
    norm = hue_normalize(hue)
    assert norm >= 0 and norm < 360


@given(channel, channel, channel)
def test_relative_luminance_within_0_1(r, g, b):
    rl = relative_luminance(r, g, b)
    assert rl >= 0 and rl <= 1


@given(color, color)
def test_contrast_within_1_21(rgb1, rgb2):
    c = contrast(rgb1, rgb2)
    assert c >= 1 and c <= 21
