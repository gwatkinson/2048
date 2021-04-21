# Import the used packages.
import numpy as np
import numpy.random as rd


# Define the static methods used in the Game class.
def move_column(column, max=3, length=4):
    """
    Moves the elements of the column from left to right as in 2048.

    Modifies the given array.

    Parameters
    ----------
    column : numpy array
        A numpy array of length 4 (not necessarily).
    max : int, optional
        The first position to check, between 0 and 3 included (default is 3).

        For example, 3 to check every value,
        2 to ommit the last one in the vector, ...
    length : int, optional
        The length of the column (default is 4).

    Returns
    -------
    boolean
        A boolean indicating if changes occurred.
    """
    modif = False
    i = max - 1

    while 0 <= i < max:
        if column[i] != 0:
            j = i
            while i < length - 1 and column[i + 1] == 0:
                i += 1
            if j != i:
                column[i] = column[j]
                column[j] = 0
                modif = True
        i -= 1

    return modif


def combine_column(column, length=4, move=True):
    """
    Combines the number in the column as in the 2048 rules.

    Modifies the given array.

    Parameters
    ----------
    column : numpy array
        The numpy array of length 4 (not necessarily) to combine.
        Must be processed by `move_column()`.
    length : int, optional
        The length of the column (default is 4).
    move: bool, optional
        Weither to apply `move_column()` at the start (default is True).

    Returns
    -------
    boolean
        A boolean indicating if changes occurred.
    """
    modif = False

    if move:
        modif = move_column(column=column, max=length - 1, length=length)

    for i in range(length - 1, 0, -1):
        if column[i] != 0 and column[i] == column[i - 1]:
            column[i] *= 2
            column[i - 1] = 0
            modif = True
            move_column(column=column, max=i, length=length)

    return modif