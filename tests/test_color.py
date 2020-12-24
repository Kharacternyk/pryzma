from hypothesis import given
from hypothesis.strategies import floats
from strategies import rgb

from pryzma.color import contrast
from pryzma.color import from_hex
from pryzma.color import hue_normalize
from pryzma.color import relative_luminance
from pryzma.color import to_hex


@given(rgb)
def test_to_hex_within_000000_FFFFFF(rgb):
    s = to_hex(*rgb)
    assert s >= "#000000" and s <= "#FFFFFF"


def test_from_hex():
    assert from_hex("#FFFFFF") == (1, 1, 1)
    assert from_hex("ffffff") == (1, 1, 1)
    assert from_hex("#000000") == (0, 0, 0)
    assert from_hex("000000") == (0, 0, 0)


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
