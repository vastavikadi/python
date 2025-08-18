a = "elephant"
print(len(a)) # gives the length of the string
print(a.startswith("a")) # returns true of false if string starts with the particular letter/substring
print(a.endswith("t"))
print(a.capitalize()) # capitalizes the first letter only
print(a.upper()) # sab uppercase me
print(a.count("e")) # counts a particular letter or substring (count of e in variable a)
print(a.find("p")) # (returns the index of 'p') and returns -1 if not present
print(a.replace("h", "j")) # replacing h with j in variable a and changes every occurence
print(a.replace(a[2], "l"))  ##lllphant replace works like this also; replaces every "e" in the string with "l".




# str.casefold() → Aggressive lowercase (for case-insensitive comparison).
# str.lower() → All lowercase.
# str.upper() → All uppercase.
# str.swapcase() → Swap upper ↔ lower.
# str.title() → Capitalize first word
# str.rfind(sub) → sub ke phle wale ka index
print(a.casefold()) # elephant
print(a.swapcase())# ELEPHANT
print(a.title()) # Elephant
print(a.rfind("ant"))

print("hey".title())


# str.strip([chars]) → Remove from both ends.
# str.lstrip([chars]) → Remove from left.
# str.rstrip([chars]) → Remove from right.