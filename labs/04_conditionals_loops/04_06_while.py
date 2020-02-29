'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

switch = True
fifth_numb = 0

while switch:
    if fifth_numb < 1000:
        fifth_numb += 5
        print(fifth_numb)
    elif fifth_numb >= 1000:
        switch = False
