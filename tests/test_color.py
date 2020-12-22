from hypothesis import given
from hypothesis.strategies import floats
from pryzma.color import relative_luminance

channel = floats(min_value=0, max_value=1)


@given(channel, channel, channel)
def test_relative_luminance_within_0_1(r, g, b):
    rl = relative_luminance(r, g, b)
    assert rl >= 0 and rl <= 1
