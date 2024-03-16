from src.domain.ComplexNumber import ComplexNumber
from src.services.Service import Service

class UI:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            print("1. Add a complex number")
            print("2. Display the list of complex numbers")
            print("3. Filter the list of complex numbers")
            print("4. Undo")
            print("5. Exit")
            option = input("Enter your option: ")
            if option == "1":
                try:
                    real = int(input("Enter the real part: "))
                    imaginary = int(input("Enter the imaginary part: "))
                    complex_nr = ComplexNumber(real, imaginary)
                    self.service.add(complex_nr)
                except ValueError as ve:
                    print(ve)
            elif option == "2":
                print("Numbers:", end=" ")
                self.print_list(self.service.get_all())
                print()
            elif option == "3":
                try:
                    start = int(input("Enter the start index: "))
                    end = int(input("Enter the end index: "))
                    self.service.filter(start, end)
                except ValueError as ve:
                    print(ve)
            elif option == "4":
                try:
                    self.service.undo()
                except ValueError as ve:
                    print(ve)
            elif option == "5":
                self.service.save_changes()
                return
            else:
                print("Invalid option!")

    def print_list(self, list):
        for element in list:
            print(element, end=" ")

