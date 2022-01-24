# Student Name: Meet Bharodiya
# Student ID:  20CE006

k=input()
# Take input as string and convert it into list
str=input()

# To store only unique element convert list into set
lst=set(list(str.split(' ')))

#Remove max element from set
lst.remove(max(lst))

#Print max element of set
print(max(lst))



