"""
Day1

Part1

I am using numpy to vectorizing math operations on list of integers.

For the solution I take the input numbers and get their diff from 2020.
This I check if the diff result is located in input integers. If so, I get the
index for the two numbers I am looking for and finally multiply them together.
"""

import numpy as np

nums = []

lines = np.genfromtxt("../input/day1", dtype=int, delimiter="\n")
diff = 2020 - lines

for n in diff:
    a, = np.where(lines == n)
    if len(a) == 1:
        index = a[0]
        nums.append(lines[index])

if len(nums) != 2:
    print("Something went wrong: {ns}".format(ns=nums))
else:
    print("{}".format(nums))
    answer = nums[0] * nums[1]
    print("This is the way: {answer}".format(answer=answer))
