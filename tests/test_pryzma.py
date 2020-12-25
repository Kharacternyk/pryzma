from hypothesis import given
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import one_of
from strategies import channels
from strategies import rgbhex

from pryzma.pryzma import Pryzma


@given(
    rgbhex,
    rgbhex,
    one_of(floats(min_value=1 / 21, max_value=21), just(None)),
    channels,
    channels,
    integers(min_value=2, max_value=1e3),
)
def test_print_has_8_lines(bg, fg, contrast_ratio, saturation, hue_offset, sample_rate):
    assert (
        len(
            Pryzma(
                bg, fg, contrast_ratio, saturation, hue_offset, sample_rate=sample_rate
            )
            .print()
            .splitlines()
        )
        == 8
    )
