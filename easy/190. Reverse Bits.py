def reverseBits(n):
    return int('{0:032b}'.format(n)[::-1], 2)

print(reverseBits(0b00000010100101000001111010011100))
