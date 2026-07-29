"""
Exercise - 03: Reverse a string and check for palindromes using slicing.
"""


def main():
    # String Reversal
    # Creates a new string with the characters in reverse order.
    print("String Reversal")
    print("-" * 40)

    # Syntax: string[::-1]
    original_text = "This is a string that I want to reverse"
    reversed_text = original_text[::-1]
    print(f"Original : {original_text}")
    print(f"Reversed : {reversed_text}")
    print()


    # Palindrome Check
    # A palindrome reads the same forwards and backwards.
    print("Palindrome Check")
    print("-" * 40)

    # check on a true palindrome
    palindrome = "malayalam"
    print(f"Input    : {palindrome}")
    print(f"Reversed : {palindrome[::-1]}")
    if palindrome == palindrome[::-1]:
        print("Result   : Palindrome\n")
    else:
        print("Result   : Not a palindrome\n")

    # check on a false palindrome
    not_palindrome = "menowork"
    print(f"Input    : {not_palindrome}")
    print(f"Reversed : {not_palindrome[::-1]}")
    if not_palindrome == not_palindrome[::-1]:
        print("Result   : Palindrome")
    else:
        print("Result   : Not a palindrome")


if __name__ == "__main__":
    main()
