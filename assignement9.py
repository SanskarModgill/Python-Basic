# Case Study 1 
# Automated Vending Machinbe simulation
# In this code we get to see about how can we run a vending machine which is selling 3 items. We put here different cases for insufficient money, more money, less money and exit.
# Using while, if and else we wrote a code.


item_a = 2
item_b = 3
item_c = 5
 
while True:
    item_a == "1. Item A"
    item_b == "2. Item B"
    item_c == "3. Item C"
    exit == "4. Exit"
    user_choice = input("Enter the task: ")
 
    if user_choice == "1":
        insert_money = int(input("Enter the money: "))
        if insert_money > item_a :
        
            change = insert_money - item_a
            print(f"Dispensing item A. Your change is {change}.")
        if insert_money == item_a:
            print("Dispensing item A. Your change is 0.")
        else :
            print("Insuffcient money")   
            more_money = int(input("Insert more money: "))
            total_money = insert_money + more_money
            if total_money == item_a:
                print("Dispensing item A. Your change is 0.")
            if total_money > item_a:
                change1 = insert_money + more_money - item_a
                print(f"Dispensing item A. Your change is {change1}.")
         
    
    if user_choice == "2":
        insert_money = int(input("Enter the money: "))
        if insert_money > item_b:
            change = insert_money - item_b
            print(f"Dispensing item B. Your change is {change}.")
        if insert_money == item_b:
            print("Dispensing item B. Your change is 0.")
        if insert_money < item_b:
            print("Insufficient balance.")
            more_money = int(input("Insert more money: "))
            total_money = insert_money + more_money
            if total_money == item_b:
                print("Dispensing item B. Your change is 0.")
            if total_money > item_b:
                change1 = insert_money + more_money - item_b
                print(f"Dispensing item B. Your change is {change1}.")
         
 
    if user_choice == "3":
        insert_money = int(input("Enter the money: "))
        if insert_money > item_c:
            change = insert_money - item_c
            print(f"Dispensing item C. Your change is {change}.")
        if insert_money == item_c:
            print("Dispensing item C. Your change is 0.")
        if insert_money < item_c:
            print("Insufficient balance.")
            more_money = int(input("Insert more money: "))
            total_money = insert_money + more_money
            if total_money == item_c:
                print("Dispensing item C. Your change is 0.")
            if total_money > item_c:
                change1 = insert_money + more_money - item_c
 
                print(f"Dispensing item C. Your change is {change1}.")
 
 
    if user_choice == "4":
        break   







# This simulation is regarding a ATM machine where a user is accessing ATM machine for different tasks like withdrawal, deposit, checking balance etc.

import time as t
balance = 500
while True:
    t.sleep(2)
    print("Welcome to xyz Bank")
    print("1. Check Balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit ")

    t.sleep(1)
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your Current bank balance is ${balance}. ")
    elif choice == "2":
        withdrawal_amount = float(input("Enter the withdrawal amount. "))
        if withdrawal_amount < balance:
            new_balance = balance - withdrawal_amount
            print(f"${withdrawal_amount} has been withdrawn. Your new balance is ${new_balance}")
        if withdrawal_amount == balance:
            print(f"${withdrawal_amount} has been withdrawn. Your new balance us $0")
        if withdrawal_amount > balance:
            print("Insufficient Balance. Please enter a lesser amount. ")
    
    elif choice == "3":
        deposit_money = float(input("Enter the money to deposit: "))
        new_balance = balance + deposit_money
        print(f"${deposit_money} has been deposited. Your new balance is ${new_balance}.")

    elif choice == "4":
        print("Thank you for using our ATM. Goodbye! ")
   