# 3.3 OOP Properties

class Pet:

    vet_name = "United Paws Veterinary Care"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    def display_pet_info(self):
        # print("Pet and owner details:", vars(self))
        print(f"\n\nDisplay Owner Name: {self.__owner_first_name}")
        print(f"Display Owner Last Name: {self.__owner_last_name}")
        print(f"Display Pet ID: {self.__pet_id}")
        print(f"Display Pet Name: {self.__pet_name}")
        print(f"Display Pet Type: {self.__pet_type}")

    print(f"Your veterinary: {vet_name}\n")


def check_property(obj, property_name):
    print(f"Has a {property_name} method: ", hasattr(obj, property_name))


def main():

    owner1 = Pet("James", "Smith", "12345", "Milo")
    owner2 = Pet("Sam", "Mitchell", "12344", "Lana", "Cat")
    owner3 = Pet("Gavin", "Harders", "54321", "Covey")

    check_property(owner1, "_Pet__owner_first_name")
    check_property(owner2, "_Pet__owner_last_name")
    check_property(owner3, "_Pet__pet_id")

    owner1.display_pet_info()
    owner2.display_pet_info()
    owner3.display_pet_info()


main()
