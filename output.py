import exp

#getting all data
allrows = exp.read()

#getting all existing entry ids
def allnames():
    if allrows != "File empty":
        for row in allrows:
            return(row["id"])
    else: 
        return("File empty")

#getting all attributes of a single searched id
def itemattributes(wantedid):
    matching = 0
    allfound = []
    for item in allrows:
        if item["id".strip().lower()] == wantedid.strip().lower():
            allfound.append(f"{item["id"]}, {item["amount"]}, {item["category"]}")
    if not allfound:
        return("No matching entry")
    else:
        return "\n".join(allfound)