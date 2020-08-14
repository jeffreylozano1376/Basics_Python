
import sys
import re
import random
import os
import math

my_list = [37, 7, 22, 15, 49, 60]


def goodSegment(badNumbers, lower, upper):

    badNumbers.sort()
    print(f"sorted badNumbers: {badNumbers}")
    five_four = badNumbers[5] - badNumbers[4]
    four_three = badNumbers[4] - badNumbers[3]
    three_two = badNumbers[3] - badNumbers[2]
    two_one = badNumbers[2] - badNumbers[1]
    one_zero = badNumbers[1] - badNumbers[0]
    bad_difference = []
    a1 = bad_difference.append(five_four)
    a2 = bad_difference.append(four_three)
    a3 = bad_difference.append(three_two)
    a4 = bad_difference.append(two_one)
    a5 = bad_difference.append(one_zero)
    print(f"bad difference: {bad_difference}")

    difference_list = list(range(1, 60))
    length_bad_difference = len(bad_difference)
    length_difference_list = len(difference_list)
    sliced = difference_list[:length_bad_difference]
    print(sliced)



# print(count_list)
# max_sum = max(sum_list)
# print(max_sum)


# result = goodSegment(1, 60)
# print(result)


#!/bin/python3


#
# Complete the 'goodSegment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY badNumbers
#  2. INTEGER lower
#  3. INTEGER upper
#

# badNumbers = [37, 7, 22, 15, 49, 60]


# def goodSegment(badNumbers, lower, upper):
#     badNumbers.sort()
#     a = badNumbers[5] - badNumbers[4]
#     b = badNumbers[4] - badNumbers[3]
#     c = badNumbers[3] - badNumbers[2]
#     d = badNumbers[2] - badNumbers[1]
#     e = badNumbers[1] - badNumbers[0]
#     bad_sums = []
#     a1 = bad_sums.append(a)
#     a2 = bad_sums.append(b)
#     a3 = bad_sums.append(c)
#     a4 = bad_sums.append(d)
#     a5 = bad_sums.append(e)
#     sum_list = list(range(lower, upper))
#     count_list = count(sum_list)
#     print(count_list)
#     slice_list = count_list
#     max_sum = max(sum_list)
#     return max_sum
