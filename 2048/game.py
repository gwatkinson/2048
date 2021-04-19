import numpy as np


class Game:
    """
    The 2048 game class.

    ...

    Attributes
    ----------
    board : numpy array
        board state of the game
    score : float
        score associated to the board

    Methods
    -------
    update(direction):
        Updates the board with the given direction.
    """

    def __init__(self, board=np.zeros((4, 4)), score=0.0):
        """
        Constructs all the necessary attributes for the game object.

        Parameters
        ----------
            board : numpy array, optional
                board state of the game (default is np.zeros((4,4)))
            score : float, optional
                score associated to the board (default is 0.0)
        """
        self.board = board
        self.score = score

    def process_column(self, column):
        """
        Process a given vector with the rules of 2048, and from left to right.

        Parameters
        ----------
        column : numpy array
            a numpy array of length 4
        
        Returns
        -------
        numpy array
            The updated array of column
        """
        

    def update(self, direction):
        """
        Updates the board with the given direction.

        Parameters
        ----------
        direction : str
            The direction with which to update the board. Values must be in `["l", "r", "t", "b"]` for *left*, *right*, *top* and *bottom*.

        Returns
        -------
        None
        """
        assert direction in ["l","r","t","b"], f'Direction 
        must be in ["l", "r", "t", "b"], not "{direction}".'
        pass