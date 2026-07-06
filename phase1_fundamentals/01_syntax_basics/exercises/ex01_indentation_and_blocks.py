# ex01_indentation_and_blocks.py
#
# Concept: Python uses indentation (not braces) to define blocks.
#
# TODO:
# 1. Write an if/else statement that checks whether a number is
#    positive, negative, or zero, and prints a message for each case.
# 2. Deliberately break the indentation (e.g. mismatch spaces) and run
#    the file to see the IndentationError Python raises. Then fix it.
# 3. Write an empty if-branch using `pass` to see how that works.

number = -5

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# Your pass-statement example:
if True:
    pass  # replace this with a comment explaining when pass is useful
