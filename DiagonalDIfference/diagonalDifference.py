#!/usr/bin/python3

import os


def diagonalDifference(arr: list) -> int:
    left_to_right = 0
    right_to_left = 0
    opp = -1
    for x in range(len(arr)):
        left_to_right += arr[x][x]
        right_to_left += arr[x][x + opp]
        opp -= 2

    return abs(left_to_right - right_to_left)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
