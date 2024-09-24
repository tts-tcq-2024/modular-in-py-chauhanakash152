from color_manual import ColorManual
from color_constants import MAJOR_COLORS, MINOR_COLORS

def get_color_from_pair_number(pair_number):
    """Get the major and minor color from a pair number."""
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)

    if major_index >= len(MAJOR_COLORS) or minor_index >= len(MINOR_COLORS):
        raise IndexError('Pair number is out of range')

    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    """Get the pair number from major and minor colors."""
    try:
        major_index = MAJOR_COLORS.index(major_color)
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError as e:
        raise ValueError(f'Invalid color: {e}')

    return major_index * len(MINOR_COLORS) + minor_index + 1

if __name__ == '__main__':
    print("Color Reference Manual:\n")
    print(ColorManual.generate_reference())
