def productExceptSelf(nums):
    products = []
    nonzero_prod = 1
    zero_count = (0, None)
    size = len(nums)


    for i in range(size):
        if nums[i]:
            nonzero_prod *= nums[i]
        else:
            zero_count = (zero_count[0] + 1, i)

    for i in range(size):
        if zero_count[0] == 0:
            products.append(int(nonzero_prod / nums[i]))
        elif zero_count[0] == 1 and i != zero_count[1]:
            products.append(0)
        elif zero_count[0] == 1 and nums[i] == 0:
            products.append(int(nonzero_prod))
        else:
            return [0] * size

    return products

print(productExceptSelf([1,2,3,4]))
        
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3,4]
# products: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# products: [0,0,9,0,0]

 

# Constraints:

#     2 <= nums.length <= 105
#     -30 <= nums[i] <= 30
#     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

# Follow up:

#     Could you solve it in O(n) time complexity and without using division?
#     Could you solve it with O(1) constant space complexity? (The products array does not count as extra space for space complexity analysis.)

