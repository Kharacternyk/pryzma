from hypothesis import given
from pryzma.color import relative_luminance
from strategies import channel


@given(channel, channel, channel)
def test_relative_luminance_within_0_1(r, g, b):
    rl = relative_luminance(r, g, b)
    assert rl >= 0 and rl <= 1
