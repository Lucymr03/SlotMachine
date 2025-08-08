#VARIABLES 
max_lines = 3 #amount of game lines in machine 

#user input (money depsited in machine)
def deposit():
    while True:
        amount = input("How much would you like to deposit?")
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
    
#slot machine setup



def main():
    balance = deposit() #starting balance after initial deposit 
