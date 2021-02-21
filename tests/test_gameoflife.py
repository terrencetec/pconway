""" Test the game of life algs.
"""
import numpy as np

import pconway.core.gameoflife


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


def test_compute_next_state():
    test_matrix = pconway.core.gameoflife.compute_next_state(initial_matrix)
    assert np.array_equal(test_matrix, final_matrix)
