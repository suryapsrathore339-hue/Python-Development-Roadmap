class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary

    def show_details(self):
        print("Name:",self.name,"| Role:",self.role,"| Salary:",self.salary)

e1=Employee("Surya","Data Analyst",2000000)
e2=Employee("Shreya","Developer",1800000)
e3=Employee("Prince","AI Expert",1900000)
e4=Employee("Anmol","UI Expert", 1600000)

e1.show_details()
e2.show_details()
e3.show_details()
e4.show_details()