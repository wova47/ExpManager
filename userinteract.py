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
    
    #for cmd in part:
    cmdg = part[0].strip().lower()
    if cmdg == "reset":
        print("")
        exp.createfile()
        print("Reset file")
        print("")
    elif cmdg == "quit":
        print("")
        print("Quitting...")
        break
    elif cmdg == "read":
        print("")
        print(output.allnames())
        print("")
    elif cmdg == "details":
        print("")
        print(output.itemattributes(part[1]))
        print("")
    elif cmdg == "add":
        print("")
        exp.add()
        print("")
        print("Added sucessfully")
        print("")
    else:
        print("")
        print("Unknown command")