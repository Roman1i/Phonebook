import user_interface
import view
import add
import import_option
import export_option


def start_program():
    status = True
    import_option.import_('log.csv')
    while status:
        user_interface.view_options()
        option = int(input())
        if option == 1:
            view.view_data()
        elif option == 2:
            add.add_new()
        elif option == 3:
            import_option.import_(input('Укажите путь: '))
        elif option == 4:
            export_option.export_(input('Укажите путь: '))
        elif option == 5:
            export_option.export_('log.csv')
            status = False
