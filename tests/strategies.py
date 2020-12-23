from hypothesis.strategies import floats, tuples

channel = floats(min_value=0, max_value=1)
color = tuples(channel, channel, channel)
