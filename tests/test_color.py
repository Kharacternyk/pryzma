from hypothesis import given
from strategies import rgb

from pryzma.color import contrast
from pryzma.color import from_hex
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


@given(rgb)
def test_relative_luminance_within_0_1(rgb):
    rl = relative_luminance(*rgb)
    assert rl >= 0 and rl <= 1


def test_relative_luminance():
    white = (1, 1, 1)
    black = (0, 0, 0)
    assert relative_luminance(*white) == 1
    assert relative_luminance(*black) == 0


@given(rgb, rgb)
def test_contrast_abs_within_1_21(rgb1, rgb2):
    c = abs(contrast(rgb1, rgb2))
    assert c >= 1 and c <= 21


def test_contrast():
    white = (1, 1, 1)
    black = (0, 0, 0)
    assert contrast(white, black) == 21
    assert contrast(black, white) == -21
    assert contrast(black, black) == 1
    assert contrast(white, white) == 1
