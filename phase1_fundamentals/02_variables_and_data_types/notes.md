# Variables and Data Types

**Day range:** 3-4

## Concepts (in my own words)

### Variables
- A variable is just a name pointing to an object in memory. Python has no
  "declare a type" step — assignment (`x = 5`) creates the variable.
- Python is **dynamically typed**: the same name can point to an `int` now
  and a `str` later. The *value* has a type, not the variable.
- Multiple assignment: `a, b, c = 1, 2, 3` and `x = y = z = 0` both work.
- Naming rules: letters, digits, underscores; can't start with a digit;
  case-sensitive; can't use reserved words (`class`, `for`, `if`, etc.).
- Convention: `snake_case` for variables/functions, `UPPER_CASE` for
  constants (Python doesn't enforce constants, it's just convention).

### Core built-in data types
- `int` — whole numbers, arbitrary precision (no overflow like C).
- `float` — decimal numbers, stored as double-precision (64-bit) floats.
- `bool` — `True` / `False`, actually a subclass of `int` (`True == 1`).
- `str` — immutable sequence of Unicode characters.
- `NoneType` — the single value `None`, Python's "no value" / null.
- `complex` — rarely used day-to-day, but exists (`3 + 4j`).

### Type checking and conversion
- `type(x)` returns the exact type; `isinstance(x, int)` also checks
  subclasses (better for branching logic).
- Explicit conversion ("casting"): `int("5")`, `float("3.14")`, `str(42)`,
  `bool(0)`.
- Implicit conversion happens in mixed arithmetic: `int + float -> float`.
- `bool()` on other types: `0`, `0.0`, `""`, `[]`, `{}`, `None` are all
  "falsy". Everything else is "truthy".

### Mutability (foundational, comes up everywhere later)
- `int`, `float`, `bool`, `str`, `tuple` -> immutable.
- `list`, `dict`, `set` -> mutable (covered properly in Data Structures topic).
- Immutability matters because `a = b` on an immutable type just copies a
  reference to the same value; you can't accidentally mutate it through `a`.

## Gotchas / things that tripped me up
- Floating point isn't exact: `0.1 + 0.2 != 0.3` (it's
  `0.30000000000000004`). Compare floats with a tolerance (`math.isclose`),
  not `==`.
- `True + True == 2` because `bool` is a subtype of `int`. Useful for
  counting `True` values in a list with `sum()`, surprising otherwise.
- `id()` and `is` check identity, not equality. Small ints (-5 to 256) and
  short strings are cached by CPython, so `is` can *look* like it works for
  equality on small values — don't rely on that.
- `input()` always returns a `str`, even if the user types a number — cast
  it explicitly (`int(input())`).
- Integer division `//` floors toward negative infinity, not toward zero:
  `-7 // 2 == -4`, not `-3`.

## Useful docs / links
- https://docs.python.org/3/library/stdtypes.html
- https://docs.python.org/3/tutorial/introduction.html
- https://docs.python.org/3/library/functions.html#type
