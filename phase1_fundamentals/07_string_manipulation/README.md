# String Manipulation  (Day 10-11)

## Overview

Strings as immutable sequences: slicing, common string methods, formatting (f-strings, .format, %), and intro to regular expressions.

## Key Concepts

- Strings are immutable sequences of Unicode characters
- Common methods: split, join, strip, replace, find, upper/lower, startswith/endswith
- String formatting: f-strings (preferred), str.format(), % formatting (legacy)
- String slicing and indexing (including negative indices)
- Multiline strings and raw strings (r'...')
- Intro to regular expressions with the `re` module (search, match, findall, sub)

## Gotchas

- Strings are immutable — methods return new strings, don't modify in place
- `+` concatenation in a loop is inefficient — prefer ''.join(list)
- Regex special characters need escaping; raw strings avoid escape confusion

## Search Keywords

Use these to look things up when you need more depth:

- `python string methods cheatsheet`
- `python f-strings formatting guide`
- `python re module regex tutorial`
- `python join vs concatenation performance`
- `python raw strings`

## References

**Official Docs**
- [Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [re — Regular expression operations](https://docs.python.org/3/library/re.html)

**YouTube (search these titles)**
- "python string methods tutorial"
- "python regex tutorial for beginners"
- "python f-strings deep dive"

**Books**
- Automate the Boring Stuff (ch. 6-7, strings & regex)
- Python Crash Course — Eric Matthes (ch. 2)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
