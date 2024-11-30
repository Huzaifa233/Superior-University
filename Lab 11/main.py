from manager import Manager
from worker import Worker
from file_handler import FileHandler

def add_employee(employees):
    employee_type = input("Enter employee type (manager/worker): ").strip().lower()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = int(input("Enter salary: "))
    if employee_type == 'manager':
        department = input("Enter department: ")
        employees.append(Manager(name, age, salary, department))
    elif employee_type == 'worker':
        hours_worked = int(input("Enter hours worked: "))
        employees.append(Worker(name, age, salary, hours_worked))

def display_employees(employees):
    for employee in employees:
        employee.display_info()
        print('-' * 20)

def update_employee(employees):
    name = input("Enter the name of the employee to update: ").strip()
    for employee in employees:
        if employee.get_name() == name:
            print(f"Updating details for {name}:")
            
            
            new_name = input("Enter new name: ").strip()
            employee.set_name(new_name)
            
         
            new_age = int(input("Enter new age: ").strip())
            employee.set_age(new_age)
            
         
            new_salary = int(input("Enter new salary: ").strip())
            employee.set_salary(new_salary)
            
          
            if isinstance(employee, Manager):
                new_department = input("Enter new department: ").strip()
                employee.set_department(new_department)
            
            # Update hours worked if Worker
            if isinstance(employee, Worker):
                new_hours_worked = int(input("Enter new hours worked: ").strip())
                employee.set_hours_worked(new_hours_worked)
            
            print(f"Details for {name} updated successfully!")
            break
    else:
        print(f"Employee with name '{name}' not found.")


def delete_employee(employees):
    name = input("Enter name of employee to delete: ").strip()
    updated_employees = [emp for emp in employees if emp.get_name().lower() != name.lower()]

    if len(updated_employees) == len(employees):
        print("Employee not found.")
    else: 
        FileHandler.save_employees(updated_employees) 
        employees[:] = updated_employees
        print("Employee deleted successfully.")


def main():
    employees = FileHandler.load_employees()

    while True:
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            display_employees(employees)
        elif choice == 3:
            update_employee(employees)
        elif choice == 4:
            delete_employee(employees)
        elif choice == 5:
            FileHandler.save_employees(employees)
            print("Exiting...")
            break

if __name__ == '__main__':
    main()
