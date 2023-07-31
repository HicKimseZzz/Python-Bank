import info

print("\nWelcome To The Mrz Bank!\n")

while True:
    print("Please select a action:\n1 -> Create new acount\n2 -> Enter acount")
    choise = int(input("?: "))
    if choise == 1:
        pass
    elif choise == 2:
        while True:
            cartNameIn = input("Please write cart holders name: ")
            cartNumIn = int(input("Please write cart number: "))
            cartPassIn = int(input("Please write cart password: "))
            for crt in range(len(info.cartNames)):
                if crt <= (len(info.cartNames)-1):
                    if info.cartNum[crt] == cartNumIn and info.cartNames[crt] == cartNameIn and info.cartPass[crt] == cartPassIn:
                        print("bus" + str(info.cartMoney[crt]))
                        print("\nPlease select an option: \n")
                        print("1 -> Withdraw\n2 -> Deposit\n3 -> Other Currencys\n 4 -x`> Exit")
                        x = input("wait")
                if crt + 1 == len(info.cartNames):    
                    print("wait") 
    else:
        print("Error.Please try again")
