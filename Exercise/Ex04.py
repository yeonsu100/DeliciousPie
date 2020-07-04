def remove(string, i):
    a = string[: i]
    b = string[i + 1:]

    return a + b


if __name__ == '__main__':
    string = "frozen"

    # Remove nth index element
    i = 5

    # Print the new string
    print(remove(string, i))

