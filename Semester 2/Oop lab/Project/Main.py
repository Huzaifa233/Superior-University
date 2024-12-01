filename = "Management.csv"

def load_employees():
    employees = []
    try:
        with open(filename, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["dept"]:
                    employees.append(Manager(row["name"], int(row["age"]), float(row["salary"]), row["dept"]))
                elif row["hours_worked"]:
                    employees.append(Worker(row["name"], int(row["age"]), float(row["salary"]), int(row["hours_worked"])))
    except FileNotFoundError:
        pass
    return employees


def save_employees(employees):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["name", "age", "salary", "dept", "hours_worked"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for emp in employees:
            if isinstance(emp, Manager):
                csv_writer.writerow({
                    "name": emp.get_name(),
                    "age": emp.get_age(),
                    "salary": emp.get_salary(),
                    "dept": emp.get_dept(),
                    "hours_worked": ""
                })
            elif isinstance(emp, Worker):
                csv_writer.writerow({
                    "name": emp.get_name(),
                    "age": emp.get_age(),
                    "salary": emp.get_salary(),
                    "dept": "",
                    "hours_worked": emp.get_hours_worked()
                })

def add_employee():
    emp_type = input("Enter the type of employee(Manager/Worker): ").strip().lower()
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    salary = float(input("Enter the salary: "))

    if emp_type == "manager":
        dept = input("Enter the department: ")
        new_employee = Manager(name, age, salary, dept)
    elif emp_type == "worker":
        hours_worked = int(input("Enter the hours worked: "))
        new_employee = Worker(name, age, salary, hours_worked)
    else:
        print("Invalid employee type...")
        return None

    employees = load_employees()
    employees.append(new_employee)
    save_employees(employees)
    print("Employee added successfully...")


def display_employees():
    employees = load_employees()
    if not employees:
        print("No employees found...")
        return

    for emp in employees:
        print(f"Name: {emp.get_name()}, Age: {emp.get_age()}, Salary: {emp.get_salary()}")
        if isinstance(emp, Manager):
            print(f"Department: {emp.get_dept()}")
        elif isinstance(emp, Worker):
            print(f"Hours Worked: {emp.get_hours_worked()}")
        print("-" * 30)

def update_employee():
    name = input("Enter the name of the employee to update: ").strip()
    employees = load_employees()
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            new_name = input("Enter new name (leave blank to keep unchanged): ")
            if new_name:
                emp.set_name(new_name)

            new_age = input("Enter new age (leave blank to keep unchanged): ")
            if new_age:
                emp.set_age(int(new_age))

            new_salary = input("Enter new salary (leave blank to keep unchanged): ")
            if new_salary:
                emp.set_salary(float(new_salary))

            if isinstance(emp, Manager):
                new_dept = input("Enter new department (leave blank to keep unchanged): ")
                if new_dept:
                    emp.set_dept(new_dept)
            elif isinstance(emp, Worker):
                new_hours = input("Enter new hours worked (leave blank to keep unchanged): ")
                if new_hours:
                    emp.set_hours_worked(int(new_hours))

            save_employees(employees)
            print("Employee updated successfully.")
            return
    print("Employee not found.")

def promote_employee():
    name = input("Enter the name of the employee to promote: ")
    employees = load_employees()
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            percentage = float(input("Enter the percentage increase in salary: "))
            new_salary = emp.get_salary() * (1 + percentage / 100)
            emp.set_salary(new_salary)
            save_employees(employees)
            print("Employee salary updated successfully.")
            return

    print("Employee not found.")


def login():
    print("Welcome to the Employee Management System!!")
    username = input("Enter the username: ")
    password = input("Enter password: ")

    if username == "Laptop" and password == "Project2024":
        print("Login successful!!")
        return True
    else:
        print("Invalid Requirements.....")
        return False


def delete_employee():
    name = input("Enter the name of the employee for delete: ").strip()
    employees = load_employees()
    updated_employees = [emp for emp in employees if emp.get_name().lower() != name.lower()]
    if len(updated_employees) < len(employees):
        save_employees(updated_employees)
        print("Employee is deleted successfully.")
    else:
        print("Employee not found.")



def main():
    if not login():
        return

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Promote Employee")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            promote_employee()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()