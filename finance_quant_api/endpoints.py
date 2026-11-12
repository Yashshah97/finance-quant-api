"""
JSON Endpoints for Finance Quant REST API
----------------------------------------

This module provides the JSON endpoints for the Finance Quant REST API.

Endpoints:
    - /time-series: Get time series data for a given symbol.
    - /risk-metrics: Get risk metrics for a given symbol.

Validation:
    - Input validation is performed on all endpoints to ensure correct usage.

"""

from http import HTTPStatus

def get_time_series(request):
    """
    Get time series data for a given symbol.

    Args:
        request (dict): API request containing 'symbol' key.

    Returns:
        dict: Time series data for the given symbol.
    """
    if 'symbol' not in request or not isinstance(request['symbol'], str):
        return {'error': 'Missing or invalid "symbol" parameter'}, HTTPStatus.BAD_REQUEST

    # Simulate time series data (replace with actual implementation)
    time_series_data = {
        'symbol': request['symbol'],
        'data': [
            {'date': '2022-01-01', 'value': 100.0},
            {'date': '2022-01-02', 'value': 120.0},
            {'date': '2022-01-03', 'value': 110.0}
        ]
    }

    return time_series_data, HTTPStatus.OK

def get_risk_metrics(request):
    """
    Get risk metrics for a given symbol.

    Args:
        request (dict): API request containing 'symbol' key.

    Returns:
        dict: Risk metrics for the given symbol.
    """
    if 'symbol' not in request or not isinstance(request['symbol'], str):
        return {'error': 'Missing or invalid "symbol" parameter'}, HTTPStatus.BAD_REQUEST

    # Simulate risk metrics data (replace with actual implementation)
    risk_metrics_data = {
        'symbol': request['symbol'],
        'metrics': [
            {'name': 'Value at Risk', 'value': 10.0},
            {'name': 'Expected Shortfall', 'value': 5.0}
        ]
    }

    return risk_metrics_data, HTTPStatus.OK
