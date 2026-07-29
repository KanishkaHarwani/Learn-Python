"""
Exercise - 05: Count word frequency in a paragraph using string methods and dictionaries.
"""

paragraph = """
Learning Python takes practice. The more you practice Python, the more confident
you become. Practice helps you understand variables, loops, functions, and
dictionaries. Python is a beginner-friendly language because its syntax is
clear and readable. Reading code, writing code, and debugging code every day
will improve your programming skills. Every small project teaches something
new, and every mistake is an opportunity to learn.
"""


def main():
    # --------------------------------------------------
    # Text Preprocessing
    # 1. Convert all words to lowercase.
    # 2. Remove common punctuation.
    # 3. Split the paragraph into individual words.
    # --------------------------------------------------
    clean_text = paragraph.lower()

    for char in ".,-":
        clean_text = clean_text.replace(char, "")

    words = clean_text.split()

    # --------------------------------------------------
    # Count the frequency of each word using a dictionary.
    # --------------------------------------------------
    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # --------------------------------------------------
    # Display Results
    # --------------------------------------------------
    print("Word Frequency Counter")
    print("-" * 40)

    print("Original Paragraph:")
    print(paragraph)

    print("\nWord Frequencies:")
    for word, count in word_count.items():
        print(f"{word:<15} : {count}")

    print("\nSummary")
    print("-" * 40)
    print(f"Total Words : {len(words)}")
    print(f"Unique Words: {len(word_count)}")


if __name__ == "__main__":
    main()
