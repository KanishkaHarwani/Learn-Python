"""
unit_converter — A CLI unit converter (temperature/length/weight)
that demonstrates type casting and validation of user input types.
"""
import sys

def unit_value_input():
    unit = input("Enter the unit you to convert? ")
    value = input("Enter the value you're converting? ")
    try:
        value = float(value)
    except ValueError:
        print("You entered a non-numerical value")
        sys.exit()
    return float(value), unit

def temperature_converter():
    print("You have selected temperature conversion\n"
          "Format for value is numerical\n"
          "Valid units are C, c, F, f")
    units = ["C", "F", "c", "F"]
    temperature, unit = unit_value_input()
    if unit in units:
        if unit == "C" or unit == "c":
            new_temp = 32 + temperature * 1.8
            output = f"{new_temp:.2f} F"
        if unit == "F" or unit == "f":
            new_temp = temperature / 1.8 - 32
            output = f"{new_temp:.2f} C"
    else:
        output = "The values provided are not valid"
    return output


def length_converter():
    print("You have selected length conversion\n"
          "Format for value is numerical\n"
          "Valid units are M, m, ft, Ft\n"
          "input can be 1.85m which equates to 1m and 85cm\n"
          "or 5.11ft which equates to 5.11ft not 5ft 11in")
    units = ["M", "m", "ft", "Ft"]
    length, unit = unit_value_input()
    if unit in units:
        if unit == "M" or unit == "m":
            len_cm = length * 100
            t_len_in = len_cm // 2.54
            length_ft = t_len_in // 12
            length_in = t_len_in - (length_ft * 12)
            output = f"{length_ft:.2f}ft {length_in:.2f}in"
        if unit == "Ft" or unit == "ft":
            length_m = length / 3.28084
            output = f"{length_m:.2f}m"
    else:
        output = "The values provided are not valid"
    return output

def weight_converter():
    print("You have selected weight conversion\n"
          "Format for value is numerical\n"
          "Valid units are Kg, kg, Lb, lb\n"
          "input can be 1.85kg which equates to 1kg and 850gm\n"
          "or 5.11lb which equates to 5.11lb not 5lb 11oz")
    units = ["Kg", "kg", "Lv", "lb"]
    weight, unit = unit_value_input()
    if unit in units:
        if unit == "Kg" or unit == "kg":
            weight_lb = weight * 2.20462
            output = f"{weight_lb:.2f}Lb"
        if unit == "lb" or unit == "Lb":
            weight_kg = weight / 2.20462
            output = f"{weight_kg:.2f}Kg"
    else:
        output = "The values provided are not valid"
    return output

def main():
    print("Welcome to the unit converter!")
    print("This program converts temperature/length/weight to a human readable unit")
    print("To convert Lenght type L")
    print("To convert Weight type W")
    print("To convert Temperature type T")
    convert_type = input("what do you want to convert?" )
    convert_type_list = ["L", "l", "W", "w", "T", "t"]
    if convert_type not in convert_type_list:
        print("you entered an valid input")
        print("logging off!")
        sys.exit()
    else:
        if convert_type == "L" or convert_type == "l":
            print(length_converter())

        if convert_type == "W" or convert_type == "w":
            print(weight_converter())

        if convert_type == "T" or convert_type == "t":
            print(temperature_converter())

    pass


if __name__ == "__main__":
    main()
