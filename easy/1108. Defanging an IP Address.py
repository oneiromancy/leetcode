def defangIPaddr(address):
    return ''.join(['[.]' if char == '.' else char for char in address])

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

print(defangIPaddr("1.1.1.1"))
