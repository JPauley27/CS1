import random# imports random from library 

foods = ["cauliflower","tilapia fillet","pork loin","green beans","rainbow carrots","potatoes","three color squash","eggplant","eye round of beef","baguette",]# this is a list of foods
sides = ["with balsamico","with garlic and olive oil","with minted yogurt","soup","chutney","salad","with salsa","over sticky rice","au jus","with basmati rice"]# this is a list of sides

while True:
      try:# tries code below,if there is a error it will enter the execpt loop 
            number_of_dishes = int(input("How many items do you need?"))# asks user for the number of dishes they want

            if number_of_dishes > 0: # if the number of dishes break the loop
                  break # break the loop
            else:
                  print("Please enter a number greater than zero!") # prints the phrase in the parenthesis
      except ValueError:# if there was a value error in the try loop
            print("Enter an integer!")# prints the phrase within the perenthesis
            
for i in range(number_of_dishes): # loops for the amount of items in number of dishes
      print(f"{random.choice(foods)} {random.choice(sides)}")# prints a random choice from foods and from sides in the f string
