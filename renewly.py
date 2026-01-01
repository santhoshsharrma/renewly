import datetime
import os
import time
subs=[]
def clear_screen():
    os.system('cls' if os.name=='nt'else'clear')
def welcome_message():
    clear_screen()
    print("\033[1;32;40m" + """ 
   _____                          _    
  |  __ \                        | |   
  | |__) |_ _ _ __ ___   __ _ _ __| | __
  |  ___/ _` | '_ ` _ \ / _` | '__| |/ /
  | |  | (_| | | | | | | (_| | |  |   < 
  |_|   \__,_|_| |_| |_|\__,_|_|  |_|\_\\
    "Welcome to Renewly - Your Subscription Manager!"\
    """ + "\033[0m")
    print("\033[1;33m"+"Manage your subscriptions easily and efficiently!\n"+"\033[0m")
def login():
    welcome_message()
    username=input("Enter your name: ")
    password=input("Choose your Password: ")
    print(f"\033[1;34mWelcome to Renewly,{username}!!\n\033[0m")
    return True
def addsubs():
    clear_screen()
    print("\033[1;35m"+"Adding a new subscription..."+"\033[0m")
    name=input("Enter the subscription name: ")
    amount=input("Enter the subscription amount: ")
    while not amount.replace('.', '', 1).isdigit():
        print("\033[1;31mInvalid amount. Please enter a valid number.\033[0m")
        amount=input("Enter the subscription amount: ")
    date_str=input("Enter the renewal date for your subscription (DD-MM-YYYY): ")
    try:
        renewal_date=datetime.datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("\033[1;31mInvalid date format. Please enter date in DD-MM-YYYY format.\033[0m")
        return
    subs.append({
        "name":name,
        "amount":float(amount),
        "date":renewal_date
    })
    print("\033[1;32mSubscription added successfully!\n\033[0m")
    time.sleep(1)
def viewsubs():
    clear_screen()
    if not subs:
        print("\033[1;33mNo subscriptions found. Add them into your Renewly List.\n\033[0m")
        return
    print("\033[1;36mYour Subscriptions are: \033[0m")
    for sub in subs:
        days_until_renewal = (sub['date'] - datetime.datetime.now()).days
        print(f"\033[1;34mSubscription Name:\033[0m {sub['name']}")
        print(f"\033[1;34mSubscription Amount:\033[0m ${sub['amount']}")
        print(f"\033[1;34mUpcoming Renewal Date:\033[0m {sub['date'].strftime('%d-%m-%Y')}")
        print(f"\033[1;32mDays until renewal: {days_until_renewal} days\033[0m\n")
    print("\033[1;35mYou’re all set!\033[0m")
    time.sleep(2)
def updatesubs():
    clear_screen()
    print("\033[1;36mUpdating a subscription...\033[0m")
    name = input("Enter your subscription name to update: ")
    for sub in subs:
        if sub["name"].lower()==name.lower():
            sub["name"]=input("Enter new subscription name: ")
            sub["amount"]=input("Enter new amount: ")
            while not sub["amount"].replace('.', '', 1).isdigit():
                print("\033[1;31mInvalid amount. Please enter a valid number.\033[0m")
                sub["amount"]=input("Enter new amount: ")
            date_str=input("Enter new renewal date (DD-MM-YYYY): ")
            try:
                sub["date"]=datetime.datetime.strptime(date_str, "%d-%m-%Y")
            except ValueError:
                print("\033[1;31mInvalid date format. Please enter date in given format.\033[0m")
                return
            print("\033[1;32mSubscription updated successfully!\n\033[0m")
            time.sleep(1)
            return
    print("\033[1;31mSubscription not found.\n\033[0m")
    time.sleep(1)
def deletesubs():
    clear_screen()
    print("\033[1;33mDeleting a subscription...\033[0m")
    name = input("Enter subscription name to delete: ")
    for sub in subs:
        if sub["name"].lower()==name.lower():
            sub.remove(sub)
            print("\033[1;31mSubscription deleted successfully!\n\033[0m")
            time.sleep(1)
            return
    print("\033[1;31mSubscription not found.\n\033[0m")
    time.sleep(1)
def menu():
    while True:
        clear_screen()
        print("\033[1;32m Please choose an option:\033[0m")
        print("\033[1;34m 1. Add a Subscription\033[0m")
        print("\033[1;34m 2. View Your Subscriptions\033[0m")
        print("\033[1;34m 3. Update Your Subscription\033[0m")
        print("\033[1;34m 4. Delete Your Subscription\033[0m")
        print("\033[1;35m 5. Exit\033[0m")
        choice=input("\033[1;33m Enter your choice: \033[0m")
        if choice=="1":
            addsubs()
        elif choice=="2":
            viewsubs()
        elif choice=="3":
            updatesubs()
        elif choice=="4":
            deletesubs()
        elif choice=="5":
            print("\033[1;32mThank you for using Renewly! See you soon :) \033[0m")
            break
        else:
            print("\033[1;31mInvalid choice. Please try again.\033[0m")
            time.sleep(1)
if login():
    menu()


