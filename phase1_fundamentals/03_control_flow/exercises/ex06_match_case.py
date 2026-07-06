"""
Exercise 6: match / case (structural pattern matching, Python 3.10+)

Task:
Write a function `describe_command(command)` that takes a tuple
representing a simple text-adventure command and returns a description
string, using match/case to branch on structure:

- ("go", direction)         -> f"Moving {direction}"
- ("take", item)            -> f"Picking up {item}"
- ("look",)                 -> "Looking around the room"
- ("quit",)                 -> "Exiting the game"
- anything else             -> "I don't understand that command"

This is a good exercise for matching on tuple *shape*, not just value
equality -- something a plain if/elif chain makes more awkward.
"""


def describe_command(command):
    # TODO: implement using match/case
    pass


if __name__ == "__main__":
    # TODO: test with a few different command tuples
    pass
