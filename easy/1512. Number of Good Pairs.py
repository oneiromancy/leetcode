def numIdenticalPairs(nums):
    goodPairs = 0

    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if idx1 < idx2 and num1 == num2:
                goodPairs += 1

    return goodPairs

print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

# Input: nums = [1,2,3,1,1,3]
# Output: 4

# Input: nums = [1,1,1,1]
# Output: 6

# Input: nums = [1,2,3]
# Output: 0
