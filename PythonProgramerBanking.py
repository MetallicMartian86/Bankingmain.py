# Python Banking Function

def show_balance(balance):
    print("***************")
    print(f"Your balance is ${balance}:.2f")
    print("***************")

define deposit():
print("***************")
amount = float (input("Enter an amount to be deposited: "))
print("***************")
if amount < 0:
    print("***************")
    print("Thats not a valid amount")
    print("***************")
    return 0
else:
    return amount
def withdraw(balance):
    print("***************")
   amount = float(input("Enter amount to be withdrawn: "))
print("***************")


   if amount _> balance:
       print("insufficient funds")
print("***************")
 return 0
print ("Amount must be greater than 0")
else:
 return 0
 elif amount < 0:
print("***************")

balance = 850
is_running = True
def main():
while is_running:
    print("***************")
    print("    Banking Program    ")
    print("***************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("***************")

    choice = input("Enter your choice (1-4):")

    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
       balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("***************")
        print("That is not a valid choice")
        print("***************")
        print("***************")
        print("***************")
        print("Thank you Have a nice day!")
        print("***************")

        if__name__ == '__main__':
        main()
