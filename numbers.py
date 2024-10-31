# 1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
length = 92
wide = 48.8
total_area = length*wide
print(round(total_area, 2))

# 2.You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
def backMoney(boughtPack, singleCost, givingAmount):
    total_price = boughtPack*singleCost
    result = givingAmount - total_price
    print('Shopeeper give me', result, 'doller')

backMoney(9, 1.49, 20)

# 3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
def totalCost(length, tilesCost):
    square_area = pow(length, 2)
    result = square_area*500
    print(result)

totalCost(5.5, 500)
# 4.Print binary representation of number 17
number = 17
binary_representation = bin(number)
print(binary_representation)