"""
Input validation and sanitization utilities.

This module provides functions to validate and sanitize inputs for the Finance Quant API.
"""

def is_positive_integer(n: int) -> bool:
    """
    Check if a number is a positive integer.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a positive integer, False otherwise.
    """
    return isinstance(n, int) and n > 0


def is_non_negative_integer(n: int) -> bool:
    """
    Check if a number is a non-negative integer.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a non-negative integer, False otherwise.
    """
    return isinstance(n, int) and n >= 0


def validate_positive_integer(name: str, value: int) -> None:
    """
    Validate that a value is a positive integer.

    Args:
        name (str): The name of the value being validated.
        value (int): The value to check.

    Raises:
        ValueError: If the value is not a positive integer.
    """
    if not is_positive_integer(value):
        raise ValueError(f"{name} must be a positive integer")


def validate_non_negative_integer(name: str, value: int) -> None:
    """
    Validate that a value is a non-negative integer.

    Args:
        name (str): The name of the value being validated.
        value (int): The value to check.

    Raises:
        ValueError: If the value is not a non-negative integer.
    """
    if not is_non_negative_integer(value):
        raise ValueError(f"{name} must be a non-negative integer")


def validate_string(name: str, value: str) -> None:
    """
    Validate that a value is a string.

    Args:
        name (str): The name of the value being validated.
        value (str): The value to check.

    Raises:
        ValueError: If the value is not a string.
    """
    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string")


def validate_list(name: str, value: list) -> None:
    """
    Validate that a value is a list.

    Args:
        name (str): The name of the value being validated.
        value (list): The value to check.

    Raises:
        ValueError: If the value is not a list.
    """
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
