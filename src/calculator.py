"""Calculator module providing basic arithmetic operations."""

from typing import Union

Number = Union[int, float]

class Calculator:
    """A simple calculator class implementing basic arithmetic operations."""

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers."""
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract second number from first number."""
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: Number, b: Number) -> Number:
        """Calculate a raised to the power of b."""
        return a ** b