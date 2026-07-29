"""
Exercise - 02: Format numbers and dates with f-strings.

Practice:
1. Padding (minimum field width)
2. Precision (decimal places)
3. Alignment (left, center, right)
"""

from datetime import datetime


def main():
    # --------------------------------------------------
    # Padding: Set a minimum width for the displayed value.
    # Syntax: {value:[width]}
    # --------------------------------------------------
    name = "Bill Doe"
    balance = 13.566

    print("Padding Examples")
    print("-" * 40)

    print(f"|{name:20}|")
    print(f"|{balance:20}|")
    print()

    # --------------------------------------------------
    # Precision: Control the number of decimal places.
    # Syntax: {value:.nf}
    # --------------------------------------------------
    pi = 3.14159265358979
    price = 19.999

    print("Precision Examples")
    print("-" * 40)

    print(f"Pi (1 decimal) : {pi:.1f}")
    print(f"Pi (3 decimals): {pi:.3f}")
    print(f"Price (2 dp)   : ${price:.2f}")
    print(f"Price (3 dp)   : ${price:.3f}")
    print()

    # --------------------------------------------------
    # Alignment: Position the value within a fixed width.
    # Syntax: {value:[fill][align][width]}
    # Align:
    #   <  Left
    #   ^  Center
    #   >  Right
    # --------------------------------------------------
    text = "Python"

    print("Alignment Examples")
    print("-" * 40)

    print(f"Left   : |{text:<15}|")
    print(f"Center : |{text:^15}|")
    print(f"Right  : |{text:>15}|")
    print()

    # Fill characters
    print("Fill Character Examples")
    print("-" * 40)

    print(f"|{text:=<15}|")
    print(f"|{text:-^15}|")
    print(f"|{text:.>15}|")
    print()

    # --------------------------------------------------
    # Date Formatting
    # --------------------------------------------------
    today = datetime.now()

    print("Date Formatting Examples")
    print("-" * 40)

    print(f"Default : {today}")
    print(f"Date    : {today:%Y-%m-%d}")
    print(f"US      : {today:%m/%d/%Y}")
    print(f"Long    : {today:%B %d, %Y}")


if __name__ == "__main__":
    main()
