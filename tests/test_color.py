from hypothesis import given
from hypothesis.strategies import floats
from strategies import rgb

from pryzma.color import contrast, hue_normalize, relative_luminance


@given(floats(min_value=-1e4, max_value=1e4))
def test_normalized_hue_within_0_360(hue):
    norm = hue_normalize(hue)
    assert norm >= 0 and norm < 360


@given(rgb)
def test_relative_luminance_within_0_1(rgb):
    rl = relative_luminance(*rgb)
    assert rl >= 0 and rl <= 1


@given(rgb, rgb)
def test_contrast_within_1of21_21(rgb1, rgb2):
    c = contrast(rgb1, rgb2)
    assert c >= 1 / 21 and c <= 21
