#################################################

Cars = [["Lamborghini", 1000000, 2, 40000],
["Ferrari", 1500000, 2.5, 50000],
["BMW", 800000, 1.5, 20000]]

#################################################

print("#"*80)
print("#" + "Welcome to XYZ Car Dealership".center(78) + "#")
print("#"*80 + "\n")

while True:
    print("#"*80)
    print("#" + "What Would You Like To Do Today?".center(78) + "#")
    print("#" + "A) Buy A Car ".center(78) + "#")
    print("#" + "B) Rent A Car".center(78) + "#")
    print("#"*80 + "\n")

    mode = input("Choose Option (A/B):\t").lower()
    while mode not in "ab" and mode != "ab":
        mode = input("Choose Option (A/B):\t").lower()

    if mode == "a":
        print("#"*80)
        print("#" + "Choose A Car".center(78) + "#")
        print("#" + "1) Lamborghini       ".center(78) + "#")
        print("#" + "2) Ferrari           ".center(78) + "#")
        print("#" + "3) BMW               ".center(78) + "#")
        print("#" + "4) Input Your own Car".center(78) + "#")
        print("#"*80)

        op = int(input("Choose Option: "))
        while op != 1 and op != 2 and op != 3 and op != 4:
            op = int(input("Choose Option: "))

        if op == 4:
            buyPrice = int(input("Enter Buy Price of Car: "))
            maintainanceCostPercentage = int(input("Enter Annual Maintainance Percentage of Car: "))
            years = int(input("How many Years: "))

        else:
            i = op-1
            print("Checking for " + Cars[i][0] + "...")
            years = int(input("How many Years: "))
            buyPrice = Cars[i][1]
            maintainanceCostPercentage = Cars[i][2]

        Price = buyPrice + buyPrice * (years-1) * maintainanceCostPercentage / 100
        p = "Buy For $" + str(Price)
        print("\n" + "#"*80)
        print("#" + "Receipt".center(78) + "#")
        print("#" + "-------".center(78) + "#")
        print("#" + "".center(78) + "#")
        print("#" + p.center(78) + "#")
        print("#"*80)


    elif mode == "b":
        print("#"*80)
        print("#" + "Choose A Car".center(78) + "#")
        print("#" + "1) Lamborghini       ".center(78) + "#")
        print("#" + "2) Ferrari           ".center(78) + "#")
        print("#" + "3) BMW               ".center(78) + "#")
        print("#" + "4) Input Your own Car".center(78) + "#")
        print("#"*80)

        op = int(input("Choose Option: "))
        while op != 1 and op != 2 and op != 3 and op != 4:
            op = int(input("Choose Option: "))

        if op == 4:
            rent = int(input("Enter monthly Rental Price of Car: "))
            months = int(input("How many Months: "))

        else:
            i = op-1
            months = int(input("How many Months: "))
            rent = Cars[i][3]

        Price = months * rent      
        p = "\n\nPrice to rent for " + str(months) + " months is $" + str(Price)
        print("\n" + "#"*80)
        print("#" + "Receipt".center(78) + "#")
        print("#" + "-------".center(78) + "#")
        print("#" + "".center(78) + "#")
        print("#" + p.center(78) + "#")
        print("#"*80)

    if input("Would You like to Exit? (y/n) ").lower() == "y": 
        break

print("#"*80)
print("#" + "Thank You!".center(78) + "#")
print("#"*80)