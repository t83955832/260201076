class Employee:
    def __init__(self,name,salary):
        self.setName(name)
        self.setSalary(salary)
    def getName(self):
        return self.name
    def setName(self,name):
        if name!="":
            self.name=name
    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        if salary<0:
            self.salary=salary


class Company:
    pass