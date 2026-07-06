# Variables and Data Types  (Day 2)

## Overview

How Python names bind to objects, dynamic typing, the built-in scalar types (int, float, bool, str, NoneType), and type conversion rules.

## Key Concepts

- Variables are references/names bound to objects (not boxes holding values)
- Dynamic typing: a name can be rebound to a different type
- Built-in types: int, float, complex, bool, str, NoneType
- Type conversion / casting: int(), float(), str(), bool()
- Mutability vs immutability (preview — deep dive in data structures)
- id(), type(), and isinstance() for inspecting objects
- Truthy/falsy values in Python

## Gotchas

- 0, '', [], None, {} are all falsy
- int/float division: `/` always returns float, `//` is floor division
- Small int caching (-5 to 256) can make `is` comparisons misleading

## Search Keywords

Use these to look things up when you need more depth:

- `python dynamic typing explained`
- `python mutable vs immutable types`
- `python type() vs isinstance()`
- `python truthy falsy values`
- `python variable name binding`

## References

**Official Docs**
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)

**YouTube (search these titles)**
- "python variables and data types explained"
- "python mutable vs immutable objects"
- "python is vs == difference"

**Books**
- Python Crash Course — Eric Matthes (ch. 2)
- Fluent Python — Luciano Ramalho (ch. 1, object references)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
