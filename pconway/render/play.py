"""Plays the Conway's game of life.
"""
import curses
import time


def play(game_type="random", fps=10, alive_char=".", dead_char=" ",
         fg_color="white", bg_color="black", borderless=True,
         duration=-1, kwargs={}):
    """Plays the game of life.

    Parameters
    ----------
    game_type: str
        "random", ... or ...
    fps: int
        Frame per second.
    alive_char: str, optional
        The character representing a live cell.
        Defaults to "o"
    dead_char: str, optional
        The character representing a dead cell.
        Defaults to " "
    fg_color: str, optional
        Foreground color.
        One of "black", "blue", "cyan", "green", "magenta", "red", "white",
        "yellow".
        Defaults to "white".
    bg_color: str, optional
        Background color.
        One of "black", "blue", "cyan", "green", "magenta", "red", "white",
        "yellow".
        Defaults to "black".
    borderless: bool, optional
        Borderless.
        Defaults to True.
    duration: float, optional
        Duration of the game in seconds. Negative means play indefinitely.
        Defaults to -1.
    **kwargs: dict
        Keyword arguments passed to the pconway.core.game.Game class.

    Returns
    -------
    Boolean
        Returns True when finished.
    """
    if game_type == "random":
        import pconway.core.custom_game
        def curse_main(stdscr):
            curses.noecho()
            curses.curs_set(0)
            curses.start_color()
            if fg_color == "black":
                fg = curses.COLOR_BLACK
            elif fg_color == "blue":
                fg = curses.COLOR_BLUE
            elif fg_color == "cyan":
                fg = curses.COLOR_CYAN
            elif fg_color == "green":
                fg = curses.COLOR_GREEN
            elif fg_color == "magenta":
                fg = curses.COLOR_MAGENTA
            elif fg_color == "red":
                fg = curses.COLOR_RED
            elif fg_color == "white":
                fg = curses.COLOR_WHITE
            elif fg_color == "yellow":
                fg = curses.COLOR_YELLOW
            else:
                raise ValueError("Color {} not avaiable".format(fg_color))

            if bg_color == "black":
                bg = curses.COLOR_BLACK
            elif bg_color == "blue":
                bg = curses.COLOR_BLUE
            elif bg_color == "cyan":
                bg = curses.COLOR_CYAN
            elif bg_color == "green":
                bg = curses.COLOR_GREEN
            elif bg_color == "magenta":
                bg = curses.COLOR_MAGENTA
            elif bg_color == "red":
                bg = curses.COLOR_RED
            elif bg_color == "white":
                bg = curses.COLOR_WHITE
            elif bg_color == "yellow":
                bg = curses.COLOR_YELLOW
            else:
                raise ValueError("Color {} not avaiable".format(bg_color))
            curses.init_pair(1, fg, bg)
            stdscr.bkgd(" ", curses.color_pair(1))

            nrow, ncol = stdscr.getmaxyx()
            # compensate for border or simply for robustness.
            nrow -= 2
            ncol -= 2

            if not borderless:
                stdscr.border()

            game = pconway.core.custom_game.RandomGame(
                nrow=nrow, ncol=ncol, **kwargs)

            start_t = time.time()
            try:
                while 1:
                    t = time.time()
                    for i in range(len(game.matrix)):
                        for j in range(len(game.matrix[i])):
                            if game.matrix[i][j] > 0:
                                stdscr.addch(i+1, j+1, alive_char)
                            else:
                                stdscr.addch(i+1, j+1, dead_char)
                    stdscr.refresh()
                    game.evolve()
                    elapsed = time.time() - t
                    if elapsed < 1/fps:
                        time.sleep(1/fps - elapsed)
                    if duration > 0 and time.time() - start_t > duration:
                        break
            except KeyboardInterrupt:
                pass
    else:
        raise ValueError("game_type must be one of the followings"
                         "['random']")
    curses.wrapper(curse_main)
    return True
