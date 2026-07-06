# Mini Project: Syntax Basics — ASCII Receipt Printer

**Goal:** Practice indentation, comments, `print()` formatting, and
variable naming together in one small script — nothing fancy, this
topic is light so the mini project stays light too.

**What it does:** Prints a fake shop receipt to the console using only
what's been covered so far (variables, `print()` with `sep`/`end`,
comments, basic naming conventions). No functions, loops, or data
structures yet — those come in later topics, so keep it to a straight
top-to-bottom script.

**How to run:**
```
python receipt.py
```

**Suggested structure (fill in `receipt.py`):**
- Define a few variables: `STORE_NAME` (constant-style), `item_1_name`,
  `item_1_price`, `item_2_name`, `item_2_price`, `tax_rate`.
- Compute `subtotal`, `tax`, and `total` using simple arithmetic.
- Use `print()` calls (with `sep="\n"`, `end=""`, dashes for a divider
  line, etc.) to format something like:

```
======================
   THE CORNER STORE
======================
Coffee ............ 3.50
Muffin ............ 2.25
----------------------
Subtotal .......... 5.75
Tax ............... 0.46
Total ............. 6.21
======================
```

No need for perfect column alignment yet (that's easier once you've
covered string formatting) — just get comfortable stringing together
variables, comments, and `print()` calls correctly.
