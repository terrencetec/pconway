"""A Library for printing hello worlds.
"""


def helloworld():
    """Printing a single hello world.
    """
    print('Hello World!')


def helloworlds(n):
    """Printing many hello worlds and return the string hello world

    Parameters
    ----------
    n: int
        The number of times that hellow world will be printed

    Returns
    -------
    string
        The string 'Hello World!'.
    """
    for _ in range(n):
        helloworld()
    return('Hello World!')
