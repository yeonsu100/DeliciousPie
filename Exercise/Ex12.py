def countOddSquares(n, m):
    return int(m ** 0.5) - int((n - 1) ** 0.5)


# Driver code
n = 5
m = 100
print("Count is", countOddSquares(n, m))

