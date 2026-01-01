import datetime
import os
import time
import json

subs = []
DATA_FILE = "subscriptions.json"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_subscriptions():
    global subs
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            subs = []
            for sub in data:
                subs.append({
                    "name": sub["name"],
                    "amount": sub["amount"],
                    "date": datetime.datetime.strptime(sub["date"], "%d-%m-%Y")
                })

def save_subscriptions():
    with open(DATA_FILE, "w") as file:
        data = []
        for sub in subs:
            data.append({
                "name": sub["name"],
                "amount": sub["amount"],
                "date": sub["date"].strftime("%d-%m-%Y")
            })
        json.dump(data, file, indent=4)

def welcome_message():
    clear_screen()
    print("\033[1;32m")
    print("""
   _____                          _    
  |  __ \\                        | |   
  | |__) |_ _ _ __ ___   __ _ _ __| | __
  |  ___/ _` | '_ ` _ \\ / _` | '__| |/ /
  | |  | (_| | | | | | | (_| | |  |   < 
  |_|   \\__,_|_| |_| |_|\\__,_|_|  |_|\\_\\
    """)
    print("Welcome to Renewly - Your Subscription Manager!")
    print("\033[0m")

def login():
    welcome_message()
    input("Enter your name: ")
    input("Choose your password: ")
    print("\nWelcome to Renewly!\n")
    time.sleep(1)
    return True

def addsubs():
    clear_screen()
    print("\033[1;35mAdding a new subscription...\033[0m\n")
    name = input("Enter subscription name: ")
    amount = input("Enter subscription amount: ")
    while not amount.replace(".", "", 1).isdigit():
        print("Invalid amount.")
        amount = input("Enter subscription amount: ")
    date_str = input("Enter renewal date (DD-MM-YYYY): ")
    try:
        renewal_date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format.")
        time.sleep(1)
        return
    subs.append({
        "name": name,
        "amount": float(amount),
        "date": renewal_date
    })
    save_subscriptions()
    print("\nSubscription added successfully!")
    time.sleep(1)

def viewsubs():
    clear_screen()
    if not subs:
        print("No subscriptions found.")
        time.sleep(1)
        return
    print("\033[1;36mYour Subscriptions:\033[0m\n")

    sorted_subs = sorted(subs, key=lambda sub: sub["date"])

    for sub in sorted_subs:
        days_left = (sub["date"] - datetime.datetime.now()).days
        print(f"Name   : {sub['name']}")
        print(f"Amount : ${sub['amount']}")
        print(f"Renewal: {sub['date'].strftime('%d-%m-%Y')}")
        print(f"Days left: {days_left} days\n")
    input("Press Enter to return to menu...")

def updatesubs():
    clear_screen()
    name = input("Enter subscription name to update: ")
    for sub in subs:
        if sub["name"].lower() == name.lower():
            sub["name"] = input("New name: ")
            amount = input("New amount: ")
            while not amount.replace(".", "", 1).isdigit():
                print("Invalid amount.")
                amount = input("New amount: ")
            sub["amount"] = float(amount)
            date_str = input("New renewal date (DD-MM-YYYY): ")
            try:
                sub["date"] = datetime.datetime.strptime(date_str, "%d-%m-%Y")
            except ValueError:
                print("Invalid date.")
                time.sleep(1)
                return
            save_subscriptions()
            print("\nSubscription updated successfully!")
            time.sleep(1)
            return
    print("Subscription not found.")
    time.sleep(1)
def deletesubs():
    clear_screen()
    name = input("Enter subscription name to delete: ")
    for sub in subs:
        if sub["name"].lower() == name.lower():
            subs.remove(sub)
            save_subscriptions()
            print("\nSubscription deleted successfully!")
            time.sleep(1)
            return
    print("Subscription not found.")
    time.sleep(1)
def menu():
    while True:
        clear_screen()
        print("\033[1;32mChoose an option:\033[0m")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Update Subscription")
        print("4. Delete Subscription")
        print("5. Exit")
        choice = input("\nEnter choice: ")
        if choice == "1":
            addsubs()
        elif choice == "2":
            viewsubs()
        elif choice == "3":
            updatesubs()
        elif choice == "4":
            deletesubs()
        elif choice == "5":
            print("\nThank you for using Renewly!")
            break
        else:
            print("Invalid choice.")
            time.sleep(1)
if login():
    load_subscriptions()
    menu()