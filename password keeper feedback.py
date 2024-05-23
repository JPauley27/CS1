import random # imports random variable

def print_info(websites, passwords, usernames,i):
    '''
    Prints an entry (website, password and username).

    Args:
        websites (list): all websites entered by the user.
        passwords (list): all corresponding passwords for every website.
        usernames (list): all corresponding usernames for every website.
        i (int): index of element to be printed

    Prints:
        it prints a index within the websites list, passwords list, and usernames list

    '''
    print(f'''website: {websites[i]}
password: {passwords[i]}
username: {usernames[i]}''')

def main(): # defines main function
    while True:
        secure_pass =["B,$5u^)19f#0","Y-6fS3vNy9&6","~2PPjUT2j^93","O-PzIG1!C71U","#?c(8Mu|0t17","RT{rh]8286@>",">07'N4G£*}ow"]# a secure password list
        websites =["vikky.com","triplett.com","randall.com","chickering.com"] # a websites list
        passwords = ["wolf9orange", "cat5apple","dog1pear","zebra3pinapple"] # a passwords list
        usernames = ["lukevikky", "lukevikky", "lukevikky","lukevikky"] # a usernames list
        
        mode = input ("which would you like:1. print all 2. print specific 3. Generate a new secure password 4. Add new username website and password?")# prompts the user ti enter a input

        if mode == "1": # if the user enters the number one prompting the computer
            for i in range(len(passwords)):
               print_info(websites, passwords, usernames,i)
        elif mode =="2": # if the user enters the number two prompting the computer
            name = input("enter a website: ") # it asks the user to enter a new website
            i = websites.index(name)# the website that is inputed is put into a name 
            print(name, usernames[i],passwords[i])# prints the name list, password and the username that goes with it
        else:
            print(" didn't input a website inside our database your going to have to restart the process")
        if mode =="3": # if the user enters the number three prompting the computer
            print (random.choice(secure_pass))# prints a random choice that is inside the secure_pass list
        elif mode == "4": # if the user enters the number four prompting the computer
            newweb = input("what is your new website?")# asks the user to enter a input
            newuser = input("what is your new username?")# asks the user to enter a input
            newpass = input("what is your new password?")# asks the user to enter a input
            websites.append(newweb)# puts the user input from newweb into websites
            usernames.append(newuser)# puts the user input from newuser into usernames
            passwords.append(newpass)# puts the user input from newpass into passwords
        user_input = input()# prompts the user for a input.
        if user_input == "end":# if the user enters the word end
            break # stops the code
main()

