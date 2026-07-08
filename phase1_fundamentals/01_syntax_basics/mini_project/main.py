"""
cli_greeter — A small CLI script that greets the user, asks for name/age/favorite language, and prints a formatted summary block.
"""


def main():
	name = input("Please provide your name: ")
	age = input("Please provide your age: ")
	language = input("Please provide your favourite language: ")
	print(f"{name} is {age} years old and his/her favourite language is {language}")
    pass


if __name__ == "__main__":
    main()
