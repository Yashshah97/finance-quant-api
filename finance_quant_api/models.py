"""
Data models and schema definitions for finance quant API.

This module defines the data structures used to represent market time series and risk metrics.
"""

from typing import Dict, List, Optional
import datetime

class TimeSeries:
    """Market time series data model."""

    def __init__(self, symbol: str, data: Dict[datetime.date, float]):
        """
        Initialize a TimeSeries instance.

        :param symbol: Market symbol (e.g., stock ticker)
        :param data: Time series data as a dictionary of dates to values
        """
        self.symbol = symbol
        self.data = data

    def __repr__(self) -> str:
        return f"TimeSeries(symbol='{self.symbol}', data={self.data})"


class RiskMetrics:
    """Risk metrics data model."""

    def __init__(self, symbol: str, data: Dict[str, float]):
        """
        Initialize a RiskMetrics instance.

        :param symbol: Market symbol (e.g., stock ticker)
        :param data: Risk metrics as a dictionary of names to values
        """
        self.symbol = symbol
        self.data = data

    def __repr__(self) -> str:
        return f"RiskMetrics(symbol='{self.symbol}', data={self.data})"


class Quote:
    """Market quote data model."""

    def __init__(self, symbol: str, bid: float, ask: float):
        """
        Initialize a Quote instance.

        :param symbol: Market symbol (e.g., stock ticker)
        :param bid: Bid price
        :param ask: Ask price
        """
        self.symbol = symbol
        self.bid = bid
        self.ask = ask

    def __repr__(self) -> str:
        return f"Quote(symbol='{self.symbol}', bid={self.bid}, ask={self.ask})"
