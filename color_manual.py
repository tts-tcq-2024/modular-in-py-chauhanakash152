from color_pair import ColorPair
from color_constants import MAJOR_COLORS, MINOR_COLORS


class ColorManual:
    @staticmethod
    def generate_reference():
        """
        Generate a reference manual for color coding.

        This method creates a string representation of color pairs, where
        each line corresponds to a unique pair number and its associated 
        major and minor colors. The color pairs are derived from predefined
        major and minor color lists.

        The output format for each line is:
        "<pair_number>: <major_color> <minor_color>".

        Returns:
            str: A formatted string containing all color pairs in the 
            reference manual, each on a new line.
        """
        max_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
        return '\n'.join(
            f'{current_pair_index}: {ColorPair.to_string(*ColorPair.from_pair_number(current_pair_index))}'  # noqa
            for current_pair_index in range(1, max_pairs + 1)
        )
