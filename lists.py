# arrays are called list in python
# collection of data of any type (slightly diff from arrays)

friends = ["hey", 32,34.43, False]
print(friends)
print(friends[3])
friends[0]="Aditya"
print(friends) # lists are mutabe unlike strings

print(friends[:])
print(friends[::2])




#list methods
friends.append("Yash") # add to the list at the end
print(friends)
# sort() #sorts the list of numbers
# reverse() # reverses the order
# insert(value, index) # inserts the value at the given index
# removes(values) # removes the value
# pop removes the last index
friends.reverse()
print(friends) #['Yash', False, 34.43, 32, 'Aditya'] anc changed the original list
friends.insert(3,5)
print(friends)

# friends.sort() wont run because has values except numbers as well
# print(friends)
print(friends.pop()) # removes and returns that removed element and it also takes the index as well