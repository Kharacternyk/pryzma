from pryzma.color import relative_luminance, hue_normalize
from hypothesis import given
from hypothesis.strategies import floats
from strategies import channel


@given(floats(min_value=-1e4, max_value=1e4))
def test_normalized_hue_within_0_360(hue):
    norm = hue_normalize(hue)
    assert norm >= 0 and norm < 360


@given(channel, channel, channel)
def test_relative_luminance_within_0_1(r, g, b):
    rl = relative_luminance(r, g, b)
    assert rl >= 0 and rl <= 1
