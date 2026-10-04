"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl
Lane  :  AI  
Date  : 4 Oct 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
label = input("Label (or 'quit' to finish): ")     
value = float(input("Value: "))     
limit = float(input("Limit: "))    


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = limit - value 
percent = value / limit * 100     
# 3. Decide a status and store it in a variable called status.
#
#    

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#


print(f" {'Value':<12}: {value:>10.2f}")
print(f" {'Limit':<12}: {limit:>10.2f}")
print(f" {'Difference':<12}: {difference:>10.2f}")
print(f" {'Percent':<12}: {percent:>10.2f}%")
print(f" {'Status':<12}: {status:>10}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
