# O(n^3) Are just like n^2 but with more elements. O(n^4), O(n^5), etc. are also possible but not generally used.

# Get every triplet of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print(nums[i], nums[j], nums[k])