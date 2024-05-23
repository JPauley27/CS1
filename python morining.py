print("alarm goes off")

while True:
    snooze = input("snooze?")
    
    if snooze == "yes":
        print("go back to sleep")
        print ("WAKE UP!")
    elif snooze == "no":
        break
    else:
        print ("that's not allowed.")
        
while True:
    shower = input("shower?")
    
    if shower == "no":
        print (" your stinky and smelly")
        break
    elif shower == "yes":
        print(" your clean")
        break
    else:
        print ("give me another anwser")
        
while True:
    getdressed = input ("get dressed?")
    
    if getdressed == "no" :
        print ("you need clothes you creep")
        break
    elif getdressed == "yes":
        print (" you look spiffy")
        break
    else:
        print ("thats not the anwser i'm looking for")
        
while True:
    eat = input ("Eat?")
    
    if eat == "no" :
        print (" you will be hungry")
        break
    elif eat == "yes" :
        print (" you are full now")
        break
    else:
        print (" that's not a anwser")
        
while True:
    raining = input (" Is it raining?")
    
    if raining == "yes":
        print ("grab a coat")
        break
    elif raining == "no" :
        print (" time to leave then.")
        break
    else:
        print (" I need a differnt anwser.")

while True:
    leaving = input (" leave the house?")
    if leaving == "yes" :
        print ("BYE BYE")
        break
    elif leaving == "no":
        print (" YOU NEED TO LEAVE GET OUT")
        break
    else:
        print (" i done with these bad anwsers GIVE ME A REAL ONE!!")
