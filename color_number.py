from color_constants import MAJOR_COLORS, MINOR_COLORS

class ColorNumber:
    @staticmethod
    def from_colors(major_color, minor_color):
        """
        Get the pair number from major and minor colors.

        Args:
            major_color (str): The name of the major color.
            minor_color (str): The name of the minor color.

        Returns:
            int: The pair number corresponding to the given major and minor colors.

        Raises:
            ValueError: If either color is not found in their respective color lists.
        """
        try:
            major_index = MAJOR_COLORS.index(major_color)
            minor_index = MINOR_COLORS.index(minor_color)
        except ValueError as e:
            raise ValueError(f'{str(e)} is not in the respective color list.')
        return major_index * len(MINOR_COLORS) + minor_index + 1

    @staticmethod
    def from_pair_number(pair_number):
        """
        Get the major and minor color from the given pair number.

        Args:
            pair_number (int): The pair number (1-based index).

        Returns:
            tuple: A tuple containing the major and minor colors.

        Raises:
            ValueError: If the pair number is less than 1.
            Exception: If the calculated major or minor index is out of range.
        """
        if pair_number < 1:
            raise ValueError('Pair number must be greater than or equal to 1.')
        pair_number_index = pair_number - 1
        major_index, minor_index = divmod(pair_number_index, len(MINOR_COLORS))
        if major_index >= len(MAJOR_COLORS):
            raise Exception('Major index out of range.')
        if minor_index >= len(MINOR_COLORS):
            raise Exception('Minor index out of range.')
        return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
