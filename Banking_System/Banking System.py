class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)
    
    def displayInfo(self):
        # TO COMPLETE
        print("name: "+ self.first_name)
        print("last_name: "+self.last_name)
        print("gender: "+self.gender)
        print("street_address: "+ self.street_address)
        print("city: "+ self.city)
        print("email: "+self.email)
        print("cc_number: "+ self.cc_number)
        print("cc_type: "+ self.cc_type)
        print(f"balance: {self.balance}")
        print("self.account_no"+self.account_no)
        print("=================================")
        
def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8][1:]), line[9])

def findUser():
    #TO COMPLETE
    user1 = False
    user_name = input("What is the user name ? ").title()
    for user in userList:
        if user_name in user.first_name or user_name in user.last_name:
            user.displayInfo()
            user1 = True

    if not user1:
        print("There is no user with that name")

    
def overdrafts():
    # TO COMPLETE
    count_overdraft = 0
    value_total_overdraft = 0.0
    for user in userList:
        user.displayInfo()
        count_overdraft+=1
        value_total_overdraft += float(user.balance)
        print(f"The total number of customer with overdrafts is"
              f"is {count_overdraft}\n The total value of those overdraft is "
              f"{round(value_total_overdraft,2)}")
def missingEmails():
    # TO COMPLETE
    count_missing_email = 0
    for user in userList:
        if not user.email:
            user.displayInfo()
            count_missing_email += 1
    print(f"\n The total number of custtomer with missing email address is "
          f"{count_missing_email}")


def bankDetails():
    # TO COMPLETE

    count_user = 0
    total_worth = 0
    highest_balance = ["",0]
    lowest_balance = ["",0]
    for user in userList:
        name = user.first_name + " " + user.last_name
        count_user+=1
        total_worth+=user.balance
        if user.balance<lowest_balance[1]:
            lowest_balance = [name,user.balance]
        elif user.balance == lowest_balance[1]:
            lowest_balance.append([name,user.balance])
        elif user.balance > highest_balance[1]:
            highest_balance = [name,user.balance]
        elif user.balance == highest_balance[1]:
            highest_balance.append([name,user.balance])
        print(f"Total user:{count_user}\n"
              f"AUM:{round(total_worth,2)}\n"
              f"Highest balance user:{highest_balance[0]} "
              f"with ${highest_balance[1]}\n"
              f"Lowest balance user : {lowest_balance[0]}"
              f"with {lowest_balance[1]} ")

def transfer():
    # TO COMPLETE
    global withdraw_user
    withdraw_account = input("Account number :")
    for user in userList:
        if user.account_no == withdraw_account:
            withdraw_user = user
            print(f"\nUser is: {withdraw_user.first_name}"
                  f"{withdraw_user.last_name}\n"
                  f"Account No: {withdraw_user.account_no}"
                  f"\n Balance ${withdraw_user.balance}")
    transfer_amount = int(input("\n How much do you want to transfer"))
    deposit_account = input("\n Enter the account number you want to "
                            "transfer money to: ")
    for user in userList:
        if user.account_no == deposit_account:
            deposit_user = user
            confirm = input(f"\nConfirm that {transfer_amount}"
                            f"will be transfer to {deposit_user.first_name}"
                            f"{deposit_user.last_name}\n"
                            f"Press Enter to confirm or any other key and"
                            f"Enter to return to the menu")
            if not confirm:
                withdraw_user.balance -= transfer_amount
                deposit_user.balance += transfer_amount
                print(f"${transfer_amount} has just been transfered"
                      f"from{withdraw_user.first_name} {withdraw_user.last_name}"
                      f"leaving a new balance of $"
                      f"{withdraw_user.balance}\n"
                      f"to {deposit_user.first_name} {deposit_user.last_name}"
                      f"leaving a new balance of ${deposit_user.balance}")
userList = []          
generateUsers()
for user in userList:
    user.displayInfo()
userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()
    
    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()      
    print()
