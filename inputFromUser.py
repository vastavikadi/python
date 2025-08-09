# this is how we take inputs from the users in python
a = input('Enter your name: ')
print(a)

# This by default takes the input as a string and we can convert it to other types if needed.

b = input('Enter a number to add to another number: ')
c = input("Enter a number to add to the first number: ")

b = int(b) # if we had not converted into int then the string would have been concatenated and we would have got like 1+5 = 15
c = int (c)

print('The sum is: ', b+c)