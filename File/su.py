class Atm:
    def __init__(self):
        print(f"Object created at memory address: {id(self)}")
        self.pin = ''
        self.balance = 0
        self.menu()  # Automatically start the menu when object is created

    def menu(self):
        user_input = input(
            "\n--- ATM Menu ---\n"
            "Press 1 to create Pin \n"
            "Press 2 to change pin \n"
            "Press 3 to check balance \n"
            "Press 4 to withdraw \n"
            "Anything else to Exit \n"
            "Selection: "
        )
        if user_input == "1":
            self.createPin()
        elif user_input == "2":
            self.changePin()
        elif user_input == "3":
            self.checkBalance()
        elif user_input == "4":
            self.withdrawBalance()
        else:
            print("Thank you for using the ATM. Goodbye!")
            return  # Clean exit from the menu loop

    def createPin(self):
        user_pin = input("Enter Pin: ")
        self.pin = user_pin
        user_balance = int(input("Enter initial balance: "))
        self.balance = user_balance
        print("Pin created Successfully!")
        self.menu()

    def changePin(self):
        old_pin = input("Enter Old pin: ")
        if old_pin == self.pin:
            newPin = input("Enter New Pin: ")
            self.pin = newPin
            print("Pin changed successfully!")
        else:
            print("Incorrect Old Pin!")
        self.menu()

    def checkBalance(self):
        user_pin = input("Enter Pin: ")
        if user_pin == self.pin:
            print("Balance is:", self.balance)
        else:
            print("Invalid Pin!")
        self.menu()

    def withdrawBalance(self):
        user_pin = input("Enter Pin: ")
        if user_pin == self.pin:
            useramt = int(input("Enter amount to withdraw: "))
            if useramt <= self.balance:
                self.balance -= useramt
                print("Amount Debited:", useramt)
                print("Remaining Balance:", self.balance)
            else:
                print("Insufficient Balance!")
        else:
            print("Invalid Pin!")
        self.menu()
a1=Atm()
a1.createPin()
a1.balance="hehehe"