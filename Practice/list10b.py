total = 0
ele = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variale total
while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

# printing total value
print("Sum of all elements in given list: ", total) 