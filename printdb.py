from persistence import repo

def print_table(name, rows):
    print(name)
    for row in rows:
        print(tuple(row)) 

def print_employees_report():
    print("Employees report")
    query = """
    SELECT employees.name, employees.salary, branches.location, 
           COALESCE(SUM(ABS(activities.quantity) * products.price), 0) AS total_sales_income
    FROM employees
    LEFT JOIN branches ON employees.branche = branches.id
    LEFT JOIN activities ON employees.id = activities.activator_id
    LEFT JOIN products ON activities.product_id = products.id
    GROUP BY employees.id
    ORDER BY employees.name;
    """
    rows = repo.execute_command(query)
    for row in rows:
        print(tuple(row))

def print_activities_report():
    print("Activities report")
    query = """
    SELECT activities.date, products.description, activities.quantity, 
           CASE WHEN activities.quantity < 0 THEN employees.name ELSE NULL END AS seller_name, 
           CASE WHEN activities.quantity > 0 THEN suppliers.name ELSE NULL END AS supplier_name
    FROM activities
    LEFT JOIN products ON activities.product_id = products.id
    LEFT JOIN employees ON activities.activator_id = employees.id AND activities.quantity < 0
    LEFT JOIN suppliers ON activities.activator_id = suppliers.id AND activities.quantity > 0
    ORDER BY activities.date;
    """
    rows = repo.execute_command(query)
    for row in rows:
        print(tuple(row))

def main():
    print_table("Activities", repo.activities.find_all())
    print_table("Branches", repo.branches.find_all())
    print_table("Employees", repo.employees.find_all())
    print_table("Products", repo.products.find_all())
    print_table("Suppliers", repo.suppliers.find_all())
    print_employees_report()
    print_activities_report()

if __name__ == '__main__':
    main()
