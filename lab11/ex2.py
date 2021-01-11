class Employee:
    def __init__(self,name,salary):
        self.set_name(name)
        self.set_salary(salary)

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_salary(self):
        return self.salary
    def set_salary(self,salary):
        if salary>0:
            self.salary = salary



class Company:
    def __init__(self):
        self.employee_list = []

    def get_employee_list(self):
        return self.employee_list
    def set_employee_list(self,employee_list):
        if type(employee_list) == list:
            self.employee_list = employee_list

    def add_employee(self, new_employee):
        if isinstance(new_employee,Employee):
            self.employee_list.append(new_employee)
    def calc_ave_salary(self):
        summ = 0
        for emp in self.employee_list:
            summ += emp.get_salary()
        return summ / len(self.employee_list)

    def display(self):
        for emp in self.employee_list:
            print("name:",emp.get_name(),"salary:",emp.get_salary())



c = Company()
e1 = Employee("One",10)
e2 = Employee("Two",20)
e3 = Employee("Three",30)



c.add_employee(e1)
c.add_employee(e2)
c.add_employee(e3)
c.add_employee(90)
c.display()



print("Average Salary:",c.calc_ave_salary())