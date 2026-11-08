"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl Dahoo
Lane  :  IT     
Date  : 4 Nov 2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1.
def parse_line(rawline):
     """Clean one raw line and return it as a dict."""
     raw_line = rawline.strip().lower()
     hostname, rest = raw_line.split(",", 1)
     record= {"hostname": hostname.strip()}
     for piece in rest.split(","):
         key, value = piece.split("=")
         record[key.strip()] = float(value.strip())
     return record

def status_of(record):
    """Return OVER LIMIT, WARNING, or OK for one parsed record."""
    percent = record["used"] / record["total"] * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"   
    else:
        return "OK"


# ====================================================================== INPUT
# 2.
with open("raw_records.txt") as file:
    raw_records = file.readlines()



# =============================================================== PROCESS + OUTPUT
# 3.
total_records = 0
flagged = 0

for raw_record in raw_records:
    if raw_record.strip() == "":
        continue
    try:
        record = parse_line(raw_record)
    except ValueError:
        print("Could not parse:", raw_record.strip())
        continue
    status = status_of(record)
    print(record, status)
    total_records += 1
    if status != "OK":
        flagged += 1

print(f"{total_records} records, {flagged} flagged")
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
