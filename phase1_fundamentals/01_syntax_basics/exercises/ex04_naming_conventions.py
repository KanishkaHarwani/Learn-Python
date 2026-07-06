# ex04_naming_conventions.py
#
# Concept: valid identifiers + PEP 8 naming conventions
# (snake_case for variables/functions, PascalCase for classes,
# UPPER_SNAKE for constants).

import keyword

print("Python reserved keywords:")
print(keyword.kwlist)

# TODO:
# 1. Below, try assigning to a couple of INVALID identifiers by
#    uncommenting them one at a time and running the file. Read the
#    SyntaxError Python gives you for each, then re-comment them out.

# 2for = "starts with a digit"      # invalid: can't start with a digit
# my-variable = "has a hyphen"      # invalid: hyphen is the minus operator
# class = "reserved keyword"        # invalid: 'class' is a keyword

# 2. Fix each invalid example above by rewriting it as a valid,
#    PEP-8-style snake_case name below.
student_count = 5
my_variable = "has a hyphen, fixed"
class_name = "reserved keyword, fixed"

# 3. Declare one constant using UPPER_SNAKE convention.
MAX_ATTEMPTS = 3

print(student_count, my_variable, class_name, MAX_ATTEMPTS)
