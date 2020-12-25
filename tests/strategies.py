from hypothesis.strategies import floats
from hypothesis.strategies import tuples

from pryzma.color import to_hex

channels = floats(min_value=0, max_value=1)
rgb = tuples(channels, channels, channels)
rgbhex = rgb.map(lambda rgb: to_hex(*rgb))
