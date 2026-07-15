def main():
    def test_arg(num = 5, word = "Hello"):
        print(num+15, word)

    test_arg(15, "Bazinga!")  # Works just fine


    # POSITIONAL ARGUMENT TEST
    #test_arg("Hello", 5) # Gives Errors

    # DEFAULT ARGUMENT TEST
    # test_arg() # Gives Default values as output

    # KEYWORD ARGUMENT TEST
    # test_arg(word = "Hail Mary!", num = 52) # Named arguments, Order doesn't matter


if __name__ == "__main__":
    main()
