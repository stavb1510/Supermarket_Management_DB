from persistence import *

import sys

def apply_action(splittedline):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    activator_id = int(splittedline[2])
    date = splittedline[3]

    product = repo.products.find(id=product_id)
    if not product:
        return 
    
    current_quantity = product[0].quantity
    
    if quantity < 0: ## Employee
        if current_quantity + quantity >= 0:
            repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
            repo.products.update_quantity(product_id, current_quantity + quantity)
    else: ## Supplier
        repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
        repo.products.update_quantity(product_id, current_quantity + quantity)

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            apply_action(splittedline)

if __name__ == '__main__':
    main(sys.argv)