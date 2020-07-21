# initialize list
test_list = ['gfg', 'is', 'good']

# printing original list
print("The original list : " + str(test_list))

# Reverse Order Sort in String List? + reverse
# using map() + sorted() + join() + lambda
res = list(map(lambda ele: "".join(sorted(ele, reverse=True)), test_list))

# printing result
print("List after string reverse sorting : " + str(res))

