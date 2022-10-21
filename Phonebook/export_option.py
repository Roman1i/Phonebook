import view


def export_(way):
    with open(way, 'w', encoding='UTF-8') as file:
        for i in view.using_book:
            for j, j_item in enumerate(i):
                if j != len(i)-1:
                    file.write(str(j_item)+';')
                else:
                    file.write(str(j_item))
