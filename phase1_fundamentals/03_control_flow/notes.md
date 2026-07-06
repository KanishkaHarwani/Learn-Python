# Control Flow

**Day range:** 5-6

## Concepts (in my own words)
- **if / elif / else** — branch execution based on a condition. Python
  doesn't have a switch statement (older versions) — a chain of `elif`
  does the same job.
- **Truthiness** — Python evaluates non-boolean values as True/False in
  conditions: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, and `None` are all
  falsy; basically everything else is truthy.
- **for loops** — iterate over an *iterable* (list, string, range, dict,
  file, generator...), not a numeric counter like in C. `for i in
  range(n)` is the idiom when you actually need a counter.
- **while loops** — repeat while a condition holds. Good for "repeat
  until something happens" when you don't know the number of iterations
  up front (e.g. waiting for valid input, game loops).
- **break** — exits the nearest enclosing loop immediately.
- **continue** — skips to the next iteration of the nearest enclosing
  loop.
- **else on a loop** — a `for`/`while` loop can have an `else` clause
  that runs only if the loop completed *without* hitting `break`. Useful
  for "search and if not found" patterns.
- **match / case** (3.10+) — structural pattern matching, more powerful
  than a simple switch since it can match on structure/type, not just
  equality.

## Gotchas / things that tripped me up
- Off-by-one errors with `range(start, stop)` — `stop` is exclusive.
- Modifying a list while iterating over it with a `for` loop skips
  elements. Iterate over a copy (`for x in list[:]`) or build a new list
  instead.
- `break` only escapes the *innermost* loop — nested loops need a flag
  or a function-with-`return` to fully exit.
- Chained comparisons like `0 < x < 10` work in Python and read
  naturally, unlike most C-like languages.
- Assignment expressions (`:=`, the "walrus operator") let you assign
  inside a condition, e.g. `while (line := f.readline()):` — handy but
  easy to overuse.

## Useful docs / links
- https://docs.python.org/3/tutorial/controlflow.html
- https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
