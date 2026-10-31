import exp
import output
import os

#for print
nl = "\n"

print(f"Commands:{nl}Quit -- quit app{nl}Reset -- reset file{nl}Read -- list all entries{nl}Details ITEMID -- list details of entry by name{nl}Add -- add new entry")
print("")

if not os.path.exists("expenses.csv"):
    exp.createfile()

while True:
    line = input(">>> ")
    part = line.split()

    if "quit" in part[0]:
        print("quitting...")
        break
    
    else:
        for cmd in part:
            cmdg = cmd.strip().lower()
            if cmdg == "reset":
                print("Reset file")
                exp.createfile()
            elif cmdg == "quit":
                print("Quitting...")
                break
            elif cmdg == "read":
                print(output.allnames())
            elif cmdg == "details":
                print(output.itemattributes(part[1]))
            elif cmdg == "add":
                exp.add()