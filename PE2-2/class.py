# 3.2 OOP and Classes

class Person:

    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_info(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age} Phone Number: {self.__phone}"

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


person1 = Person("Alex", "321 Memory Ln", "20", "3213213210")
person2 = Person("Jake", "322 Memory Ln", "22", "3213213213")
person3 = Person("Mack", "320 Memory Ln", "47", "3213213212")

print(person1.get_info())
