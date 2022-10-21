def view_options():
    print('1. Просмотр запсей')
    print('2. Добавить запись')
    print('3. Импорт')
    print('4. Экспорт')
    print('5. Выход')


def get_option(n):
    option = int(input(n))
    return option
