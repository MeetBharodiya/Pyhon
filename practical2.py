# Dictionary

# a. Write a Python script to check whether a given key already exists in a dictionary.

# dic1={"First_name":"Meet","Last_Name":"Bharodiya","Brach":"CE"}

# to take input from user
# key=input("Enter the key you want to check: ")

# to check given keys exit in dict or not
# if key in dic1.keys():
#     print("Key is present")
# else:
#     print("key is not present")

# b. Write a Python script to merge two Python dictionaries.

# thisdict1={"First_name":"Meet","Last_Name":"Bharodiya","Brach":"CE"}
# thisdict2={"brand": "Ford","model": "Mustang","year": 1964}

# to merge two dictionaries
# thisdict2.update(thisdict1)
# print(thisdict2)

# c. Write a Python program to sum all the items in a dictionary.

# dic1={'a':15,'b':30,'c':60}

# to do sum we need to crete list of values which are available in dic.
# list=[];
# for i in dic1:

#     # take each values of dictonary in list
#     list.append(dic1[i]);

# sum function is used to do sum of all element of list
# print(sum(list))

# d.  Write a Python script to add a key to a dictionary.

# dic2={0: 10, 1: 20}
# print(dic2)
# dic2.update({3:30})
# print(dic2)

# e.  Write a Python script to concatenate following dictionaries to create a new one.

# dic3={1:10, 2:20}
# dic4={3:30, 4:40}
# dic5={5:50,6:60}
# dic4.update(dic5)
# dic3.update(dic4)
# print(dic3)


# Tuple

# a. Write a Python program to create a tuple with different data types.

# thistuple = ("apple", 56.4563, 4567,False)
# print(thistuple)

# b. Write a Python program to create a tuple with numbers and print one item.

# thistuple1=(10,20,30,40)
# print(thistuple1[0])
# print(thistuple1[3])

# c. Write a Python program to add an item in a tuple

# thistuple1=(10,20,30,40)
# print(thistuple1)
# L=list(thistuple1)
# L.append(50)
# thistuple1=tuple(L)
# print(thistuple1)

# d. Write a Python program to convert a tuple to a string

# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# str =  ''.join(tup)
# print(str)

# e. Write a Python program to find the length of a tuple.

# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# print(len(tup))

# Set

# a. Write a Python program to add member(s) in a set and clear a set

# set1={'meet','harmi','sharad','Jay'}
# print(set1)
# set1.add('Hinal')
# print(set1)

# b. Write a Python program to remove an item from a set if it is present in the set

# set2={'aniket','jay','jeel','chintan','bhavdeep'}
# print(set2)
# name=input("Enter the name you want to remove: ")
# if name in set2:
#     set2.remove(name)      
# print(set2) 

# c. Write a Python program to create an intersection, Union, difference of sets

# sets are define
# A = {0, 2, 4, 6, 8};
# B = {1, 2, 3, 4, 5};
  
# # union
# print("Union :", A | B)
  
# # intersection
# print("Intersection :", A & B)
  
# # difference
# print("Difference :", A - B)

# d. Write a Python program to find maximum and the minimum value in a set.

# setn = {56,33,65,34,89,45,32,80}
# print("Original set elements:")
# print(setn)
# print("Maximum value of the said set:")
# print(max(setn))
# print("Minimum value of the said set:")
# print(min(setn))

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# List = [2, 1, 2, 2, 1, 3]
# counter = 0
# num = List[0]
# for i in List:
#     curr_frequency = List.count(i)
#     if(curr_frequency> counter):
#         counter = curr_frequency
#         num = i
# print("Number which is repeted most: ")
# print(num)
# print("Frequency of most repeted number is: ")
# print(counter)

# tuple=(1,2,4,5,6,6,3,6,8,3,6)
# L=list(tuple)
# counter1 = 0
# num1 = L[0]
# for i in L:
#     curr_frequency = L.count(i)
#     if(curr_frequency> counter1):
#         counter1 = curr_frequency
#         num1 = i
# print("Number which is repeted most: ")
# print(num1)
# print("Frequency of most repeted number is: ")
# print(counter1)

# items = ['Pen', 'Scissor', 'Pen', 'Pen', 'Scissor']

# count = {}
# for item in items:
#     count[item] = count.get(item, 0) + 1
