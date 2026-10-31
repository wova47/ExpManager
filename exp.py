import csv

#the class
class expclass:
    def __init__(self, id, amount, category):
        self.amount = amount
        self.category = category
        self.id = id

#base functions
def createfile():
    with open("expenses.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "AMOUNT", "CATEGORY"])

def write(expclass):
    with open("expenses.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([expclass.id, expclass.amount, expclass.category])

def read():
    with open("expenses.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        if reader.fieldnames == None:
            return("File empty")
        else:
            return[
                {"id": row["ID"], "amount": row["AMOUNT"], "category": row["CATEGORY"]}
                for row in reader
            ]

#adding entry
def add():
    expid = input("Name of expense: ")
    expamount = input("Amount: ")
    expcat = input("Category: ")

    newdata = expclass(expid, expamount, expcat)
    write(newdata)