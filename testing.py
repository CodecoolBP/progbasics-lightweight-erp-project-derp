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


'''generated = []
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()+=[]'
for i in range(8):
    generated.append(random.choice(chars))
generated = "".join(generated)
   

   
print(generated)'''

list_thing = ["g", "c", "f", "z"]
new_list_thing = []
abc = "a"
for i in list_thing:
    if ord(str(i)) > ord(abc):
        abc = (str(i))
        new_list_thing.append(abc)
    elif ord(str(i)) < ord(abc):
        ddf = str(i)
        new_list_thing.insert(0,ddf)
print(new_list_thing)

for i in new_list_thing:
    if ord(str(i)) > ord(abc):
        abc = (str(i))
        new_list_thing.append(abc)
    elif ord(str(i)) < ord(abc):
        ddf = str(i)
        new_list_thing.insert(0,ddf)
print(new_list_thing)




