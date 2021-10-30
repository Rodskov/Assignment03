#This program will ask the user the amount of money
#     and the current price of apples
#     The program will calculate the maximum number of 
#     how many apples the use can buy and compute the change

#Step1 Ask the amount of money the user have
def askMoney():
    money = input("How much money do you have?: ")
    money = int(money)
    return money

#Step2 Ask the current price of apples
def askApplePrice():
    applePrice = input("What is the current cost of apples?: ")
    applePrice = int(applePrice)
    return applePrice

#Step3 Calculate the maximum number of apples the money can buy
def maxApples():
    maxNumber = userMoney//applePrice
    return maxNumber

#Step4 Calculate the change
def moneyChange():
    change = userMoney%applePrice
    return change

userMoney = askMoney()
applePrice = askApplePrice()
maxBuy = maxApples()
appleChange = moneyChange()