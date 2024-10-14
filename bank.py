balance = 10000.00

def check_balance():
    print(f"Your currant balance is = {balance}")

def deposit():
    depo_ammount = float(input("How much do you want to deposit = "))
    balance += depo_ammount
    print(f"Deposited ammount {depo_ammount} successfull.\nNew balance is = {balance}")

def withdraw():
    if wi_balance > balance:
        print("Insufficient ammount, please recharge your account.")
    else:
        wi_balance = float(input("How much do you want to withdraw : "))
        balance -= wi_balance
        print(f"Withdraw ammount {wi_balance} successfull, new balance is = {balance}")

print("Welcome to XYZ Bank Limited. Please enter username and password to login.")

username = input("Username : ")
password = input("Password : ")

if username == "junaid" and password == "123qaz" :
    print("Welcome to XYZBL online portal")

    while True:
        print("Please enter number to aquire service :")
        print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
        choice = int(input("Choice : "))

        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            deposit()
        elif choice == 4:
            break
        else:
            print("Wrong input. Please enter valid number.")

print("Thanks for being with us.\nHope to see you again soon.\nHave a good day.")