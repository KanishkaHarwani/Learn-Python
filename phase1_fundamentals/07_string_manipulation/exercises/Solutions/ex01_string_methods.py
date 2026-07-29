"""
Exercise 01 - String Manipulation

Practice:
1. split()
2. join()
3. replace()
4. find()
"""


def main():
    para_1 = """SPEAK, MEMORY— Odf the cunning hero,
The wanderer, blown off course time and again
After he plundered Troy’s sacred heights.

Speak
Odf all the cities he saw, the minds he grasped,
The suffering deep in his heart at sea
As he struggled to survive and bring his men home
But could not save them, hard as he tried—
The fools—destroyed by their own recklessness
When they ate the oxen of Hyperion the Sun,
And that god snuffed out their day of return.

Odf these things,
Speak, Immortal One,
And tell the tale once more in our time.

By now, all the others who had fought at Troy—
At least those who had survived the war and the sea—
Were safely back home. Only Odysseus
Still longed to return to his home and his wife.
The nymph Calypso, a powerful goddess—
And beautiful—was clinging to him
In her caverns and yearned to possess him."""

    # Split the poem into a list where each element is one line.
    lib = para_1.split("\n")
    title = "The Odyssey, Book 1, Lines 1–20"

    # Rebuild the poem by joining the lines with '\n' and adding a title.
    para_2 = title + "\n\n" + "\n".join(lib)

    # Replace every incorrect "Odf" with "Of".
    para_3 = para_2.replace("Odf", "Of")

    # Find the first occurrence of "Troy".
    idx_troy = para_3.find("Troy")

    print("Original Text")
    print("-" * 40)
    print(para_1)

    print("Text split along newlines")
    print("-" * 40)
    print(lib)

    print("\nPoem rejoined with Title")
    print("-" * 40)
    print(para_2)

    print("\nCorrected Text")
    print("-" * 40)
    print(para_3)

    print("\nSearch Result")
    print("-" * 40)
    print(f"'Troy' first appears at index: {idx_troy}")


if __name__ == "__main__":
    main()
