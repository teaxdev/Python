"""
Creating a student class

"""

# class names start with a capital


class Student:
    # Initializer with private variables
    # __ means private - not easily accessed from other programs
    def __init__(self, first_name, last_name, student_id, year):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__year = year

    # custom method to display all object information
    def get_info(self):
        return (
            f"{self.__first_name} {self.__last_name}, "
            "ID: {self.__student_id}, Year: {self.__year}"
        )

    # Getters

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_id(self):
        return self.__student_id

    def get_year(self):
        return self.__year

    # Setters

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_year(self, year):
        self.__year = year


student1 = Student("Buffy", "Summers", "12345", "Freshman")
student2 = Student("Willow", "Rosenberg", "45678", "Freshman")

print(student1.get_info())
print(student2.get_info())
