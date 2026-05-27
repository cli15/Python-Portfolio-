#Christina
#Dog Recommendations
#Learning to give credit to sources + giving dog reccomendation based on user input

import webbrowser

url = ["https://tinyurl.com/4pvh8275", #Golden Retriever
       "https://tinyurl.com/329fw9bb", #Husky
       "https://tinyurl.com/bdddjpts", #Shiba
       "https://tinyurl.com/mu4js29p" ]#Samoyed

description = ["A golden retriever is best for families with small children, because it is a gentle, highly affectionate, and trainable companion.",
               "A husky suits active families who enjoy a high-exercise and independent dog.",
               "A shiba inu are best for patient families who have experience with cats, and understand its high-maintenance needs.",
               "A samoyed is ideal for families seeking a gentle, friendly dog needing regular grooming and moderate exercise."]

filter= []
def recommend ():
       while True:
              type = input("Hi, welcome to Perfect Companion. Would you like to get a dog recommendation? (yes,no) ").lower()
              if type == "yes":
                     dog = input("Are you looking for a gentle dog? (yes,no) ").lower()
                     if dog == "yes":
                            child = input("Do you have small children? (yes,no) ").lower()
                            if child == "yes":
                                   filter.append(description[0])
                                   webbrowser.open(url[0])
                                   print(filter)
                                   filter.clear()
                            else:
                                   hair = input("Are you okay with a dog that requires regular grooming? (yes, no) ").lower()
                                   if hair == "yes":
                                          filter.append(description[3])
                                          webbrowser.open(url[3])
                                          print(filter)
                                          filter.clear()
                                   elif hair == "no":
                                          filter.append(description[0])
                                          webbrowser.open(url[0])
                                          print(filter)
                                          filter.clear()

                                   else:
                                          print("Sorry I didn't get that, please try again.")
                     elif dog == "no":
                            fam = input("What type of family are you (active, patient) ").lower()
                            if fam == "active":
                                   filter.append(description[1])
                                   webbrowser.open(url[1])
                                   print(filter)
                                   filter.clear()
                            elif fam == "patient":
                                   filter.append(description[2])
                                   webbrowser.open(url[2])
                                   print(filter)
                                   filter.clear()
                            else:
                                   print("Sorry I didn't get that, please try again.")
                     else:
                            print("Sorry I didn't get that, please try again.")

              elif type == "no":
                     print("That's okay! Looking forward to seeing you in the future!")
                     break
              else:
                     print("unvalid response please try again.")


#Main
recommend()

#Sources of Information

#Picture of Golden Retriever:
#Website name: Times Entertainment
#Article URL: https://tinyurl.com/4ufswwu3
#Author name :N/A
#Date: June 16, 2025

#Picture of Husky:
#Wbebsite name: American Kennel Club
#Article URL: https://tinyurl.com/bdfk9dre
#Author name: How to Train a Siberian Husky Puppy: Milestones & Timeline
#Date: October 8, 2021

#Picture of Shiba:
#Website name:Furry Green
#Article URL:https://tinyurl.com/yd6kvbr9
#Author name:N/A
#Date: July 27, 2025

#Picture of Samoyed:
#Website name: Daily Paws
#Article URL: https://tinyurl.com/49jscehc
#Author name: Maddie Topliff
#Date: October 7, 2025
