from persistence import *

import sys
import os

def add_branche(splittedline):
    repo.branches.insert(Branche(int(splittedline[0]), splittedline[1], int(splittedline[2])))

def add_supplier(splittedline):
    repo.suppliers.insert(Supplier(int(splittedline[0]), splittedline[1], splittedline[2]))

def add_product(splittedline):
    repo.products.insert(Product(int(splittedline[0]), splittedline[1], float(splittedline[2]), int(splittedline[3])))

def add_employee(splittedline):
    repo.employees.insert(Employee(int(splittedline[0]), splittedline[1], float(splittedline[2]), int(splittedline[3])))

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline = line.strip().split(",")
            if splittedline[0] in adders:
                adders[splittedline[0]](splittedline[1:])
if __name__ == '__main__':
    main(sys.argv)