from color_pair import ColorPair
from color_constants import MAJOR_COLORS, MINOR_COLORS

class ColorManual:
    @staticmethod
    def generate_reference():
        """Generate a reference manual for color coding."""
        max_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
        return '\n'.join(
            f'{i}: {ColorPair.to_string(*ColorPair.from_pair_number(i))}' 
            for i in range(1, max_pairs + 1)
        )
