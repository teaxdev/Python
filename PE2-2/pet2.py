# 3.4 OOP Methods

class Pet:

    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    def get_kind(self):
        return self.__kind

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name

    def set_kind(self, value):
        self.__kind = value

    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value

    def print_details(self):
        print(f"\nDisplay Kind: {self.__kind}")
        print(f"Display Breed: {self.__breed}")
        print(f"Display Name: {self.__name}")


def main():

    pet1 = Pet("Cat", "Tabby", "Luca, The Explorer")
    pet2 = Pet("Dog", "Chihuahua", "Paco, Master Barker")
    pet3 = Pet("Dog", "Pitbull", "Princess, Devourer of Kibble")

    pet1.print_details()
    pet2.print_details()
    pet3.print_details()
    print("Name of the class: ", Pet.__name__)
    print("Name of the module: ", Pet.__module__)
    print(Pet.__bases__)


main()
