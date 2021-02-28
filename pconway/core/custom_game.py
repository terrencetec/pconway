"""Some defined games to start with
"""
import numpy as np

import pconway.core.game


class RandomGame(pconway.core.game.GameOfLife):
    """Conway's game of life initialized with random population.

    Parameters
    ----------
    nrow: int
        Number of rows in the universe.
    ncol: int
        Number of columns in the universe.
    seed: int, optional
        The seed for the random number generator.
        Defaults to 123.
    spawn_rate: float, optional
        The chance of a live cell being spawned.
        Defaults to 0.5.
    mutation_rate: float, optional
        A float from 0 to 1.
        The chance that a cell would mutate.
        This applies after each evolution.
        Defaults to 0.
    """
    def __init__(self, nrow, ncol, seed=123, spawn_rate=0.5, mutation_rate=0):
        """Constructor

        Parameters
        ----------
        nrow: int
            Number of rows in the universe.
        ncol: int
            Number of columns in the universe.
        seed: int, optional
            The seed for the random number generator.
            Defaults to 123.
        spawn_rate: float, optional
            The chance of a live cell being spawned.
            Defaults to 0.5.
        mutation_rate: float, optional
            A float from 0 to 1.
            The chance that a cell would mutate.
            This applies after each evolution.
            Defaults to 0.
        """
        np.random.seed(seed)
        matrix = np.zeros((nrow, ncol), dtype=int)
        matrix = pconway.mutation(matrix=matrix, mutation_rate=spawn_rate)
        super().__init__(matrix=matrix, mutation_rate=mutation_rate)
