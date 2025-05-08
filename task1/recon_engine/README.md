# 🔄 Reconciliation Engine

A lightweight Python-based reconciliation tool that compares transaction records against a simulated ledger using fuzzy header mapping and customizable thresholds.

---

## 📁 Project Structure

```
recon_engine/
├── main.py
├── reconciler.py
├── fuzzy_mapper.py
├── ledger_schema.py
├── parsers/
│   └── __init__.py
├── samples/
│   └── sample_data.csv
├── tests/
│   └── test_reconciler.py
└── report.json
```

---

## 🚀 Features

- Supports CSV input with fuzzy header mapping using Levenshtein distance
- Dynamically loads parsers
- Maps input headers to a standardized ledger schema
- Reconciles data and categorizes records into:
  - ✅ `matched`
  - ❌ `mismatched`
  - ⚠️ `missing`
- Saves reconciliation reports to JSON
- Includes unit tests with performance tracking

---

## 🧰 Requirements

- Python 3.8+
- [python-Levenshtein](https://pypi.org/project/python-Levenshtein/)

```bash
pip install python-Levenshtein
```

---

## ▶️ Usage

Run the reconciliation engine:

```bash
python main.py
```

Sample output:

```
Available parsers: ['csv_comma', 'csv_semicolon']
Header Mapping: {'TransactionID': 'transaction_id', ...}
✅ Reconciliation complete. Report saved to report.json
Matched: 5
Mismatched: 3
Missing: 2
```

---

## 🧪 Running Tests

```bash
python -m unittest tests/test_reconciler.py
```

Performance log:

```
🕒 Reconciliation time for 10,000 records: 0.0072 seconds
```

---

## ✍️ Customization

- **Add new parsers** in the `parsers/` directory.
- **Edit the ledger schema** via `ledger_schema.py`.
- **Extend reconciliation logic** in `reconciler.py`.

---

## 📄 License

MIT License – free for personal and commercial use.

---

## 👨‍💻 Author

Made with 🛠️ by Shaikh M. Shariq
