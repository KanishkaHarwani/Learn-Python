# ex02_comments.py
#
# Concept: single-line comments with `#`, and triple-quoted strings
# used as (unofficial) block comments / docstrings.

# This is a single-line comment explaining the next line.
x = 10  # inline comment: x starts at 10

"""
This is a triple-quoted string being used as a block comment.
It's not a real comment (Python still evaluates it as a string
literal), but it's a common convention for longer explanations.
It's ALSO exactly how docstrings work for modules/functions/classes
(more on that in the functions topic).
"""

# TODO:
# 1. Add a comment above each line below explaining what it does.
y = x * 2
z = y ** 2

print(x, y, z)
