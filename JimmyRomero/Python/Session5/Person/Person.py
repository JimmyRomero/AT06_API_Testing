class Person:
    def __init__(self, first, last, age, ci):
        self.first_name = first
        self.last_name = last
        self.age_person = age
        self.ci_person = ci

    def data_person(self):
        return self.first_name + " " + self.last_name + " " + self.age_person + " " + self.ci_person
