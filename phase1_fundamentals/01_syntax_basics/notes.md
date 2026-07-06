# Syntax Basics

**Day range:** Day 1-2

## Concepts (in my own words)
- Python doesn't use `{ }` or `end` keywords to mark blocks — **indentation
  itself is the syntax**. A colon `:` starts a block (after `if`, `for`,
  `def`, `class`, etc.) and everything indented under it belongs to that
  block. Standard is 4 spaces, don't mix tabs and spaces.
- A statement normally ends at the newline — no semicolon needed. You *can*
  put a `;` to fit two statements on one line, but it's considered bad style
  outside of quick one-liners.
- Comments start with `#` and run to the end of the line. There's no
  built-in multi-line comment syntax — people often use a triple-quoted
  string as a "comment block," but that's technically just an unused string
  literal, not a real comment.
- `print()` is a function (not a statement like Python 2) — always needs
  parentheses. `print(a, b)` prints both separated by a space by default;
  `print(a, end="")` suppresses the trailing newline.
- Variable names: letters, digits, underscores, can't start with a digit,
  case-sensitive, can't be a reserved keyword (`import keyword;
  keyword.kwlist` shows the full list). Convention is `snake_case` for
  variables/functions, `PascalCase` for classes, `UPPER_SNAKE` for
  constants.
- Line continuation: a long line can be split with a trailing backslash
  `\`, but it's more common (and safer) to just wrap in parentheses,
  brackets, or braces — Python treats unclosed `()`, `[]`, `{}` as one
  logical line automatically.
- Running code: `python script.py` runs a file top to bottom. The
  interactive REPL (`python` with no args, or `ipython`) evaluates one
  expression at a time and echoes the result — good for quick checks, not
  for real programs.
- `.py` files can be scripts (run directly) or modules (imported by other
  files) — that duality is why the `if __name__ == "__main__":` guard
  exists (comes up more in the modules topic, but worth knowing it exists
  from day one).

## Gotchas / things that tripped me up
- Mixing tabs and spaces in the same block raises a `TabError` (or silently
  does the wrong thing in old Python 2 code) — set the editor to insert
  spaces only.
- Forgetting the colon `:` at the end of `if`, `for`, `def`, etc. is a very
  common `SyntaxError` for beginners.
- Inconsistent indentation *within the same block* (e.g. 4 spaces on one
  line, 5 on the next) raises `IndentationError`, even though both "look"
  indented.
- An empty block (e.g. stubbing out a function body to fill in later) needs
  the `pass` keyword — you can't leave a colon with nothing indented under
  it.

## Useful docs / links
- Python official tutorial, "An Informal Introduction to Python":
  https://docs.python.org/3/tutorial/introduction.html
- PEP 8 (style guide — naming, indentation conventions):
  https://peps.python.org/pep-0008/
- `python -m this` in a terminal — prints "The Zen of Python."
