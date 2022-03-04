
# Instance methods have 'self' has a mandatory first argument
# class methods have 'cls' has mandatory first argument and that method should contain '@classmethod' decorator
# Static methods don't have any mandatory arguments but it should contain '@staticmethod' decorator
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        print(self.lastname + self.firstname)

    def instance_method(self):
        print("this is instance method for student class")

    @classmethod
    def divide_string(cls, name):
        name = name.split(" ")
        print(name)

    @staticmethod
    def static_method():
        print("your invoked static method present inside the student class")


if __name__ == "__main__":
    Student.divide_string("kalyan kundella")
    stud = Student("Kalyan", "Kundella")
    stud.instance_method()
    stud.static_method()
    Student.static_method()