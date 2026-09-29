#!/usr/bin/env python

import operator

try:
    input_func = raw_input
except NameError:
    input_func = input

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    ">>": operator.rshift,
    "<<": operator.lshift,
    "%": operator.mod,
    "**": operator.pow
}


def parse_number(text):
    try:
        return int(text)
    except ValueError:
        return float(text)


def get_user_input():
    try:
        number1 = parse_number(input_func("Enter first number: "))
        number2 = parse_number(input_func("Enter second number: "))
        op = input_func("Enter function (+, -, *, /, >>, <<, %, **): ")
        func = operators.get(op)

        if func is None:
            return (None, None, None)

        if op in (">>", "<<"):
            if not isinstance(number1, int) or not isinstance(number2, int):
                return (None, None, None)

    except (ValueError, TypeError):
        return (None, None, None)

    return (number1, number2, func)


if __name__ == "__main__":
    while True:
        num1, num2, func = get_user_input()

        if num1 is None or num2 is None or func is None:
            print("Invalid input")
            break

        try:
            print(func(num1, num2))
        except (ArithmeticError, ValueError):
            print("Invalid calculation")
            break