def containsDuplicate(nums):
    d = {}

    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            return True

    return False

print(containsDuplicate([1,2,3,4]))