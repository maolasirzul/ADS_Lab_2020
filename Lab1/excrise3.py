""""
Author: Maola Sirzul
Date started:19/1/2021
Version: Final
Description: opening file
"""

f = open("lucky_ids.txt", "r")
if "000973114" in f.read():
    print("Yes")
else:
    print("No")
