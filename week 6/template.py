"""
RECORD CHECK  -  my version
===========================

Name  : Jashyl Dahoo
Lane  :  IT     
Date  : 28 Oct 2026

Run it:   python template.py

"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1.

df = pd.read_csv("records_sample.csv") 
print(df.columns)
# ================================================================= PROCESS
# 2. 

df["percent"] = (df["value"] / df["limit"]) * 100 
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)   

# ================================================================== OUTPUT
# 3.
print("All servers:")
print(df)

print("\nServers that are not OK:")
print(df[df["status"] != "OK"])

counts = df.groupby("status")["status"].count()
print("\nCounts per status:")
print(counts)

df.to_csv("servers_report.csv", index=False)

counts.plot(kind="bar")
plt.title("Servers per status")
plt.savefig("Servers_status.png")
plt.show()
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
