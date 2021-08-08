sum = 0
while (True):
    userInput = input("Enter the price of item or press h to quit: \n")
    if (userInput != 'h'):
        sum = sum + int(userInput)
        print(f"order total so far: {sum}")

    else:
        print(f"your bill total is {sum}. welcome again")
        break
