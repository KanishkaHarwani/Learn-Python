"""
Exercise 4: while loops

Task:
Write a function `collatz_steps(n)` that returns how many steps it
takes for the Collatz sequence starting at n to reach 1:
- if n is even: n = n // 2
- if n is odd:  n = 3 * n + 1
Repeat until n == 1, counting the number of steps taken.

Example: collatz_steps(6) -> 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
         that's 8 steps.

Use a while loop (you don't know the number of iterations ahead of
time, which is the classic signal to reach for `while` over `for`).
"""


def collatz_steps(n):
    # TODO: implement using a while loop
    pass


if __name__ == "__main__":
    # TODO: test with a few starting numbers, e.g. 1, 6, 27
    pass
