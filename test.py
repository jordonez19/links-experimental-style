nums = [1, 5, 2, 1, 4, 5, 1]
# dup = [x for i, x in enumerate(nums) if i != nums.index(x)]
# print(dup)  # [1, 5, 1]


def longestSubarray(nums):
    # Write your code here
    for i in enumerate(nums):
        if i != nums.index(x):
            print(i)
