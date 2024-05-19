import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', type=int, default=0,
        help='The maximum number of primes to generate.'
    )
    parser.add_argument(
        '--base', type=str, default='10',
        help='Base in which the results will be shown.'
    )
    parser.add_argument(
        '--bits', type=lambda value: int(value, base=2), default='000000000',
        help='Which bits are must be flagged in the number.'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    print(args)