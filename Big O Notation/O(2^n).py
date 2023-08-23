# O(2^n) is a reflection of O(log n). O(3^n), O(4^n), etc. are also possible but not generally used.

# Recursion, tree height n, two branches
def recursion(i, nums):
    if i == len(nums):
        return 0
    branch1 = recursion(i + 1, nums)
    branch2 = recursion(i + 2, nums)