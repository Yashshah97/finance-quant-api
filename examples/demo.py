"""Demo for Finance Quant Rest Api."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import finance_quant_api

print("Finance Quant Rest Api", "v" + finance_quant_api.__version__)
print("modules:", [m for m in dir(finance_quant_api) if not m.startswith('_')])
