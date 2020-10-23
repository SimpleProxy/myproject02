#!/bin/python3

def iterative_factorial(n):
    v = 1

    for i in range(1, n + 1):
        v *= i

    return v

if __name__ == "__main__":
    pass

