# Functions  (Day 5-6)

## Overview

Defining reusable code with def, parameters (positional, keyword, default, *args/**kwargs), return values, scope (LEGB), and lambda expressions.

## Key Concepts

- def syntax, parameters vs arguments, return vs implicit None
- Default arguments, keyword arguments, positional-only/keyword-only params
- *args and **kwargs for variable-length arguments
- Scope: Local, Enclosing, Global, Built-in (LEGB rule); global/nonlocal keywords
- Lambda functions (anonymous, single-expression functions)
- Docstrings for functions (PEP 257) and type hints basics
- First-class functions: passing functions as arguments (map/filter preview)

## Gotchas

- Mutable default arguments (e.g. def f(x=[])) persist across calls — classic bug
- Shadowing built-in names as parameter names (list, str, id)
- Forgetting return means the function returns None silently

## Search Keywords

Use these to look things up when you need more depth:

- `python args kwargs explained`
- `python LEGB scope rule`
- `python mutable default argument bug`
- `python lambda functions`
- `python type hints function annotations`

## References

**Official Docs**
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 257 Docstrings](https://peps.python.org/pep-0257/)

**YouTube (search these titles)**
- "python functions explained"
- "python args and kwargs tutorial"
- "python scope LEGB rule explained"

**Books**
- Python Crash Course — Eric Matthes (ch. 8)
- Fluent Python — Luciano Ramalho (ch. 7, first-class functions)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
