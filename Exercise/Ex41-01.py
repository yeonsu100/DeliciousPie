# using list comprehension

# initializing list
test_list = [(1, 2), (3, 4), (5, 6)]

# printing original list
print("The original list of tuples : " + str(test_list))

# using list comprehension
# convert list of tuples to list of list
res = [list(ele) for ele in test_list]

# print result
print("The converted list of list : " + str(res))
