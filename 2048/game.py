# Import the used packages.
import numpy as np
import numpy.random as rd

# Import the util functions
from utils import *


# Define the Game class
class Game:
    """
    The 2048 game class.

    ...

    Attributes
    ----------
    board : numpy array
        Board state of the game (default is np.zeros((4, 4))).
    score : float
        Score associated to the board (default is 0.0).
    lost : boolean
        Boolean to indicate if the game is lost (default is False).
    zeros : numpy array
        An array that contains the indexes of the zeros.
    len_zeros : int
        The number of zeros on the board.

    Methods
    -------
    add_random_tile():
        Randomly add a new tile on a empty tile of the board.
    move(direction, copy):
        Updates the board with the given direction.
    update_zeros():
        Updates the zeros attributes.
    check_lost():
        Checks if the game is over.
    update_score():
        Updates the score
    iterate(direction):
        Makes a move and all the steps of the game
        (add new tile, check for game over, ...).
    print():
        Prints the board
    """

    def __init__(self, board=np.zeros((4, 4)), score=0.0, lost=False):
        """
        Constructs all the necessary attributes for the game object.

        Parameters
        ----------
            board : numpy array, optional
                Board state of the game (default is np.zeros((4,4))).
            score : float, optional
                Score associated to the board (default is 0.0).
        """
        self.board = board
        self.score = score
        self.lost = lost
        self.zeros = np.argwhere(board == 0)
        self.len_zeros = len(self.zeros)
        if (board == np.zeros((4, 4))).all():
            self.add_random_tile()

    def add_random_tile(self):
        """
        Adds a new tile with value 2 or 4 (with a 0.9/0.1 probability distribution)
        in a empty tile of the board.

        Modifies the board array.

        Returns
        -------
        None
        """
        if self.len_zeros == 0:  # Should never be True
            self.lost = True
        else:
            p = rd.randint(self.len_zeros)
            ind = self.zeros[p]
            self.board[ind[0], ind[1]] = rd.choice([2, 4], p=[0.9, 0.1])
            self.zeros = np.delete(self.zeros, p, axis=0)
            self.len_zeros -= 1

    def move(self, direction, copy=False):
        """
        Updates the board with the given direction.

        Parameters
        ----------
        direction : int
            The direction with which to update the board.
            Values must be between 0 and 3 for *left*, *right*, *top* and *bottom*.
        copy : boolean
            Weither or not to make a copy the board then return it.

        Returns
        -------
        tuple
            (If copy is True, returns the modified array else only returns the boolean,
            A boolean if indicating if changes occurred)
        """
        assert direction in list(
            range(4)
        ), f'Direction must be in {list(range(4))}, not "{direction}".'

        modif = []

        if copy:
            m = self.board.copy()
        else:
            m = self.board

        for i in range(4):
            if direction == 0:
                col = m[i, ::-1]
                modif.append(combine_column(col))
                m[i] = col[::-1]
            elif direction == 1:
                col = m[i]
                modif.append(combine_column(col))
                m[i] = col
            elif direction == 2:
                col = m[::-1, i]
                modif.append(combine_column(col))
                m[:, i] = col[::-1]
            elif direction == 3:
                col = m[:, i]
                modif.append(combine_column(col))
                m[:, i] = col

        if copy:
            return m, any(modif)
        else:
            return any(modif)

    def update_zeros(self):
        """
        Updates the zeros attributes of the class.

        Returns
        -------
        None
        """
        self.zeros = np.argwhere(self.board == 0)
        self.len_zeros = len(self.zeros)

    def check_lost(self):
        """
        Checks if the game is over.

        Returns
        -------
        None
        """
        if self.len_zeros != 0:
            return False

        moved = [self.move(d, copy=True)[1] for d in range(4)]

        if any(moved):
            return False
        return True

    def update_score(self):
        pass

    def iterate(self, direction):
        """
        Function to iterate the game with the given direction.

        It doesn't move if the game is already lost.
        It tries to move with the given direction,
        if it doesn't move, returns False.
        Then it finds the zeros and add a new tile.
        Then it updates the score.
        Finally, it checks if the game is lost when there are no zeros left.

        Parameters
        ----------
        direction : int
            The direction with which to update the board.
            Values must be between 0 and 3 for *left*, *right*, *top* and *bottom*.

        Returns
        -------
        bool
            Returns None if the game is lost, else returns if there were changes.
        """
        if self.lost:
            return

        bool = self.move(direction=direction)
        if not bool:
            return False

        self.update_zeros()
        self.add_random_tile()
        self.update_score()

        if self.len_zeros == 0:
            self.lost = self.check_lost()
            if self.lost:
                return

        return True

    def print(self):
        print(self.board)

    def __str__(self):
        """
        A rapid display for the game.

        Prints the array and the number of zeros.

        Returns
        -------
        str
            The number of zeros
        """
        print(self.board)
        if self.lost:
            return f"The game is lost."
        return f"There is {self.len_zeros} zeros."