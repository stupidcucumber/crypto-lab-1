import argparse
from src.utils import baillie_psw_test


def parse_arguments() -> argparse.Namespace: 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--number', type=int, required=True,
        help='Number you want to test'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    names: list[str] = ['not primary', 'almost certainly primary']
    print('Requested number: ', args.number)
    print('The primality of the number: ', names[int(baillie_psw_test(number=args.number))])