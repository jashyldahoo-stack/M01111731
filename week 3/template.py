"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl Dahoo
Lane  :  AI / Cyber / IT      (delete two)
Date  : 10 Oct 2026

Run it:   python template.py


"""

# =================================================================== FUNCTIONS
# 1. 
# your function(s) go here
def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >=100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Return the free amount and the percentage used."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, perncent, status):
    """Print the bordered report for one record"""
    print()
    print("= * 34")
    print(f" RECORD CHECK - {label}")
    print(f" Used : {value:10.2f}")
    print(f" Total : {limit:10.2f}")
    print(f" Free : {difference:10.2f}")
    print(f" Percent : {percent}")
    print(f" Status : {status:.10}")
    print("= * 34")

# ==================================================================== INPUT
# 2.
over_count = 0

while True:
    label = input("Hostname (or quit): ")
    if label.lower() == "quit":
        break

value = float(input("GB used: "))
limit = float(input("GB total:"))
# ================================================================== PROCESS
# 3.
difference, percent = check(value, limit)
status = status_of(percent)
# =================================================================== OUTPUT
# 4. 
print_report(label, value, difference, percent, status)

if status == "OVER LIMIT":
    over_count += 1

print("Records over limit:", over_count)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
