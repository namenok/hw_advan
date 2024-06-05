#практична пікль
import pickle
import json

cu = int(input(
    f'меню\n1.завантажити дані \n2.зберегти дані \n3.додавати дані \n4.видалення даних \t\t\nвведи відповідну цифру: '))

file_name = 'values.dat'
if cu == 1:
    li = [1, 2, 3, 4, 5]
    file_pi = 'val.dat'

    def serialize(val):
        with open(file_pi, 'wb') as fi:
            pickle.dump(val, fi)

    with open(file_pi, 'rb') as f:
        print(f.read())
elif cu == 2:

    do = [input('введи свої 5 цілих чисел: ')]
    file_pi_2 = 'valu.dat'

    def serialize2(val):
        with open(file_pi_2, 'wb') as fi:
            pickle.dump(val, fi)
    serialize2(file_pi_2)

elif cu == 3:
    do1 = [input('введи свої 5 цілих чисел в рядок: ')]
    do2 = [input('введи свої 5 цілих чисел в рядок, які ти хочеш додати: ')]

    pi_file_3 = 'pifi.dat'

    def serialize(val):
        with open(pi_file_3, 'wb') as fi:
            pickle.dump(val, fi)
    serialize(do1)

    def serialize(val):
        with open(pi_file_3, 'a+') as fi:
            pickle.dump(val, fi)
    serialize(do2)
elif cu == 4:
    li = [1, 2, 3, 4, 5]
    file_pi = 'val.dat'

    def serialize(val):
        with open(file_pi, 'wb') as fi:
            pickle.dump(val, fi)
    serialize(li)

    with open(file_pi, 'wb') as f:
        f.seek(0)
else:
    print('неправильний ввід')



#практична json

my_dict = dict(
    log1='pas1',
    log2='pas2',
    log3='pas3'
)
file_name_js = 'values.json'

def serialized_json(json_data):
    with open('json21.json', 'w') as file:
        json.dump(json_data, file)
serialized_json(my_dict)

#додавання даних до файлу
my_second_dict = dict(
    log4='pas4',
    log5='pas5'
)
with open('json21.json', 'a') as file:
    json.dump(my_second_dict, file)

#видалення усіх даних з файлу
o = dict()
with open('json21.json', 'w') as file:
    json.dump(o, file) #видаляються дані, як перезапиc

#пошук
#знову завантажую туди дані, щоб було з чого шукати
def serialized_json(json_data):
    with open('json21.json', 'w') as file:
        json.dump(json_data, file)
serialized_json(my_dict)

with open('json21.json', 'r') as file:
    if 'log3' in file:
        print('так, є такий ключ')

#редагування - десеріалізую - видалю один елемент , засеріалізую, зберігається
with open('json21.json', 'r') as file:
    json.load(file)
    del my_dict['log2']
    print(my_dict)
    json.dump(my_dict, file)

#завантажити ( відобразити ?
with open('json21.json', 'r') as file:
    json.load(file)
    file.read()

#--------------------домашня робота----------------
# 1

my_dict = dict(
    Ukraine='Kyiv',
    UK='London',
    France='Paris'
)
file_name_js = 'values.json'

def serialized_json(json_data):
    with open('json21.json', 'w') as file:
        json.dump(json_data, file)

serialized_json(my_dict)

#додавання даних до файлу
my_second_dict = dict(
    Germany='Berlin',
    Polska='Varshava'
)
with open('json21.json', 'a') as file:
    json.dump(my_second_dict, file)

#видалення усіх даних з файлу
o = dict()
with open('json21.json', 'w') as file:
    json.dump(o, file)

#пошук
#знову завантажую туди дані, щоб було з чого шукати
def serialized_json(json_data):
    with open('json21.json', 'w') as file:
        json.dump(json_data, file)
serialized_json(my_dict)

with open('json21.json', 'r') as file:
    if 'Germany' in file:
        print('так, є такий ключ')

#редагування - десеріалізую - видалю один елемент , засеріалізую, зберігається
with open('json21.json', 'r') as file:
    json.load(file)
    del my_dict['Polska']
    print(my_dict)
    json.dump(my_dict, file)

#завантажити
with open('json21.json', 'r') as file:
    json.load(file)
    file.read()



# 2
import json

my_dict = dict(
    grupaX='albomX',
    grupaY='albomY',
    grupaB='albomB'
)
file_name_js = 'values.json'

def serialized_json(json_data):
    with open('json21.json', 'w') as file:
        json.dump(json_data, file)

serialized_json(my_dict)

#додавання даних до файлу
my_second_dict = dict(
    grupaD='albomD',
    grupaS='albomS'
)
with open('json21.json', 'a') as file:
    json.dump(my_second_dict, file)

#видалення усіх даних з файлу
o = dict()
with open('json21.json', 'w') as file:
    json.dump(o, file)

#пошук
#знову завантажую туди дані, щоб було з чого шукати
def serialized_json(json_data):
    with open('json21.json', 'w') as file:
        json.dump(json_data, file)
serialized_json(my_dict)

with open('json21.json', 'r') as file:
    if 'grupaY' in file:
        print('так, є такий ключ')

#редагування - десеріалізую - видалю один елемент , засеріалізую, зберігається
with open('json21.json', 'r') as file:
    json.load(file)
    del my_dict['grupaD']
    print(my_dict)
    json.dump(my_dict, file)

#завантажити
with open('json21.json', 'r') as file:
    json.load(file)
    file.read()