from parsers import load_parsers, PARSERS
from ledger_schema import LEDGER_FIELDS
from fuzzy_mapper import fuzzy_map_headers
from reconciler import reconcile, save_report

def main():
    load_parsers()
    print(f"Available parsers: {list(PARSERS.keys())}")

    file_path = "samples/sample_data.csv"
    parser = PARSERS["csv_comma"]
    raw_records = parser(file_path)

    if not raw_records:
        print("No records found.")
        return

    original_headers = raw_records[0].keys()
    header_map = fuzzy_map_headers(original_headers, LEDGER_FIELDS)
    print(f"Header Mapping: {header_map}")

    mapped_records = []
    for record in raw_records:
        mapped = {header_map[k]: v.strip() for k, v in record.items()}
        # Handle missing amounts
        if mapped.get("amount") == "":
            mapped["amount"] = "0.0"  # or skip the record, or log a warning
        mapped_records.append(mapped)


    print("\nMapped Records Preview:")
    for row in mapped_records[:3]:
        print(row)

    report = reconcile(mapped_records)
    save_report(report)

    print("\n✅ Reconciliation complete. Report saved to report.json")
    print(f"Matched: {len(report['matched'])}")
    print(f"Mismatched: {len(report['mismatched'])}")
    print(f"Missing: {len(report['missing'])}")

if __name__ == "__main__":
    main()
