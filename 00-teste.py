# Importing the required libraries




# print (not None != "")

"""myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myList = list(set(myList))

print(myList)"""



items=[x for x in input().split(',')]
items.sort()


print(','.join(items))