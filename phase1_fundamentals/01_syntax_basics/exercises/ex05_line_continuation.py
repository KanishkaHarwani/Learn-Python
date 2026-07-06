# ex05_line_continuation.py
#
# Concept: splitting long logical lines using implicit continuation
# (unclosed brackets) vs explicit continuation (backslash).

# Implicit continuation - preferred. Python treats an unclosed
# (), [], or {} as one logical line until it's closed.
total = (
    1
    + 2
    + 3
    + 4
)

my_list = [
    "apple",
    "banana",
    "cherry",
]

# Explicit continuation with backslash - works, but more fragile
# (no trailing whitespace allowed after the backslash) and less common.
total_backslash = 1 + \
    2 + \
    3

# TODO:
# 1. Rewrite the long line below using implicit continuation (wrap it
#    in parentheses and break it across multiple lines).
long_calculation = 10 * 20 + 30 * 40 - 50 * 60 + 70 * 80 - 90 * 100

# 2. Write a function CALL (not definition yet - that's the next topic)
#    to sum(my_list_of_numbers) but split the arguments across lines
#    using the list's own brackets.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

print(total, my_list, total_backslash, long_calculation)
