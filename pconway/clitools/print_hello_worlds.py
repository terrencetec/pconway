import argparse


def parser():
    parser = argparse.ArgumentParser(description="Print hello worlds")
    parser.add_argument("-n", type=int, help="Print n number of times", required=True)
    return parser


def main(args=None):

    from mypythonlibrary.helloworld import helloworlds

    options = parser().parse_args(args)

    helloworlds(options.n)
