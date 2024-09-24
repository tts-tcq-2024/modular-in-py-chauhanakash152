from color_constants import MAJOR_COLORS, MINOR_COLORS

class ColorPair:
    @staticmethod
    def from_pair_number(pair_number):
        """Get the major and minor color from a pair number."""
        idx = pair_number - 1
        major_index = idx // len(MINOR_COLORS)
        minor_index = idx % len(MINOR_COLORS)
        return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

    @staticmethod
    def to_string(major_color, minor_color):
        """Convert major and minor color to a string representation."""
        return f'{major_color} {minor_color}'
