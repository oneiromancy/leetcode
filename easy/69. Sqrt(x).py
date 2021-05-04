def mySqrt(x):
    lim = 0.25
    guess = x / 2

    while True:
        if x - lim <= guess ** 2 <= x + lim:
            return int(guess)

        guess = (guess + (x / guess)) / 2


print(mySqrt(2147395599))
