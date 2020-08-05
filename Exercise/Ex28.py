def display():
    n = 5
    i = 1

    # Outer loop for how many lines we want to print
    while (i <= n):
        k = i
        j = 1

        # Inner loop for printing natural number
        while (j <= i):
            print(k, end=" ")

            # Logic to print natural value column-wise
            k = k + n - j
            j = j + 1

        print("\r")
        i = i + 1


# Driver code
display()
