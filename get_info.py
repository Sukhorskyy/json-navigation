'''
Module gives user easy access to the information in .json file
'''
import json
import pprint


def read_data(path):
    '''
    Return data from .json file
    '''
    with open(path, mode='r', encoding='utf-8') as timeline:
        data = json.load(timeline)
    return data


def is_list(data):
    '''
    Print the information about list
    '''
    print('It is a list')
    print('Choose one of the next function by printing its number:')
    print('1. Get length of list')
    print('2. Get the content of list')
    print('3. Get the content of element by printing its index')
    print('0. Exit')
    while True:
        action = input('Your choise: ')
        if action == '1':
            print(len(data))
        elif action == '2':
            pprint.pprint(data)
        elif action == '3':
            el_index = input('Input index of element: ')
            pprint.pprint(data[int(el_index)])
        elif action == '0':
            break
        else:
            print('Wrong function. Try again.')


def is_dict(data):
    '''
    Print the information about dict
    '''
    print('It is a dictionary')
    print('Choose one of the next function by printing its number:')
    print('1. Get length of dictionary')
    print('2. Get keys of dictionary')
    print('3. Get the value of key by printing its name')
    print('4. Get the whole content of dictionary')
    print('0. Exit')
    while True:
        action = input('Your choise: ')
        if action == '1':
            print(len(data))
        elif action == '2':
            print(data.keys())
        elif action == '3':
            el_name = input('Input the key: ')
            pprint.pprint(data[el_name])
        elif action == '4':
            pprint.pprint(data)
        elif action == '0':
            break
        else:
            print('Wrong function. Try again.')


def main():
    path_to_file = input('Please, print path to the file: ')
    data = read_data(path_to_file)
    if type(data) == list:
        is_list(data)
    elif type(data) == dict:
        is_dict(data)
    else:
        print('It is neither list nor dictionary')


if __name__ == "__main__":
    main()