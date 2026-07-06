# Error Handling  (Day 14-15)

## Overview

Handling runtime errors gracefully with try/except/else/finally, raising exceptions, custom exception classes, and the exception hierarchy.

## Key Concepts

- try / except / else / finally block structure and execution order
- Catching specific exceptions vs bare except (why bare except is discouraged)
- Raising exceptions with `raise`, re-raising, and `raise ... from ...`
- Custom exception classes (subclassing Exception)
- Built-in exception hierarchy (ValueError, TypeError, KeyError, IndexError, etc.)
- Context managers and exceptions (how `with` handles cleanup on error)
- assert statements for debugging/invariants (not for validation)

## Gotchas

- Bare `except:` catches everything including KeyboardInterrupt/SystemExit
- Swallowing exceptions silently (empty except block) hides bugs
- finally always runs, even after return in try — order-of-execution surprises

## Search Keywords

Use these to look things up when you need more depth:

- `python try except finally explained`
- `python custom exception class`
- `python exception hierarchy`
- `python raise from chaining exceptions`
- `python assert statement usage`

## References

**Official Docs**
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

**YouTube (search these titles)**
- "python exception handling tutorial"
- "python custom exceptions explained"
- "python try except finally deep dive"

**Books**
- Python Crash Course — Eric Matthes (ch. 11 style testing/errors)
- Fluent Python — Luciano Ramalho (ch. on control flow/exceptions)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
