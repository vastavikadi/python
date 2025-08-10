a = "Elephant" #strings are immutable in python and once defined and initialized cant be changed afterwards
print(a[1]) #this way we can access the characters in a string using the same concept of indexing as in arrays
# a[4]='g' # as you can see this will give an error because strings are immutable
print(a)

#indexing from the start ( left side ) starts with 0 and from the right side starts with -1

# how to slice a string
print(a[0:3]) # this will print the first three characters of the string (excluding the character at index 3)
print(a[3:]) # this will print the string from the fourth character to the end
print(a[:4]) # this will print the string from the beginning to the fourth character