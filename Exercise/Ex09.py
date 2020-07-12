def binaryPallindrome(num):
    # convert number into binary
    binary = bin(num)

    binary = binary[2:]

    return binary == binary[-1::-1]


# Driver program
if __name__ == "__main__":
    num = 9
    print
    binaryPallindrome(num)
