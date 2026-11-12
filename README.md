# Finance Quant Rest Api

This is a lightweight REST API designed to provide access to market time series and risk metrics, allowing developers to easily integrate financial data into their applications. Built from the ground up in pure Python, this API prioritizes simplicity and ease of use while maintaining robust input validation and thorough testing. With JSON endpoints and comprehensive documentation, users can quickly get started with integrating this API into their projects.

## What makes it unique

Combines market time series and risk metrics with a lightweight HTTP API with JSON endpoints and input validation — a niche where few ready-made tools exist.

## Features

- **`finance_quant_api/app.py`** — Main application entry point
- **`finance_quant_api/endpoints.py`** — JSON endpoints for API
- **`finance_quant_api/models.py`** — Data models and schema definitions
- **`finance_quant_api/services.py`** — Business logic services and utility functions
- **`finance_quant_api/tests_test_api.py`** — Unit tests for the API
- **`finance_quant_api/utils_validation.py`** — Input validation and sanitization utilities

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/finance-quant-api.git
cd finance-quant-api

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
finance-quant-api/
├── finance_quant_api/
│   ├── app.py
│   ├── endpoints.py
│   ├── models.py
│   ├── services.py
│   ├── tests_test_api.py
│   ├── utils_validation.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **finance-quant** · Archetype: **api** ·
Built autonomously by JARVIS on 2026-11-11. MIT licensed.
