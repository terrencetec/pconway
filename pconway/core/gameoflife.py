"""The game of life algorithm.
"""
import numpy as np


def compute_next_state(matrix):
    """Returns the next state of a matrix according to the game of life algs.

    Parameters
    ----------
    matrix: array
        A matrix with entities 1 or 0 (live or dead)

    Returns
    -------
    next_matrix: array
        The evoluted state.

    Note
    ----
    Any live cell with fewer than two live neighbours dies.
    Any live cell with two or three live neighbours lives on to
    the next generation.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a
    live cell.
    """
    matrix = np.array(matrix)
    alive_matrix = get_alive_matrix(matrix)
    # For each cell, check the number of lives around itself and apply
    # the Conway's game of life rules.
    next_matrix = np.vectorize(compute_cell_next_state)(matrix, alive_matrix)
    return next_matrix


def compute_cell_next_state(current, neighbours):
    """Return the next state of the cell on position (i, j) in alive_matrix.
    Parameters
    ----------
    current: int
        The state of the cell, 1 or 0 (live or dead)
    neighbours: array
        The number of alive cells around the cell.

    Returns
    -------
    new_state: int
        The new state of the cell, 1 or 0 (live or dead)
    """
    new_state = 0
    if current > 0:
        if neighbours == 2 or neighbours == 3:
            new_state = 1
    elif neighbours == 3:
        new_state = 1
    return new_state


def get_alive_neighbours(matrix, i, j):
    """Returns the number of alive neighbours around the i,j cell.

    Parameters
    ----------
    matrix: array
        A matrix with entities 1 or 0 (live or dead)
    i: int
        Number of rows of the main cell of interest.
    j: int
        Number of column of the main cell of interest.

    Returns
    -------
    nalive: int
        The number of alive cells around cell of interest.
    """
    # Get slicers which capture a 3x3 matrix around the main cell
    if i-1 < 0:
        slice_i_min = 0
    else:
        slice_i_min = i-1

    if i+1 > len(matrix)-1:
        slice_i_max = len(matrix)-1+1
    else:
        slice_i_max = i+1+1
    if j-1 < 0:
        slice_j_min = 0
    else:
        slice_j_min = j-1

    if j+1 > len(matrix[i])-1:
        slice_j_max = len(matrix[i])-1+1
    else:
        slice_j_max = j+1+1
    sliced_matrix = matrix[slice_i_min:slice_i_max, slice_j_min:slice_j_max]

    # Count the number of entities that are non zero (alive)
    nalive = np.count_nonzero(sliced_matrix)
    # uncount our cell of interest:
    if matrix[i][j] > 0:
        nalive -= 1
    return nalive


def get_alive_matrix(matrix):
    """Returns a matrix with number of lives around each cell.

    Parameters
    ----------
    matrix: array
        A matrix with entities 1 or 0 (live or dead)

    Returns
    -------
    alive_matrix: array
        The number of alive cells around each cell.
    """
    alive_matrix = np.zeros_like(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            alive_matrix[i][j] = get_alive_neighbours(matrix, i, j)
    return alive_matrix


def mutation(matrix, mutation_rate):
    """Mutate the population

    Parameters
    ----------
    matrix: array
        A matrix with entities 1 or 0 (live or dead)
    mutation_rate: float
        A float from 0 to 1.
        The chance that a cell would flip.
        This applies after each evolution.

    Returns
    -------
    matrix: array
        The mutated matrix.
    """
    random_binomial = np.random.binomial(1, mutation_rate, np.shape(matrix))
    return np.bitwise_xor(matrix, random_binomial)
