
#
class PlaceHolder:
    pass


class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")

    age = 25

    @staticmethod
    def get_age():
        pass


a = Person("Serhii")
a.print_name()


class Student(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name)
        self.surname = surname

    def print_surname(self):
        print(f"My surname is {self.surname}")


b = Student('Serhii', 'Yatsiuk')
b.print_name()
b.print_surname()
