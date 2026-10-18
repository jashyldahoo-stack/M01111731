"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl Dahoo
Lane  :  AI
Date  : 17 Oct 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Return the difference, percent of limit used, and status for one record."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record"""
    print(f"{label}: {value: .1f}/{limit: .1f} GB"
          f"({percent: .1f}%, diff {difference:+.1f}) -> {status}")

def print_message(text):
    """Print a one-off message (errors and the final summary)."""
    print(text)
    

# ====================================================================== STORE
# 2. 
def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label,
                            "value": float(value),
                            "limit": float(limit)})
    return records

def write_results(path, results):
    """Write one 'label, status' line per result to a file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")

try:
    records = load_records("servers.txt")
except FileNotFoundError:
    print_message("servers.txt not found - starting with no records.")
    records = []

# =============================================================== PROCESS + OUTPUT
# 3.
# your loop goes here
over_count = 0
results = []

for r in records:
    difference, percent, status = check_record(r["value"], r["limit"])
    print_report(r["label"], r["value"], r["limit"], difference, percent, status)
    results.append((r["label"], status))
    if status == "OVER LIMIT":
        over_count +=1

print_message(f"{over_count} of {len(records)} records OVER LIMIT")
write_results("results.txt", results)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
