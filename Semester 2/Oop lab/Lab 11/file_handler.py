import csv
from manager import Manager
from worker import Worker

class FileHandler:
    @staticmethod
    def save_employees(employees):
        with open("employees.csv", mode="w", newline="") as file:
            writer.writerow("Name", "Age", "Salary", "Department", "Hours Wrked")
            writer = csv.writer(file)
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), ''])
                elif isinstance(employee, Worker):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), '', employee.get_hours_worked()])

    @staticmethod
    def load_employees():
        employees = []
        try:
            with open("employees.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    name, age, salary, department, hours_worked = row
                    if department:
                        employees.append(Manager(name, int(age), int(salary), department))
                    elif hours_worked:
                        employees.append(Worker(name, int(age), int(salary), int(hours_worked)))
        except FileNotFoundError:
          
            print("employees.csv is not exit. Star with adding new employee.")
            with open("employees.csv", mode="w") as file:
                pass
        return employees
