#This program will ask how many apples and oranges the user will buy
#Then the program will compute how much the total amount is

#Step1 Ask how many apples the user wants to buy
#and compute the cost
applePrice = 20
def applesToBuy():
    apples = input("How many apples do you want to buy?: ")
    appleCost = int(apples) * applePrice 
    return appleCost 
appleCost = applesToBuy()

#Step2 Ask how many oranges the user wants to buy
#and compute the cost
orangePrice = 25
def orangesToBuy():
    oranges = input("How many oranges do you want to buy?: ")
    orangeCost = int(oranges) * orangePrice 
    return orangeCost 
orangeCost = orangesToBuy()

print(appleCost)
print(orangeCost)
#Step3 Compute the total cost of apples and oranges
