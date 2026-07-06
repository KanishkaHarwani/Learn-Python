# Phase 1 - Topic 3 - Control Flow Exercises

## Exercise 01: if / elif / else basics
Task:
Write a function `classify_number(n)` that returns:
- "negative"  if n < 0
- "zero"      if n == 0
- "small"     if 0 < n <= 10
- "large"     if n > 10

Then, below the function, call it with a few different values and
print the results to check your work.


## Exercise 02: Nested conditionals

Task:
Write a function `grade_and_honors(score)` that takes a numeric score
(0-100) and returns a tuple (letter_grade, honors) where:
- letter_grade: "A" (90+), "B" (80-89), "C" (70-79), "D" (60-69), "F" (<60)
- honors: True only if letter_grade is "A" AND score >= 95, else False

This forces you to nest an inner condition inside an outer one instead
of just chaining elif/elif/elif.


## Exercise 03: for loops

Task:
1. Write a function `sum_of_multiples(limit, of=(3, 5))` that returns
   the sum of all numbers below `limit` that are multiples of any
   number in `of`. (Classic "Project Euler #1" style problem.)

2. Write a function `first_n_squares(n)` that returns a list of the
   first n square numbers (1, 4, 9, 16, ...) using a for loop and
   range() -- no list comprehension yet, that's a later topic.


## Exercise 04: while loops

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


## Exercise 05: break, continue, and loop-else

Task:
1. Write a function `first_prime_after(n)` that searches upward from
   n+1 and returns the first prime number found. Use `break` once
   you've found it -- no need to keep checking further numbers.

2. Write a function `sum_ignoring_negatives(numbers)` that sums a list
   of numbers but skips (via `continue`) any negative values.

3. Write a function `contains_duplicate(items)` that uses a for/else
   loop: loop through pairs of indices checking for a duplicate value,
   `break` as soon as one is found, and use the loop's `else` clause to
   return False only if the loop completes without finding one.
   (There are simpler ways to check for duplicates in Python -- this
   exercise is specifically about practicing for/else.)


## Exercise 06: match / case (structural pattern matching, Python 3.10+)

Task:
Write a function `describe_command(command)` that takes a tuple
representing a simple text-adventure command and returns a description
string, using match/case to branch on structure:

- ("go", direction)         -> f"Moving {direction}"
- ("take", item)            -> f"Picking up {item}"
- ("look",)                 -> "Looking around the room"
- ("quit",)                 -> "Exiting the game"
- anything else             -> "I don't understand that command"

This is a good exercise for matching on tuple *shape*, not just value
equality -- something a plain if/elif chain makes more awkward.


