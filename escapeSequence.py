# | Escape | Meaning                               | Example             | Output                       |
# | ------ | ------------------------------------- | ------------------- | ---------------------------- |
# | `\'`   | Single quote                          | `'I\'m fine'`       | `I'm fine`                   |
# | `\"`   | Double quote                          | `"She said \"Hi\""` | `She said "Hi"`              |
# | `\\`   | Backslash                             | `"C:\\Users\\Name"` | `C:\Users\Name`              |
# | `\n`   | Newline (line break)                  | `"Hello\nWorld"`    | `Hello <br> World`           |
# | `\t`   | Horizontal tab                        | `"Hello\tWorld"`    | `Hello    World`             |
# | `\r`   | Carriage return (moves to line start) | `"Hello\rWorld"`    | `World`                      |
# | `\b`   | Backspace (removes prev char)         | `"Helloo\b"`        | `Hello`                      |
# | `\f`   | Form feed (new page, rare)            | `"Hello\fWorld"`    | `Hello (page break) World`   |
# | `\v`   | Vertical tab                          | `"Hello\vWorld"`    | `Hello (vertical gap) World` |


# Escape sequences in Python are special character combinations that start with a backslash (\) and represent things you can’t type directly or that have special meaning.

print("Hello\vWorld")
print("Hello\fWorld")
print("Hello\rWorld") # removed hello from the output
print("Hello\bWorld")


# escape sequence characters: \n , \t 
# using this we can print double quotes too
print("Hey it's a \"boy\"")

