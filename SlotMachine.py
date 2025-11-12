import random 


#VARIABLES 
max_lines = 3 #amount of game lines in machine 
max_bet = 100
min_bet = 1

ROW = 3
COL = 3



#user input (money depsited in machine)
def deposit():
    while True:
        amount = input("What amount would you like to deposit?")
        if amount.isdigit():
            amount = int(amount) #convert string to int if true 
            if amount > 0:
                break
            else:
                print("amount must be greater than $0.00")
        #if amount is not a digit   
        else:
            print("Please enter an amount")
    return amount

#number of lines to bet on
def numberOfLines():
    while True:
        lines = input("Please enter amount of lines ypu'll bet on (1-"  + str(max_lines + ")?"))
        if lines.isdigit():
            lines = int(lines) #convert string to int if true 
            if 1<= lines <= max_lines:
                break
            else:
                print("amount must be greater than 0")
        #if amount is not a digit   
        else:
            print("Please enter an amount")
    return amount
    
    
#slot machine setup

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines(1-" + str(max_lines)+ ")" )
        if lines.isdigit():
            lines = int(lines) #convert string to int if true 
            if 1 <= lines <= max_lines:
                break
            else:
                print("enter valid number of lines")
        #if amount is not a digit   
        else:
            print("Please enter an amount")
    return lines
    
def get_bet():
    while True:
        amount = input("What amount would you like to bet?")
        if amount.isdigit():
            amount = int(amount) #convert string to int if true 
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"amount must be between {min_bet} - ${max_bet}")
        #if amount is not a digit   
        else:
            print("Please enter an amount")
    return amount
    

def main():
    balance = deposit() #starting balance after initial deposit 
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        
        if total_bet > balance:
            print(f"you do not enough to bet that amount, current balance is: ${balance}")
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    
    
    
    main()
