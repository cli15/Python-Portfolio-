#Christina and Isa
#Slot Machine
#Making a slot machine

import random
def game ():
    credits = 0
    balance = 0
    credits = int(input("How much credits would you like to load into your account? (20,50,100)? "))
    balance =  credits + balance
    while True:
        print(f"You have {balance} credits.")
        resp = input("Would you like to play the slot machine for 10 credits? ").lower().strip()
        if resp == "yes":
            if balance >= 10:
                hearts = [ "💖", "💖", "💗","💗","💝","💝","7"]
                play1 = random.choice(hearts)
                print(play1)
                play2 = random.choice(hearts)
                print(play2)
                play3 = random.choice(hearts)
                print(play3)
                if play1 == "7" and play2 == "7" and play3 == "7":
                    print("Jackpot!")
                    balance = balance - 10
                    payout = input("Would you like to add 500 credits or cash out $250? (credits/cash) ").lower().strip()
                    if payout == "credits":
                        balance = balance + 500
                    elif payout == "cash":
                        print("$250 has been added to your account.")
                        break
                    else:
                          print("Invalid input.")
                elif play1 == play2 and play2 == play3:
                    balance = balance - 10
                    print("You Win!")
                    payout = input("Would you like to add 100 credits or cash out $50? (credits/cash) ").lower().strip()
                    if payout == "credits":
                        balance = balance + 100
                    elif payout == "cash":
                        print("$50 has been added to your account.")
                        break
                    else:
                          print("Invalid input.")

                else:
                    print("Better luck next time.")
                    balance = balance - 10
            elif balance == 10:
                hearts = [ "💖", "💖", "💗","💗","💝","💝","7"]
                play1 = random.choice(hearts)
                print(play1)
                play2 = random.choice(hearts)
                print(play2)
                play3 = random.choice(hearts)
                print(play3)
                if play1 == "7" and play2 == "7" and play3 == "7":
                    print("Jackpot!")
                    balance = balance - 10
                    payout = input("Would you like to add 500 credits or cash out $250? (credits/cash) ").lower().strip()
                    if payout == "credits":
                        balance = balance + 500
                    elif payout == "cash":
                        print("$250 has been added to your account.")
                        break
                    else:
                        print("Invalid input.")
                elif play1 == play2 and play2 == play3:
                    balance = balance - 10
                    print("You Win!")
                    payout = input("Would you like to add 100 credits or cash out $50? (credits/cash) ").lower().strip()
                    if payout == "credits":
                        balance = balance + 100
                    elif payout == "cash":
                        print("$50 has been added to your account.")
                        break
                    else:
                          print("Invalid input.")
                          balance = balance - 10
                else:
                    print("Better luck next time.")
                    balance = balance - 10

            else:
                status = input("INSUFFICIENT FUNDS. Please insert credits to play again or quit. (insert credits/quit) ").lower ()
                if status == "insert credits":
                    credits = int(input("How many credits would you like to load into your account? (20,50,100)? "))
                    balance = balance + credits
                else:
                    break
        elif resp == "no":
            break
        else:
            print("Invalid, try again.")

def simulation():
    balance= 10000
    for i in range (1000):
        hearts = [ "💖","💖", "💗","💗", "💝","💝","7"]
        play1 = random.choice(hearts)
        print(play1)
        play2 = random.choice(hearts)
        print(play2)
        play3 = random.choice(hearts)
        print(play3)
        if play1 == "7" and play2 == "7" and play3 == "7":
            print("Jackpot!")
            balance = balance - 10
            balance = balance + 500
        elif play1 == play2 and play2 == play3:
            print("You Win!")
            balance = balance - 10
            balance = balance + 100
        else:
            print("Better luck next time.")
            balance = balance - 10
    print(f"Casino profit: {10000-balance}.")






#main
game ()
