from color_pair import ColorPair
from color_constants import MAJOR_COLORS, MINOR_COLORS


class ColorManual:
    @staticmethod
    def generate_reference():
        """Generate a reference manual for color coding."""
        max_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
        return '\n'.join(
            f'{current_pair_index}: {ColorPair.to_string(*ColorPair.from_pair_number(current_pair_index))}' # noqa
            for current_pair_index in range(1, max_pairs + 1)
        )
