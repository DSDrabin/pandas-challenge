# Beginner exercises

Allow roughly 30–45 minutes per exercise. Run each script from the repository root and record a lesson in `notes/progress.md`.

| Step | Practical task | pandas skills | Done when |
|---|---|---|---|
| 1 | Inspect invoices; validate required columns, unique invoice IDs, dates, numeric amounts and missing values | read_csv, head, dtypes, isna, duplicated | 6 rows; no missing values or duplicate invoice IDs; invoiced $9,200; paid $2,400 |
| 2 | Add outstanding cents and filter invoices with a balance; save outputs/outstanding.csv | Column arithmetic, boolean masks, to_csv | 5 invoices; outstanding $6,800 |
| 3 | Add days overdue and ageing buckets at 30 June 2026; save outputs/ageing.csv | to_datetime, clip, cut or conditional masks, groupby | Bucket totals match checks below |
| 4 | Summarise balances by customer and write outputs/customer_summary.csv | groupby, agg, sort_values | Alpha $800; Beta $2,500; Gamma $3,500 |
| 5 | Compare bank and GL movements; write outputs/reconciliation_exceptions.csv | merge with how="outer", indicator=True, validate="one_to_one" | R003 mismatch; R004 bank only; R005 GL only |

## Shared definitions and checks
Outstanding = invoice amount − paid amount. Use integer cents for calculations; reject unexpected negative balances in this fixture.
Only positive outstanding balances enter ageing. Days overdue = max(0, reporting date − due date).
Current means due date on or after reporting date; overdue buckets are 1–30, 31–60, 61–90 and 91+ days.
Expected balances: Current $2,500; 1–30 $800; 31–60 $1,000; 61–90 $0; 91+ $2,500. Include empty buckets as zero.

For reconciliation, references must be non-null and unique in each source. Match reference first, compare signed amounts with a one-cent tolerance, and flag date differences separately. Do not match on amount alone.
R003 bank − GL = −$50. Bank net movement = $1,250; GL = $1,150; difference = $100.
Control: −$50 − $50 − (−$200) = $100.
These are movement comparisons, not a complete bank balance reconciliation.

## Suggested files
Keep the provided 01_inspect_invoices.py; create 02_outstanding.py, 03_ageing.py, 04_customer_summary.py and 05_reconcile.py.
Finish with a short report listing totals, exceptions, and the checks you performed. Run each script twice; outputs should be replaced, not appended.
