import os, json

def save_report(filename, masked_items):
    os.makedirs("../reports", exist_ok=True)
    out_path = os.path.join("../reports", f"{filename}.json")
    with open(out_path, "w") as f:
        json.dump(masked_items, f, indent=2)
    print(f"[+] Report saved: {out_path}")
