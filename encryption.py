def message_finder (message, original_alphabet, new_alphabet):
    new_message=''
    for m in message:
        for letter in original_alphabet:
            if m == letter:
                new_message += new_alphabet[original_alphabet.index(letter)]
    return new_message
def main():
    alphabet= list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    new_message=""
    secret_alphabet= list(" 12345678910@!*^V&$L1Q-=+><?/\}")
    message = str.upper(input("enter message"))
    encrypt = input("encrypt or decrypt")
    if encrypt == "encrypt":
        new_message =message_finder(message, alphabet, secret_alphabet)
    elif encrypt == "decrypt":
        new_message = message_finder(message, secret_alphabet, alphabet)
    print (new_message)
main()
