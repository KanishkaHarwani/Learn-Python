# Mini Project: Unit Converter (CLI)

**Goal:** Practice variables, type conversion, and truthy/falsy checks in a
small, actually-useful script.

**What it does:**
A command-line tool that converts between common units, exercising the
core data types from this topic:
- Temperature: Celsius <-> Fahrenheit (float math)
- Distance: kilometers <-> miles (float math)
- Currency-style rounding: display results rounded to 2 decimal places
- Input validation: reject non-numeric input gracefully (str -> float
  conversion with error handling)

**How to run:**
```
python converter.py
```
Follow the prompts. Type `quit` at any point to exit.

**Stretch goals (optional):**
- Add weight conversion (kg <-> lbs).
- Keep a running history of conversions in a list and print it on exit.
- Use `bool` flags to let the user pick "verbose mode" (prints intermediate
  values) vs "quiet mode" (just the answer).
