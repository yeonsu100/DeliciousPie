def Cloning(li1):
    li_copy = []
    for item in li1: li_copy.append(item)
    return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)