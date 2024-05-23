##1,4,5, secure passowrd challenge, retroactivly adding a new PUW
import random

def print_info(websites, passwords, usernames,i):
    print(f'''website: {websites[i]}
password: {passwords[i]}
username: {usernames[i]}''')

def main(): # defines main function
    while True:
        secure_pass =["B,$5u^)19f#0","Y-6fS3vNy9&6","~2PPjUT2j^93","O-PzIG1!C71U"]# a secure password list
        websites =["vikky.com","triplett.com","randall.com","chickering.com"] # a websites list
        passwords= ["wolf9orange", "cat5apple","dog1pear","zebra3pinapple"] # a passwords list
        usernames = ["lukevikky", "lukevikky", "lukevikky","lukevikky"] # a usernames list
        
        mode= input ("which would you like:1. print all 2. print specific 3. Generate a new secure password 4. Add new username website and password?")# prompts the user ti enter a input

        if mode == "1": # if the user enters the number one prompting the computer
            for i in range(len(passwords)):
               print_info(websites, passwords, usernames,i)
        elif mode =="2": # if the user enters the number two prompting the computer
            name = input("enter a website: ") # it asks the user to enter a new website
            i = websites.index(name)# the website that is inputed is put into a name 
            print(name, usernames[i],passwords[i])# prints the name list, password and the username that goes with it
        elif mode =="3": # if the user enters the number three prompting the computer
            print (random.choice(secure_pass))# prints a random choice that is inside the secure_pass list
        elif mode == "4": # if the user enters the number four prompting the computer
            new = input("Do you want to enter new website, username, or password?")# asks the user the question inside of the qoutations
            newweb = input("what is your new website?")# asks the user to enter a input
            newuser = input("what is your new username?")# asks the user to enter a input
            newpass = input("what is your new password?")# asks the user to enter a input
            websites.append(newweb)# puts the user input from newweb into websites
            usernames.append(newuser)# puts the user input from newuser into usernames
            passwords.append(newpass)# puts the user input from newpass into passwords

            if websites in websites:
                i = websites.index(website)
        user_input = input()
        if user_input == "end":# if the user enters the word end
            break # stops the code
main()
2,3

##import random
##
##websites =["vikky.com","triplett.com","randall.com","chickering.com"]
##passwords= ["wolf9orange", "cat5apple","dog1pear","zebra3pinapple"]
##usernames = ["lukevikky", "lukevikky", "lukevikky","lukevikky"]
##
##def print_info(websites, passwords, usernames,i):
##    print(f'''website: {websites[i]}
##password: {passwords[i]}
##username: {usernames[i]}''')
##
##def main():
##
##    newweb = input("what is your new website?")
##    newuser = input("what is your new username?")
##    newpass = input("what is your new password?")
##    websites.append(newweb)
##    usernames.append(newuser)
##    passwords.append(newpass)
##main()
##mode= input ("which would you like:1. print all 2. print specific")
##
##if mode == "1":
##    for i in range(len(passwords)):
##        print_info(websites, passwords, usernames,i)
##elif mode =="2":
##    name = input("enter a website: ")
##    i = websites.index(name)
##    print(name, usernames[i],passwords[i])
##
##main()
