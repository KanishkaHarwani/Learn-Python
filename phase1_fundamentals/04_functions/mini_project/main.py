"""
calculator_functions — A calculator module where each operation
(add/sub/mul/div/power) is its own function, dispatched via a dictionary of functions.
"""
import sys

def main():
    def calculator_function(operator, *args):
        def add(*args):
            total = 0
            for arg in args:
                total += arg
            return total

        def mul(*args):
            total = 1
            for arg in args:
                total *= arg
            return total

        def pow(*args):
            if len(args) == 2:
                return args[0] ** args[1]
            else:
                return "the power function only accepts two arguments\nLogging Off!"

        def sub(*args):
            if len(args) == 2:
                return args[0] - args[1]
            else:
                return "the sub function only accepts two arguments\nLogging Off!"

        def div(*args):
            if len(args) == 2 and args[1] != 0:
                return args[0] / args[1]
            elif args[1] == 0:
                return "the division function does not take 0 as a divisor\nLogging Off!"
            else:
                return "the div function only accepts two arguments\nLogging Off!"

        module_dictionary = {"add": add, "mul": mul, "sub": sub, "div": div, "power": pow}
        return module_dictionary[operator](*args)

    print("This is a CLI calculator program")
    print("""the choices for the operator are add/sub/mul/div/por for 
    addition, substraction, multiplication, division and power""")
    operator = input("Please enter your operator: ").lower()
    operators = ("add", "sub", "mul", "div", "power")
    if operator in operators:
        arguments_string = input("Please enter your arguments: ").split()
        try:
            arguments = list(map(float, arguments_string))
            result = calculator_function(operator, *arguments)
            print(f"The result is {result}")
        except ValueError:
            print("Non-numeric values entered")
            print("Logging Off!")
            sys.exit()

    else:
        print("Input is not a valid operator")
        print("Logging Off!")
        sys.exit()

if __name__ == "__main__":
    main()
