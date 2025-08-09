# Module is a file containing codes written by someone else
# It can define functions, classes, and variables that can be reused in other Python programs, and can be installed using pip, can be imported using the import statement.

import pyjokes

joke = pyjokes.get_joke()
print(joke)

# There are two types of modules:
# Built-in and External modules
# Built-in modules are part of the Python standard library, such as math, sys, and os.
# External modules are third-party modules that can be installed using pip, such as requests, numpy, and pandas.

# REPL stands for Read-Eval-Print Loop, which is an interactive programming environment that allows you to enter Python code and see the results immediately. It is useful for testing small pieces of code and debugging. (simpply type python in the terminal and start calculating)


# Using triple single quotes or triple double quotes allows you to create multi-line strings in Python. This is useful for writing long texts, docstrings, or comments that span multiple lines.

print('''This is a multi-line string.
It spans multiple lines.
''')

