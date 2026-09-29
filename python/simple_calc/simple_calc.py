#!/usr/bin/env python3

import operator


operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def get_user_input():
    """Get input from the user.

    Returns tuple: (number, number, function), or
    (None, None, None) if the inputs are invalid.
    """
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        op = input("Enter function (valid values are +, -, *, /): ")

        func = operators.get(op)
    except Exception:
        return (None, None, None)

    return (number1, number2, func)


if __name__ == "__main__":
    while True:
        num1, num2, func = get_user_input()

        if num1 is None or num2 is None or func is None:
            print("Invalid input")
            break

        print(func(num1, num2))