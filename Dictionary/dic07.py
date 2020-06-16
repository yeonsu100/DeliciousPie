from collections import Counter

def maxAnagramSize(input):
    # split input string separated by space
    input = input.split(" ")

    # sort each string in given list of strings
    for i in range(0, len(input)):
        input[i] = ''.join(sorted(input[i]))

    freqDict = Counter(input)

    # get maximum value of frequency
    print(max(freqDict.values()))


# Driver program
if __name__ == "__main__":
    input='Some things never change Like how I am holding on tight to you'
    maxAnagramSize(input)