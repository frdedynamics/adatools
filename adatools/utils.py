import numpy as np
import dynamixel_sdk as dxl

def to4bytes(num):
    """
    Convert an integer or a NumPy array of integers to a list of four bytes.
    Useful for sending goal positions to multiple Dynamixel servos simultaneously with groupSyncWrite.

    Parameters:
        num (int or numpy.ndarray): The input integer or NumPy array of integers.

    Returns:
        list: A list of four bytes, where each byte is represented as an integer.

    Examples:
        >>> to4bytes(4095)
        [255, 15, 0, 0]

        >>> import numpy as np
        >>> to4bytes(np.array([4095, 4000]))
        array([[255,  15,   0,   0],
               [160,  15,   0,   0]])
    """

    # Convert the input to a NumPy array if it's not already
    num_array = np.asarray(num)

    low_word = np.bitwise_and(num_array, 0xFFFF)
    high_word = np.right_shift(num_array, 16)
    low_byte = np.bitwise_and(low_word, 0xFF)
    high_byte = np.bitwise_and(high_word, 0xFF)
    return np.column_stack([
        dxl.DXL_LOBYTE(low_word),
        dxl.DXL_HIBYTE(low_word),
        dxl.DXL_LOBYTE(high_word),
        dxl.DXL_HIBYTE(high_word)
    ]).tolist()