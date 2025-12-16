# https://www.youtube.com/watch?v=m7hI2LulMxE&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=5
from math import factorial


def birthday_problem(n):
    # return factorial(365) / (factorial(365 - n) * (365**n))
    p = 1
    for i in range(1, n + 1):
        p *= (365 - i + 1) / 365
    return p


def search_half():
    n = 2
    while (p := birthday_problem(n)) >= 0.5:
        n += 1
    print("n = " + str(n))
    print("p = " + str(p))


search_half()
