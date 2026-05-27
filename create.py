#Beverage Finder
#Program allows for the user to find a beverage that caters to their dietary needs

import pandas as pd
import webbrowser
import random

data = pd.read_csv("beverages.csv")
name = data["Name"].tolist()
type = data["Type"].tolist()
sugarfree = data["Sugar Free?"].tolist()
calories = data["Calories"].tolist()
fats = data["Fat (g)"].tolist()
protein = data["Protein (g)"].tolist()
caffeine = data["Caffeine (mg)"].tolist()
filter = []

#Use parameters: "Juice, Milk, Water, Coffee, Tea, Soda, or Energy Drink"
def beverage (keyword):
        while True:
            print(" ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
            print("Hi, welcome to |-{BEVERAGE FINDER}-| !")
            print("Having dietary restrictions can be hard, but that's why we are here to help you!")
            print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
            user = input("Would you like to find your perfect beverage? |yes| |no| ").lower().strip()
            if user == "yes":
                print("")
                print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                print("What nutrition fact would you like to adjust?")
                print("")

            #User can pick one to change
                print("|sugar| |calories| |fats| |protein| |caffeine|")
                print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                change = input("choice: ").lower().strip()

            #Sugar
                if change == "sugar":
                    sugartype = input("Do you prefer sugarfree or normalsugar? ").strip().lower()
                    if sugartype == "sugarfree":
                        for i in range (len(type)):
                            if keyword in type[i] and sugarfree[i] == True:
                                filter.append(name[i])
                        if not filter:
                            print("...unvalid...")
                            again = input("try again? |yes| |no| ").lower().strip()
                            if again == "yes":
                                continue
                            else:
                                break
                        print(filter)
                        filter.clear()
                        print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                        retry = input("retry? |yes| |no| ")
                        if retry == "yes":
                            continue
                        elif retry == "no":
                            break
                        else:
                            print("...?")
                            break
                    elif sugartype == "normalsugar":
                        for i in range (len(type)):
                            if keyword in type[i] and sugarfree[i] == False:
                                print(filter)
                                filter.append(name[i])
                                sugargrams = float(input("Under how many grams of sugar? ")).strip()
                        if sugargrams <= sugars[i]:
                            filter.append(name[i])
                        if not filter:
                            print("...unvalid...")
                            again = input("try again? |yes| |no| ").lower().strip()
                            if again == "yes":
                                continue
                            else:
                                break
                        print(filter)
                        filter.clear()
                        print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                        retry = input("retry? |yes| |no| ")
                        if retry == "yes":
                            continue
                        elif retry == "no":
                            break
                        else:
                            print("...?")
                            break
                    else:
                        print("...invalid.")
                        break

                #Calories
                #Input MUST be number => 0
                elif change == "calories":
                    cals = input("Under how many calories? ").strip()
                    for i in range (len(calories)):
                        if keyword in type[i] and int(cals) >= int(calories[i]):
                            filter.append(name[i])
                    if not filter:
                        print("...unvalid...")
                        again = input("try again? |yes| |no| ").lower().strip()
                        if again == "yes":
                            continue
                        else:
                            break
                    print(filter)
                    filter.clear()
                    print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                    retry = input("retry? |yes| |no| ")
                    if retry == "yes":
                        continue
                    elif retry == "no":
                        break
                    else:
                        print("...?")
                        break

                #Fats
                #Input MUST be number > 0
                elif change == "fats":
                    fat = input("Under how many grams of fats? ").strip()
                    for i in range (len(fats)):
                        if keyword in type[i] and int(fat) > int(fats[i]):
                            filter.append(name[i])
                #Code used to cut down output if filter is too large
                    one = random.choice(filter)
                    filter.remove(one)
                    two = random.choice(filter)
                    filter.remove(two)
                    three = random.choice(filter)
                    filter.remove(three)
                    four = random.choice(filter)
                    filter.remove(four)
                    five = random.choice(filter)
                    filter.remove(five)
                    print(f" Your options are: {one}, {two}, {three}, {four}, {five} " )
                    if filter == "[]":
                        print("...unvalid...")
                        again = input("try again? |yes| |no| ").lower().strip()
                        if again == "yes":
                            continue
                        else:
                            break

                    filter.clear()
                    print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                    retry = input("retry? |yes| |no| ")
                    if retry == "yes":
                        continue
                    elif retry == "no":
                        break
                    else:
                        print("...?")
                        break

                #Protein
                #Input MUST be number => 0
                elif change == "protein":
                    pro = input("More than how many grams of protein? ")
                    for i in range (len(name)):
                        if keyword in type[i] and float(pro) < float(protein[i]):
                            filter.append(name[i])
                    if not filter:
                            print(f" {pro} not found in list, try numbers less than 5.")
                            again = input("try again? |yes| |no| ").lower().strip()
                            if again == "yes":
                                continue
                            else:
                                break
                    print(filter)
                    filter.clear()
                    print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                    retry = input("retry? |yes| |no| ")
                    if retry == "yes":
                        continue
                    elif retry == "no":
                        break
                    else:
                        print("...?")
                        break
                #Caffeine
                #Input MUST be number => 0
                elif change == "caffeine":
                    caf = input("Under how many grams of caffeine? ")
                    for i in range (len(name)):
                        if keyword in type[i] and int(caf) > int(caffeine[i]):
                            filter.append(name[i])
                #Code used to cut down output if filter is too large
                    one = random.choice(filter)
                    filter.remove(one)
                    two = random.choice(filter)
                    filter.remove(two)
                    three = random.choice(filter)
                    filter.remove(three)
                    four = random.choice(filter)
                    filter.remove(four)
                    five = random.choice(filter)
                    filter.remove(five)
                    print(f" Your options are: {one}, {two}, {three}, {four}, {five} " )
                    if not filter:
                        print("...unvalid...")
                        again = input("try again? |yes| |no| ").lower().strip()
                        if again == "yes":
                            continue
                        else:
                            break
                    filter.clear()
                    print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                    retry = input("retry? |yes| |no| ")
                    if retry == "yes":
                        continue
                    elif retry == "no":
                        break
                    else:
                        print("...?")
                        break
                else:
                    print("")
                    print("[ not a choice ]")
                    print("")
                    break
            else:
                print("~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~")
                print("Welp, we hope to see you in the future! Have a great day!")
                break

#Sources:
#Data Set shared by CODE.org

#Data Set Info:
#USDA Food Data Central
#Link: https://fdc.nal.usda.gov/ (April 2020 Download)

#I learned the "if not" function (line 143) from:
#Better Stack
#Link: https://tinyurl.com/5zmnx2tr (2023)


#Main
beverage("Coffee")


