import argparse
import numpy as np
from src import PrimeNumberGenerator


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
        '--bits', type=str, default=None,
        help='Which bits are must be flagged in the number.'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    generator = PrimeNumberGenerator(
        bit_mask=args.bits
    )
    base = int(args.base) if args.base.isnumeric() else 'bytes'
    for step, number in enumerate(generator, start=1):
        if base != 'bytes':
            print('Number: ', np.base_repr(number, base))
        else:
            print('Number: ', number.to_bytes(2, byteorder='big'))
        if step >= args.n:
            break
    print('Generation has been ended!')