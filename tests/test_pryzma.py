from hypothesis import given
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import one_of
from hypothesis.strategies import tuples
from strategies import channels
from strategies import hues
from strategies import rgbhex

from pryzma.color import from_hex
from pryzma.pryzma import Pryzma


def is_valid_color(hexcolor):
    color = from_hex(hexcolor)
    return all(c >= 0 and c <= 1 for c in color)


@given(
    rgbhex,
    rgbhex,
    one_of(floats(min_value=1 / 21, max_value=21), just(None)),
    one_of(just(1), just(-1)),
    channels,
    one_of(tuples(hues, hues, hues, hues, hues, hues), just(None)),
    integers(min_value=2, max_value=1e3),
)
def test_colors_have_8_valid_items(
    bg, fg, contrast_ratio, contrast_ratio_sign, saturation, hues, sample_rate
):
    if contrast_ratio:
        contrast_ratio *= contrast_ratio_sign
    colors = Pryzma(
        bg,
        fg,
        contrast_ratio,
        saturation,
        hues,
        sample_rate,
    ).colors
    assert len(colors) == 8
    assert all(is_valid_color(color) for color in colors)
