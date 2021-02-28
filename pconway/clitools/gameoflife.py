import argparse


def parser():
    parser = argparse.ArgumentParser(description="Play Conway's game of life")
    parser.add_argument(
        "-c", "--color", type=str, help="Foreground color. Defaults 'white'.",
        choices=["black", "blue", "cyan", "green", "magenta", "red", "white",
                 "yellow"],
        default="white")
    parser.add_argument("-C", "--char", type=str,
        help="Character representing live cells. Defaults '.'.", default=".")
    parser.add_argument("-b", "--border",
        help="Border on the screen", action="store_true")
    parser.add_argument("-s", "--speed", type=int, help="Frame per second",
        default=10)
    parser.add_argument("-m", "--mutation-rate", type=float,
        help="Mutation rate.", default=0.)
    parser.add_argument("--seed", type=int,
        help="Random number generator seed", default=123)
    parser.add_argument("-d", "--duration", type=float,
        help="Duration (seconds). Negative means infinte. Defaults -1.",
        default=-1)
    return parser


def main(args=None):

    import pconway

    options = parser().parse_args(args)
    fg_color = options.color
    alive_char = options.char
    if len(alive_char) != 1:
        raise ValueError("Number of characters must be exactly 1.")
    borderless = not options.border
    fps = options.speed
    mutation_rate = options.mutation_rate
    seed = options.seed
    duration = options.duration
    kwargs={
        "mutation_rate": mutation_rate,
        "seed": seed,
    }
    pconway.play(
        fg_color=fg_color, alive_char=alive_char, borderless=borderless,
        fps=fps, duration=duration, kwargs=kwargs)
