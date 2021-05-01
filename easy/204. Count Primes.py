def countPrimes(n):
    if n > 2:
        eratosthenes_sieve= [True] * n
        eratosthenes_sieve[0] = eratosthenes_sieve[1] = False

        for i in range(2, n):
            if eratosthenes_sieve[i]:
                for j in range(i*i, n, i):
                    eratosthenes_sieve[j] = False

        return sum(eratosthenes_sieve)
    else:
        return 0

print(countPrimes(499979))


# Count the number of prime numbers less than a non-negative number, n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:

# Input: n = 0
# Output: 0

# Example 3:

# Input: n = 1
# Output: 0

 

# Constraints:

#     0 <= n <= 5 * 106

