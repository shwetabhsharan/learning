"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

def two_sum(data, target):
    """
    """

    for i in range(0, len(data)-1):
        for j in range(0, len(data)-1):
            if data[i] + data[j+1] == target:
                return i, j+1
            else:
                j = j + 1

# print two_sum([2, 7, 11, 15], 9)
# print two_sum([2, 7, 11, 15], 18)
# print two_sum([2, 7, 11, 15], 26)
# print two_sum([2, 5, 5, 11], 10)

def two_sum1(data, target):
    """
    """
    data_dict = {}
    for i in range(0, len(data)):
        data_dict[i] = data[i]
    for k, v in data_dict.items():

        if i > len(data)-1:
            return -1
        elif target == data_dict[i] + data_dict[i+1]:
            print i, i+1
            return
        else:
            i = i+1
two_sum1([2, 7, 11, 15], 26)
