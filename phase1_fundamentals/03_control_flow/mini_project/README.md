# Mini Project: Number Guessing Game

**Goal:** Practice combining while loops, if/elif/else, break, and
continue into one small interactive program.

**What it does:**
The program picks a random number in a range (e.g. 1-100) and the
player repeatedly guesses until they get it right. After each guess,
it tells the player "too high" or "too low", tracks the number of
attempts, and offers a "hint" every 3 wrong guesses. The player can
type "quit" at any point to exit early.

**Requirements:**
- Use a `while` loop that continues until the correct guess or "quit".
- Use `if/elif/else` to branch on too-high / too-low / correct / quit.
- Use `continue` to reject invalid (non-numeric) input without crashing
  or counting it as an attempt.
- Use `break` to exit cleanly on a correct guess or a quit command.
- Print a final summary (number of attempts, whether they won or quit).

**How to run:**
```
python game.py
```

**Stretch goals (optional):**
- Add a difficulty selector (easy/medium/hard) that changes the range
  and/or max number of attempts.
- Track and display a best-score (fewest attempts) across multiple
  rounds using a loop-else on an outer "play again?" loop.
