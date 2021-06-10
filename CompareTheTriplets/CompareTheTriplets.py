import os


def compareTriplets(a: list, b: list) -> list:
    # Write your code here
    bob_pts = 0
    alice_pts = 0
    for x in range(len(a)):
        if a[x] > b[x]:
            alice_pts += 1
        elif a[x] < b[x]:
            bob_pts += 1
        else:
            pass

    return [alice_pts, bob_pts]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
