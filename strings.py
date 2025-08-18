a = "Elephant" #strings are immutable in python and once defined and initialized cant be changed afterwards
print(a[1]) #this way we can access the characters in a string using the same concept of indexing as in arrays
# a[4]='g' # as you can see this will give an error because strings are immutable
print(a)

#indexing from the start ( left side ) starts with 0 and from the right side starts with -1

# how to slice a string
print(a[0:3]) # this will print the first three characters of the string (excluding the character at index 3)
print(a[3:]) # this will print the string from the fourth character to the end
print(a[:4]) # this will print the string from the beginning to the fourth character

# negative slicing done using the right side indexing
print(a[-1]) # this will print the last character of the string
print(a[-4:-1]) # this will print the string from the fourth last character to the second last character

print(a[-4:-1]) # excludes the character at index -1
print(a[1:4]) # this will print the string from the second character to the fourth character (excluding the character at index 4)
print(a[0:3]) # this will print the first three characters of the string (excluding the character at index 3)


# skip value in the string
print(a[::2]) # this will print every second character of the string
print(a[1::2]) # this will print every second character of the string starting from the second character
print(a[1:7:2]) # this will print every second character of the string starting from the second character to the seventh character (excluding the character at index 7)
print(a[0:7:2]) # this will print every second character of the string from the beginning to the seventh character (excluding the character at index 7)
print(a[0:8:2]) # this will print every second character of the string from the beginning to the last (including index 7) 


name = input("Enter your name: ")
print(f"This is name your name {name}") #kinda template literal in js


letter = '''Hey Name,
this is the Date'''

print(letter.replace("Name", "Adi").replace("Date", "26 Aug, 2005")) # chaining of the replace method
# strings are immutable and original remains the same

