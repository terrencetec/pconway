"""A game of Conway's game of life
"""
import numpy as np

import pconway.core.gameoflife


class GameOfLife:
    """A game of Conway's game of life.

    Parameters
    ----------
    matrix: array
        A matrix with entities 1 or 0 (live or dead)
    mutation_rate: float, optional
        A float from 0 to 1.
        The chance that a cell would mutate.
        This applies after each evolution.
        Defaults to 0.

    Attributes
    ----------
    matrix: array
        A matrix with entities 1 or 0 (live or dead)
    mutation_rate: float, optional
        A float from 0 to 1.
        The chance that a cell would mutate.
        This applies after each evolution.
        Defaults to 0.
    population: int
        The number of live cells in the game.
    iteration: int
        The number of iteration evolved.
    """
    def __init__(self, matrix, mutation_rate=0):
        """Constructor

        Parameters
        ----------
        matrix: array
            A matrix with entities 1 or 0 (live or dead)
        mutation_rate: float, optional
            A float from 0 to 1.
            The chance that a cell would mutate.
            This applies after each evolution.
            Defaults to 0.
        """
        self.matrix = np.array(matrix)
        self.mutation_rate = mutation_rate
        self.population = np.sum(self.matrix)
        self.iteration = 0

    def evolve(self):
        """Evolve a step.
        """
        self.matrix = pconway.core.gameoflife.compute_next_state(
            matrix=self.matrix)
        self.matrix = pconway.core.gameoflife.mutation(
            matrix=self.matrix, mutation_rate=self.mutation_rate)
        self.population = np.sum(self.matrix)
        self.iteration += 1
