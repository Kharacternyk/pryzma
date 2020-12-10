from hypothesis import given
from hypothesis.strategies import floats
from math import nan
from pryzma.color import saturation, hue, relative_luminance

channel = floats(min_value=0, max_value=1)


@given(channel, channel, channel)
def test_saturation_within_0_1(r, g, b):
    s = saturation(r, g, b)
    assert s >= 0 and s <= 1


@given(channel, channel, channel)
def test_hue_within_0_360_or_nan(r, g, b):
    h = hue(r, g, b)
    assert h >= 0 and h < 360 or h is nan


@given(channel, channel, channel)
def test_relative_luminance_within_0_1(r, g, b):
    rl = relative_luminance(r, g, b)
    assert rl >= 0 and rl <= 1
