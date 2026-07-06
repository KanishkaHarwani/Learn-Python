# ex03_print_basics.py
#
# Concept: print() is a function, and it takes useful keyword args:
# sep, end, and multiple positional args.

print("Hello", "World")                  # default sep=" "
print("Hello", "World", sep="-")         # custom separator
print("No newline after this...", end="")
print(" <- continues on the same line")

# TODO:
# 1. Use print() with sep="" and 3+ arguments to build a single
#    concatenated line of output.
# 2. Use end="\n\n" to print a line followed by a blank line.
# 3. Print the same sentence two ways: once using a comma-separated
#    print(), once using an f-string (f"...") passed as a single
#    argument. (f-strings are covered more in string manipulation —
#    just get a first look here.)

name = "Ada"
age = 30

print("Name:", name, "Age:", age)
print(f"Name: {name} Age: {age}")
