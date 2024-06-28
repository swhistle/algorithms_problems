import math


def guessNumber(n, pick):
    steps = 0

    left = 1
    right = n
    middle = (left + right) // 2

    for i in range(1, math.ceil(math.log(n, 2)) + 1):
        steps += 1

        if middle == pick:
            print(steps)
            return steps

        elif middle < pick:
            left = middle + 1
            middle = (left + right) // 2

        elif middle > pick:
            right = middle - 1
            middle = (left + right) // 2

    print(-1)
    return -1


guessNumber(1000, 250)
guessNumber(1000, 999)
guessNumber(1000, 1000)
