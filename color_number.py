from color_constants import MAJOR_COLORS, MINOR_COLORS

class ColorNumber:
    @staticmethod
    def from_colors(major_color, minor_color):
        """Get the pair number from major and minor colors."""
        major_index = MAJOR_COLORS.index(major_color)
        minor_index = MINOR_COLORS.index(minor_color)
        return major_index * len(MINOR_COLORS) + minor_index + 1

    @staticmethod
    def from_pair_number(pair_number):
        """Get the major and minor color from the given pair number."""
        pair_number_index = pair_number - 1
        major_index = pair_number_index // len(MINOR_COLORS)
        minor_index = pair_number_index % len(MINOR_COLORS)
        return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
