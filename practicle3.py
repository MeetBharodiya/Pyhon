# Student Name: Meet Bharodiya
# Student ID:  20CE006

k=input()

# Take input as string and convert it into list
str=input()
lst=list(str.split(' '))

for i in lst:
    # count function will return frequncy of i in list
    curr_frequency=lst.count(i);
    if curr_frequency==1:
        captain_room=i;
print(captain_room);

