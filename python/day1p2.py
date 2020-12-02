import numpy as np


def get_nums(lines):
    s = set()
    for i in lines:
        for j in lines:
            n = 2020 - i - j
            if n in lines:
                s.add(n)

    return np.array(list(s))


lines = np.genfromtxt("../input/day1", dtype=int, delimiter="\n")

nums = get_nums(lines)

print(nums)
print(nums.sum())
print(nums.prod())
