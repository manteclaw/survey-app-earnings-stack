#!/usr/bin/env python3
"""Quick analysis of Survey App Earnings Stack sample data."""

import csv
from collections import Counter

def load_data():
    with open("sample.csv", "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def summarize(rows):
    print(f"Rows: {len(rows)}")
    print(f"Columns: {', '.join(rows[0].keys())}")
    print("\nFirst 3 rows:")
    for row in rows[:3]:
        print(f"  {row}")
    print("\nColumn summaries:")
    for col in rows[0].keys():
        try:
            vals = [float(r[col]) for r in rows if r[col].replace('.','').replace('-','').isdigit()]
            if vals:
                print(f"  {col}: avg={sum(vals)/len(vals):.2f}, range=[{min(vals):.2f}, {max(vals):.2f}]")
        except:
            counts = Counter(r[col] for r in rows)
            print(f"  {col}: {dict(counts.most_common(3))}")

if __name__ == "__main__":
    rows = load_data()
    summarize(rows)
