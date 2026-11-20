#!/usr/bin/env python3
"""
Simple CLI Calculator
=====================

A minimal command-line calculator supporting basic arithmetic.

Supported operations: addition, subtraction
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


# Dictionary mapping operation names to their functions
OPERATIONS = {
    "add": add,
    "subtract": subtract,
}


def main():
    print("=" * 32)
    print("        SIMPLE CALCULATOR")
    print("=" * 32)
    print("Available operations:", ", ".join(OPERATIONS))

    try:
        first = float(input("Enter first number:  "))
        second = float(input("Enter second number: "))
    except ValueError:
        print("Error: please enter numeric values.")
        return

    op = input("Enter operation: ").strip().lower()
    if op not in OPERATIONS:
        print(f"Error: unknown operation '{op}'.")
        print("Available operations:", ", ".join(OPERATIONS))
        return

    print(f"Result: {OPERATIONS[op](first, second)}")


if __name__ == "__main__":
    main()
