import json

def parse_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def build_ledger(records, offset=0.01):
    return {
        r["transaction_id"]: {
            "amount": parse_float(r["amount"]) + offset,
            "date": r["date"],
            "description": r["description"]
        }
        for r in records
    }

def reconcile(records, threshold=0.01):
    report = {
        "matched": [],
        "mismatched": [],
        "missing": []
    }

    ledger = build_ledger(records)

    for r in records:
        tx_id = r.get("transaction_id")
        if tx_id not in ledger:
            report["missing"].append(tx_id)
            continue

        expected = ledger[tx_id]
        actual_amount = parse_float(r.get("amount"))

        if abs(actual_amount - expected["amount"]) > threshold:
            report["mismatched"].append({
                "transaction_id": tx_id,
                "expected_amount": expected["amount"],
                "actual_amount": actual_amount
            })
        else:
            report["matched"].append(tx_id)

    return report

def save_report(report, path="report.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
