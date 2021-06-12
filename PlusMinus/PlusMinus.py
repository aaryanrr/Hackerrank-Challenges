#!/usr/bin/python3

import math
import os
import random
import re
import sys


def plus_minus(arr: list) -> None:
    negative = 0
    positive = 0
    zero = 0
    for x in arr:
        if x < 0:
            negative += 1
        elif x == 0:
            zero += 1
        else:
            positive += 1
    print(round(positive / len(arr), 6))
    print(round(negative / len(arr), 6))
    print(round(zero / len(arr), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
