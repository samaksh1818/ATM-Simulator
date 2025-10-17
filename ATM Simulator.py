pin = 1856

for attempt in  range(5):
    entered_pin = int(input("Enter your four digit pin: "))
    if entered_pin == pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
        print(f"Attempts left: {4 - attempt}")
else:
    print("Too many incorrect attempts! ATM locked")
    exit()


balance = 9000

while True:
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Your current balance is:",balance)
        case 2:
            amount = float(input("Enter amount to deposit: "))
            if amount >0:
                balance += amount
                print(f"{amount} deposited successfully!")
                print("updated balance:",balance)
            else:
                print("Deposit amount must be positive.")
        case 3:
            amount = float(input("Enter amount to withdraw: "))
            if balance >= amount > 0:
                balance -= amount
                print(f"{amount} withdrawn successfully!")
                print("updated balance:",balance)
            elif amount <= 0:
                print("Withdrawl amount must be positive.")
            else:
                print("Insufficient balance!")
        case 4:
            print("Thank you for using the ATM!")
            break
        case _:
            print("Invalid choice! Please try again.")