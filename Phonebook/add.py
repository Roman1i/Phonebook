import view


def add_new():
    name = input('Введите имя: ')
    number = input('Введите номер: ')
    description = input('Введите описание: ')
    view.using_book.append([name, number, description + '\n'])
