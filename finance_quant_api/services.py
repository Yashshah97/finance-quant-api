"""
Services and utility functions for finance quant API.

This module contains business logic services and utility functions used by the API.
"""

def calculate_mean(data):
    """
    Calculate mean of a list of numbers.

    Args:
        data (list): List of numbers.

    Returns:
        float: Mean of the input list.
    """
    return sum(data) / len(data)


def calculate_volatility(data, window_size=30):
    """
    Calculate volatility of a list of numbers using moving average.

    Args:
        data (list): List of numbers.
        window_size (int): Size of the moving average window. Defaults to 30.

    Returns:
        float: Volatility of the input list.
    """
    if len(data) < window_size:
        raise ValueError("Data must be at least as long as the window size")

    means = [calculate_mean(data[i-window_size+1:i]) for i in range(window_size-1, len(data))]
    return calculate_mean(means)


def validate_date(date_str):
    """
    Validate a date string.

    Args:
        date_str (str): Date string to validate.

    Returns:
        bool: Whether the date is valid.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_asset(asset):
    """
    Validate an asset symbol.

    Args:
        asset (str): Asset symbol to validate.

    Returns:
        bool: Whether the asset is valid.
    """
    return len(asset) == 6 and asset.isalpha()
