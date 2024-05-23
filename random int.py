import random

while True:
    question = str.lower(input("whats your question?"))
    responses = ["YES","NO","Maybe" ," ask again later"," i don't think that will happen","outlook is good","my relpy is no","signs point to yes","signs point to no", " ask later I need to ponder my response", "very doubtful","without a doubt" ]

    if "will i be" in question:
        nolist =[" No","never","that will not happen","My reply is no","signs point to no"]
        print(random.choice(nolist))
    elif "am i" in question:
        yeslist =["yes","of corse","signs point to yes","without a doubt","of corse","why not"]
        print(random.choice(yeslist))
    else:
        print(random.choice(responses))
    
