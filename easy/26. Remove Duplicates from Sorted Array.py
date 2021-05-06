def removeDuplicates(nums):
    prev_idx = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[prev_idx]:
            nums[prev_idx + 1] = nums[i]
            prev_idx += 1
    
    return prev_idx + 1

print(removeDuplicates([1,1,2]))

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]