from color_constants import MAJOR_COLORS, MINOR_COLORS


class ColorPair:
    @staticmethod
    def from_pair_number(pair_number):
        """
        Get the major and minor color corresponding to the given pair number.

        Args:
            pair_number (int): The pair number to convert, starting from 1.

        Returns:
            tuple: A tuple containing the major color and minor color as strings.

        Raises:
            IndexError: If the pair number is out of range for defined colors.
        """
        pair_number_index = pair_number - 1
        major_index = pair_number_index // len(MINOR_COLORS)
        minor_index = pair_number_index % len(MINOR_COLORS)

        # Check for index validity
        if major_index >= len(MAJOR_COLORS) or minor_index >= len(MINOR_COLORS):
            raise IndexError('Pair number is out of range for available colors.')

        return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

    @staticmethod
    def to_string(major_color, minor_color):
        """
        Convert major and minor colors to a single string representation.

        Args:
            major_color (str): The name of the major color.
            minor_color (str): The name of the minor color.

        Returns:
            str: A formatted string combining both colors.
        """
        return f'{major_color} {minor_color}'
