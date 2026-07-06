# Comprehensions and Generators  (Day 9)

## Overview

Pythonic, concise ways to build and iterate data: list/dict/set comprehensions and lazy generator expressions/functions using yield.

## Key Concepts

- List comprehensions: syntax, conditionals, nested comprehensions
- Dict comprehensions and set comprehensions
- Generator expressions (parentheses instead of brackets) — lazy evaluation
- Generator functions using `yield`; difference from `return`
- When to prefer a generator over a list (memory efficiency for large/infinite sequences)
- itertools module preview: chain, islice, count

## Gotchas

- Generators are exhausted after one iteration — can't reuse them
- Overly nested/complex comprehensions hurt readability — sometimes a loop is clearer
- A generator function's body doesn't run until you iterate it (lazy)

## Search Keywords

Use these to look things up when you need more depth:

- `python list comprehension vs generator expression`
- `python yield generators explained`
- `python dict comprehension examples`
- `python itertools tutorial`
- `python lazy evaluation generators`

## References

**Official Docs**
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Generators (HOWTO)](https://docs.python.org/3/howto/functional.html#generators)
- [itertools](https://docs.python.org/3/library/itertools.html)

**YouTube (search these titles)**
- "python list comprehensions explained"
- "python generators and yield explained"
- "python itertools tutorial"

**Books**
- Fluent Python — Luciano Ramalho (ch. 2, 17 - iterators/generators)
- Effective Python — Brett Slatkin (items on comprehensions/generators)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
