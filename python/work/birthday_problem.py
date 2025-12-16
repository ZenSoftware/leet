# https://www.youtube.com/watch?v=m7hI2LulMxE&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=5

import argparse


def birthday_problem(n):
    p = 1
    for i in range(1, n + 1):
        p *= (365 - i + 1) / 365
    return p


def find_half():
    n = 2
    while (p := birthday_problem(n)) >= 0.5:
        n += 1
    return n, p


def main():
    parser = argparse.ArgumentParser(description="Birthday problem utility")
    parser.add_argument(
        "n", nargs="?", type=int, help="number of people to compute probability for"
    )
    parser.add_argument(
        "--find-half",
        "-f",
        action="store_true",
        help="find smallest n where probability < 0.5",
    )
    args = parser.parse_args()

    if args.find_half:
        n, p = find_half()
        print(f"p({n}) = {p}")
    elif args.n is not None:
        p = birthday_problem(args.n)
        print(f"p({args.n}) = {p}")
    else:
        n, p = find_half()
        print(f"p({n}) = {p}")


if __name__ == "__main__":
    main()
