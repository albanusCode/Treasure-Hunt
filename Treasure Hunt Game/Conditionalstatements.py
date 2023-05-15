# #conditional statements  if/else and nested if/else statement
# print("Welcome to RollerCoaster!")
# height = int(input("What is your height in centimeters?\n"))

# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("What is you age?\n"))
#     if age < 12:
#         print("child ticket is $5 only.")
#     elif age <= 18:
#         print("youth ticket is $7 only.")
#     else:
#         print("adult ticket is $12 only")
                
# else:
#     print("sorry! You have to grow taller before you can ride")    

# number = input("which number do you want to chooose?\n")
# if int(number) % 2 == 0:
#     print("This is an even number")
# else:
#     print("this is an odd number")

# weight = input("Enter your weight in kgs \n")
# height = input("Enter yor height in meters \n")
# BMI = int(float(weight)/float(height)**2) #** raises power to exponetial
# if BMI < 8.5:
#     print(f"your BMI is {BMI} you are underweight")
# elif BMI < 25:
#     print(f"your BMI is {BMI} you have a normal weight")
# elif BMI < 30:
#     print(f"your BMI is {BMI} you are overweight")
# elif BMI < 35:
#     print(f"your BMI is {BMI} you have obese weight")
# else:
#     print(f"your BMI is {BMI} you have clinically obese weight")

# #leap year
# year = int(input("Enter year to check"))
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("leap year")
# else:
#     print("Not leap year")

#     #multple if statements -- when we want to check several conditions even with the first being true
# print("Welcome to RollerCoaster!")
# height = int(input("What is your height in centimeters?\n"))
# bill = 0
# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("What is you age?\n"))
#     if age < 12:
#         bill = 5
#         print("child ticket is $5 only.")
#     elif age <= 18:
#         bill = 7
#         print("youth ticket is $7 only.")
#     else:
#         bill = 12
#         print("adult ticket is $12 only")
#     wants_photo  = input("Do you want photo taken? Y or N. ")
#     if wants_photo == "Y" or "y":
#         bill +=3
#     print(f"Your bill is ${bill}. ")            
# else:
#     print("sorry! You have to grow taller before you can ride")    

#pizza order
# print("Welcome to python pzza deliveries. ")
# size = input("What size of pizza do you want? S, M or L \n")
# add_pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")
# bill = 0
# if size == "S":
#     bill+=15
# elif size == "M": 
#     bill+=20
# else: 
#     bill+=25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill+=2
#     else:
#         bill+=3    
# if extra_cheese == "Y":
#     bill+=1 
# print(f"Your total bill is {bill}")

#Logical operations
# print("Welcome to RollerCoaster!")
# height = int(input("What is your height in centimeters?\n"))
# bill = 0
# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("What is you age?\n"))
#     if age < 12:
#         bill = 5
#         print("child ticket is $5 only.")
#     elif age <= 18:
#         bill = 7
#         print("youth ticket is $7 only.")
#     elif age >= 45 and age <= 50:
#         print("We are currently givingg free tickets for this age bracket.")
#     else:
#         bill = 12
#         print("adult ticket is $12 only")
#     wants_photo  = input("Do you want photo taken? Y or N. ")
#     if wants_photo == "Y" or "y":
#         bill +=3
#     print(f"Your bill is ${bill}. Have fun ")            
# else:
#     print("sorry! You have to grow taller before you can ride")    

#beezfeed love calculator
# name1 = input("Enter your name \n")
# name2 = input("Enter their name \n")
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
# print(f"t = {t}")
# print(f"r = {r}")
# print(f"u = {u}")
# print(f"e = {e}")
# print(f"Total = {true}")

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
# print(f"l = {l}")
# print(f"o = {o}")
# print(f"v = {v}")
# print(f"e = {e}")
# print(f"Total = {love}")

# score = int(str(true) + str(love))

# if (score < 10) or (score > 90):
#     print(f"Your score is {score}. You go together like coke and mentos")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}. You're alright together")
# else:
#     print(f"Your score is {score}") 

#Day3 Final Project
#lower()  convers whatever the user inputs to lower case always.
print("Welcome to treasure island puzzle")
treasure = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

choice1 = input('You\'re in a cross road. where do you want to go? type Left or right. \n').lower()
if choice1 == "left":
    choice2 = input("You reached the sea. You need to go to the island. Choose means. Type 'Wait' to wait for boat or 'Swim' To swmim across \n").lower()
    if choice2 == "wait":
        choice3 = input("You have reachead the island. Open one of the doors, Type 'Blue' to open the blue door, 'Yellow' to open the yellow door or 'Red' to open the red door. \n ").lower()
        if choice3 == "yellow":
            print(f"WALALAAA! CONGRATULATIONS you've found the treasure. YOU WIN\n {treasure}")
        else:
            print("OOPS! Wrong door. YOU FAILED ")    
    else:
        print("OOPS! long distance. you drowned. YOU FAILED")
else:
    print("OOPS! Wrong way. YOU FAILED ")
