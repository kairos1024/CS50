price = 50
# Loop until price is greater than 0
while price > 0:
    print(f"Amount Due: {price}")
    coins = input("Insert Coin: ")
    #Check if coin is equal to 25, 10, or 5 cents
    if coins == "25" or coins == "10" or coins == "5":
        coins = int(coins)
        price = price - coins
    else:
        print("Amount Due: 50")
        break
# Calculate change
if price == 0:
    print("Change Owed: 0")
elif price < 0:
    change = (-price)
    print(f"Change Owed: {change}")
else:
    print()