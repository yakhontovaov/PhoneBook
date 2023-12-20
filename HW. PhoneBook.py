filename = 'phone.txt'


def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Найти абонента по номеру телефона',
          '4. Изменить номер телефона',
          '5. Добавить абонента в справочник',
          '6. Удалить запись',
          '7. Закончить работу', sep='\n')

    choice = int(input('Введите номер меню: '))
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            string = ''
            for v in phone_book[i].values():
                string += v + ','
            phout.write(f'{string[:-1]}\n')


def find_by_lastname(phone_book, last_name):
    for k in phone_book:
        if last_name == k['Фамилия']:
            return k['Телефон']
    return 'Такого абонента не существует'


def find_by_number(phone_book, number):
    for k in phone_book:
        if number == k['Телефон']:
            return k['Телефон']
    return 'Такого абонента не существует'


def change_number(phone_book, last_name, new_number):
    new_num = {}
    for k in phone_book:
        if last_name == k['Фамилия']:
            new_num = k
            new_num['Телефон'] = new_number
            phone_book.remove(k).append(new_num)
            write_txt(filename, phone_book)
            return 'Номер телефона ' + new_num['Имя'] + ' ' + new_num['Фамилия'] + ' изменен'
    return 'Такого абонента не существует'


def add_user(phone_book, new_user):
    phone_book.append(new_user)
    write_txt(filename, phone_book)
    return 'Новый абонент ' + new_user['Имя'] + ' ' + new_user['Фамилия'] + ' добавлен'


def delete_by_lastname(phone_book, last_name):
    for k in phone_book:
        if last_name == k['Фамилия']:
            phone_book.remove(k)
            write_txt(filename, phone_book)
            return 'Абонент ' + k['Имя'] + k['Фамилия'] + ' удален'
    return 'Такого абонента не существует'


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt(filename)

    while (choice != 7):
        if choice == 1:
            print(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите телефон ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            last_name = input('Введите фамилию ')
            new_number = input('Новый номер ')
            print(change_number(phone_book, last_name, new_number))
            # write_txt(filename, phone_book)
        elif choice == 5:
            fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
            new_user = {}
            for k in fields:
                inputStr = input('Введите ' + k + ': ')
                if len(inputStr) == 0:
                    inputStr = input('Введите ' + k + ': ')
                new_user[k] = inputStr
            print(add_user(phone_book, new_user))
            # with open(filename, 'r', encoding='utf-8') as phb:
            #     for line in phb:
            #         record = dict(zip(fields, line.split(',')))
            #         data.append(record)
            # return phone_book
            # new_user = input('new user ')
            # add_user(phone_book, new_user)
            # write_txt(filename, phone_book)
        elif choice == 6:
            lastname = input('Фамилия ')
            print(delete_by_lastname(phone_book, lastname))

        choice = show_menu()


work_with_phonebook()
