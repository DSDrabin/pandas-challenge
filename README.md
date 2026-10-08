# pandas finance starter

A beginner pandas track for finance and reporting. This repository was empty before this starter; it is separate from the VBA stock challenge and any other Python projects.

## Start
Install Python 3 with pip, open a terminal in the repository root, then:
```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/01_inspect_invoices.py
```
On systems where Python is named `python3`, use that command to create the environment.

Work through [the exercises](exercises/README.md) in order. The first script loads and inspects the data; you implement the remaining calculations. Use scripts first and optional notebooks later.

## Folders
| Folder | Purpose |
|---|---|
| `data/raw/` | Fictional, unchanged input CSVs |
| `scripts/` | Numbered exercise scripts |
| `notebooks/` | Optional interactive exploration |
| `exercises/` | Tasks and expected results |
| `outputs/` | Generated CSV summaries |
| `notes/` | Learning notes and observations |

All amounts are AUD; use **30 June 2026** as the reporting date. Parse ISO dates explicitly. Convert money to integer cents before calculations and matching; format dollars only for reports. Validate missing values and duplicate keys rather than silently filling them.

Use only fictional or safely anonymised datasets in this public repository.
