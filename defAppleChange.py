#This program will ask the user the amount of money
#and the current price of apples
#The program will calculate the maximum number of 
#how many apples the use can buy and compute the change

#Step1 Ask the amount of money the user have
def askMoney():
    money = input("How much money do you have?: ")
    money = int(money)
    return money

userMoney = askMoney()
print(userMoney)