from Python.Exam.Person import Person


class EmployeeCommercial(Person):

    def __init__(self, name, pieces, department, num):
        super().__init__(name, pieces)
        self.department = department
        self.id = "CE-00" + str(num)
        self.salary = 0
        self.discount = 0

    def get_id(self):
        return self.id

    def get_salary(self):
        return self.pieces * 2.5

    def get_discount(self):
        return self.get_salary() * 12.5 / 100

    def get_net_salary(self):
        return self.get_salary() - self.get_discount()

    def get_employee(self):
        return "{}| {}| {}| {}| {}| {}".format(self.id, self.name, self.department, str(self.get_salary()), str(
            self.get_discount()), str(self.get_net_salary()))
