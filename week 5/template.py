"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl Dahoo
Lane  :  IT      
Date  : 21 Oct 2026

Run it:   python template.py


"""

# ====================================================================== CLASS
# 1.
class Record:
    """One server: a hostname, GB used and GB total"""

    def __init__(self, label, value, limit):
        """Store the hostname, GB used and GB total on this object."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK for this record."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. 
def load_records(path):
    """Read label, value, limit, lines from a file and return a list of Records"""
    loaded = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            loaded.append(Record(label, float(value), float(limit)))
    return loaded

records = load_records("records.txt")

# ==================================================================== OUTPUT
# 3.
over_limit_total = 0

for record in records:
    result = record.status()
    if result == "OVER LIMIT":
            over_limit_total += 1

    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f" GB used : {record.value}")
    print(f" GB total : {record.limit}")
    print(f" status : {result}")
    print("=" * 34)

print()
print(f"{over_limit_total} of {len(records)} records are OVER LIMIT")
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
