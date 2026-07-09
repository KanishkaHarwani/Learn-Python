def describe_command(command):
    # TODO: implement using match/case
    match command:
        case ("go", direction):
            print(f"Moving {direction}!")
        case ("take", item):
            print(f"Picking up {item}")
        case ("look",):
            print("Looking around the room")
        case ("quit",):
            print("Exiting the game")
        case _:
            print("I don't understand the command")

if __name__ == "__main__":
    # TODO: test with a few different command tuples
    command = ("go", "north")
    describe_command(command)

    command = ("take", "key")
    describe_command(command)

    command = ("look",)
    describe_command(command)

    command = ("quit",)
    describe_command(command)

    command = ("dance",)
    describe_command(command)
    pass
