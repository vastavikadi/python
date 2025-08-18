# this too is a collection like a list but immutable like string

a = (1,) # (1) isko integer smjhega
print(type (a)) # <class 'tuple'>

b = (1,2,"Apple", "Banana", True)
print(b)

# methods on tuple
print("Methods of b:")
print(b.count(False)) # 0 because this is the number of times false came
print(b.index(2)) # returns the index of the element
print(max(b))
# len(tuple) → Returns number of elements 
# max(tuple) → Returns maximum value only for number tuple
# min(tuple) → Returns minimum value only for number tuple
# sum(tuple) → Returns sum (if elements are numbers) only for number tuple
# sorted(tuple) → Returns a sorted list of elements only for number tuple
# tuple(iterable) → Converts an iterable to a tuple only for number tuple


# concatenation of tuples
# t1 = (1, 2, 3)
# t2 = (4, 5)
# t3 = t1 + t2
# print(t3)  # (1, 2, 3, 4, 5)

# repetition of tuples
# t = (1, 2)
# print(t * 3)  # (1, 2, 1, 2, 1, 2)

# Unpacking
# Tuples can be unpacked into variables.
# t = (100, 200, 300)
# a, b, c = t
# print(a, b, c)  # 100 200 300

# t = (10, 20, 30)
# print(20 in t)      # True
# print(40 not in t)  # True

#IMPORTANT
# The built-in tuple() constructor is used to convert any iterable (like a list, string, set, dictionary, or generator) into a tuple.

# list to tuple
# my_list = [1, 2, 3, 4]
# t = tuple(my_list)
# print(t)   # (1, 2, 3, 4)

# From string → tuple
# s = "hello"
# t = tuple(s)
# print(t)   # ('h', 'e', 'l', 'l', 'o')