def kidsWithCandies(candies, extraCandies):
    return [True if person + extraCandies >= max(candies) else False for person in candies]

print(kidsWithCandies([4,2,1,1,2], 1))
