def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

        # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)
print
"Sorted character array is %s" % ("".join(ans))

