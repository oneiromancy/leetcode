def maximumWealth(accounts):
    return max([sum(account) for account in accounts])

print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10

# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

    