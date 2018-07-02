from Python.Session5.Person.Person import Person


class Employee(Person):
    def __init__(self, first, last, age, ci, employee_id, department):
        super().__init__(first, last, age, ci)
        self.id = employee_id
        self.employee_department = department

    def data_employee(self):
        return self.first_name + " " + self.last_name + " " + self.age_person + " " + self.ci_person + " " + self.id + " " + self.employee_department


person1 = Person("Jin", "Romero", "27", "1234567")
employee1 = Employee("Rui", "Yagami", "25", "78945600", "8007412", "QA")

print(person1.data_person())
print(employee1.data_employee())
