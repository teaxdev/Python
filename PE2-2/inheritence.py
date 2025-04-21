# PE2 3.5.1.1 OOP Inheritance
# Creating and using a Dog SuperClass 🐕
# and a HerdingDog subclass 🐏🐏🐏
# along with instantiating (making objects)

class Employee:

    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    def get_employee_name(self):
        return self.employee_name

    def get_employee_number(self):
        return self.employee_number


class ProductionWorker(Employee):

    def __init__(self, employee_name, employee_number, shift_number, pay_rate):
        super().__init__(employee_name, employee_number)
        self.shift_number = shift_number
        self.pay_rate = pay_rate

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate

    def get_shift_number(self):
        return self.shift_number

    def get_pay_rate(self):
        return self.pay_rate

    def get_info(self):
        return (
            f"Name: {self.employee_name}, Employee ID: {self.employee_number}, Shift: {self.shift_number}, Pay rate: {self.pay_rate}")


JamesBond = ProductionWorker("James Bond", "007", "1", "18.50")

print(JamesBond.get_info())


def main():
    print("\nPlease enter your credentials in their respective fields: ")
    your_name = input("Enter your full name: ")
    your_id = input("Enter your ID: ")
    your_shift = input(
        "Enter your shift number (1 for morning, 2 for afternoon): ")
    your_pay = input("Enter pay rate (ex. 18.00): ")

    your_info = ProductionWorker(your_name, your_id, your_shift, your_pay)
    print(f"Here's your info: \n{your_info.get_info()}")


main()
