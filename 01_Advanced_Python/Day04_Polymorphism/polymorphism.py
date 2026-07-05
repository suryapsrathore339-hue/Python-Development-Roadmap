class Employee:
    def work(self):
        pass

class Teacher(Employee):
    def work(self):
        print("Teaching Students")

class Doctor(Employee):
    def work(self):
        print("Treating patients")

class Engineer(Employee):
    def work(self):
        print("Building Software")

employees=[Teacher(),Doctor(),Engineer()]

for employee in employees:
    employee.work()
    