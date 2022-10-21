import view


def import_(way):
    with open(way, 'r', encoding='UTF-8') as file:
        out = []
        lst_ = file.readlines()
        for item in lst_:
            out.append(item.split(";"))
        view.using_book = out
