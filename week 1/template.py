"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl 
Lane  :  AI 
Date  : 4 Oct 2024

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
label = input("Dataset name: ")
first = float(input("Rows loaded: "))
second = float(input("Rows expected: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
difference = first - second
percent = first / second * 100

percent_missing = 100 - percent


# =================================================================== OUTPUT
# 3. Print the report.
#
#print(f"  Loaded      : {first:>10.2f}")
print(f"  Expected    : {second:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent:>10.2f} %")
print(f"  Missing %   : {percent_missing:>10.2f} %")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
