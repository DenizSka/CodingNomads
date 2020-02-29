"""
Replicate one of the oldest known encryption in code.
Apply a Cesar cipher of 7 to the 'secret' variable.
P.S.: http://www.montypython.net/scripts/dentist.php ;)
You can start with the following code:
"""

# need help

# secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
# cipher = 7

# secret = 'abc'
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# new_list = []
#
# def ciphering(secret, cipher):
#     list_words = secret.upper()
#   Looping through the string will create a list of letters for me. No need for split
#     list_words = list_words.split()
#     for one in list_words:
#         list_letter = list(one)
#         for letter in list_letter:
#             get_index = alphabet.index(letter)
#             new_index = get_index - int(cipher)
#             new_list.append(alphabet[new_index])
#     print(new_list)
#
# print(ciphering(secret,cipher))

# First we start with simple version of the secret and cipher so we can debug.
secret = 'ccda sda'
x = secret.upper()
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cipher = 1
z = " "

# you can do a javascript type of for loop in python using range
for y in range(0, len(x)):
    for i in range(0, len(alphabet)):
        print(f"this is y {y}")
        print(f"this is i {i}")
        if x[y] == alphabet[i]:
            # print(i)
            # print(alphabet[i])
            # print(alphabet[i-cipher])
            new_letter = alphabet[i-cipher]
            z = z + str(new_letter)
        elif x[y] == " ":
            z = z + " "

print(z)

# now we can call this loop with more complex secret and cipher


secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

secret = secret.upper()

response_string = " "
for secret_index in range(0, len(secret)):
    for alp_index in range(0, len(alphabet)):
        if secret[secret_index] == alphabet[alp_index]:
            new_letter = alphabet[alp_index-cipher]
            response_string = response_string + str(new_letter)
    if secret[secret_index] == " ":
        response_string = response_string + " "

print(response_string)
