""" Test the game of life algs.
"""
import numpy as np

import pconway.core.gameoflife
import pconway.core.game
import pconway.core.custom_game


initial_matrix = np.array(
    [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,1,1]
    ]
)
final_matrix = np.array(
    [
        [0,0,0,0],
        [0,1,0,0],
        [0,1,1,1],
        [0,0,1,1]
    ]
)
random_matrix = np.array(
    [
        [1,0,0,1],
        [1,0,1,1],
        [0,0,0,1],
        [0,0,0,1]
    ]
)


def test_compute_next_state():
    test_matrix = pconway.core.gameoflife.compute_next_state(initial_matrix)
    assert np.array_equal(test_matrix, final_matrix)


def test_game():
    game = pconway.core.game.GameOfLife(matrix=initial_matrix)
    game.evolve()
    assert all(
            [
                game.population == np.sum(final_matrix),
                game.iteration == 1,
                np.array_equal(game.matrix, final_matrix),
            ]
        )


def test_random_game():
    game = pconway.core.custom_game.RandomGame(nrow=4, ncol=4, seed=123)
    assert np.array_equal(game.matrix, random_matrix)
