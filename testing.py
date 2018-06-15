import random

'''def open_stuff():
    with open("test.csv", "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
        return table
        
def print_stuff():
    table = open_stuff()
    for lines in table:
      
        for element in lines:
            print('| {} '.format(element), end='')
        print(' |\n')

open_stuff()
print_stuff()'''


generated = []
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()+=[]'
for i in range(8):
    generated.append(random.choice(chars))
generated = "".join(generated)
   

   
print(generated)