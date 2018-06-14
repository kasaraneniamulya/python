class Employee:                   #creating a class employee
    employee_count = 0             #varaiable to count the num of employees
    sal_list=[]
    def __init__(self,name,family,salary,department): #created a constructor init to initialize name, family, salary and department
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.sal_list.append(self.salary)
        Employee.employee_count += 1

    def avg_salary(self):     #defining a method for avg salary
        return sum(Employee.sal_list)/Employee.employee_count



class Full_time_employee(Employee):         #creating a child class full time employee
    def __init__(self, name, family, salary, department ):
       super().__init__(name,family,salary,department) #inheriting the properties of employee class


emp = Employee("alekya", 4, 50000,"HR")
emp1 = Full_time_employee("amulya", 4, 20000, "development")
emp2 = Full_time_employee("anuhya", 4, 20000, "testing")

print(Full_time_employee.avg_salary(Employee))
print(Employee.employee_count)