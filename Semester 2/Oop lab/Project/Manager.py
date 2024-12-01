class Manager(Employee):
    def __init__(self, name, age, salary, dept):
        super().__init__(name, age, salary)
        self.__dept = dept

    def get_dept(self):
        return self.__dept

    def set_dept(self, dept):
        self.__dept = dept