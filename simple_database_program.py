from peewee import *

db = SqliteDatabase('Jugglers.sqlite')

class Juggler(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db


    def __str__(self):
        return(f'Name: {self.name}, Country: {self.country}, # of Catches: {self.catches}')


"""CODE FOR THE MENU FEATURE WAS ADAPTED FROM THE CAPSTONE READING LIST PROJECT"""
class Menu():

    def __init__(self):
        self.menu_options = {}
        self.functions = {}


    def add_menu_option(self, key, text, function):
        self.menu_options[key] = text
        self.functions[key] = function


    def is_valid_choice(self, choice):
        return choice in self.menu_options


    def get_function(self, choice):
        return self.functions[choice]


    def __str__(self):
        menu_options = [f'{key}: {self.menu_options[key]}' for key in self.menu_options.keys()]
        return '\n'.join(menu_options)

    
"""These functions work directly with the Juggler class to update data in the database"""
def add_juggler(name, country, catches):
    new_juggler = Juggler(name=name, country=country, catches=catches)
    new_juggler.save()
        

def search_by_name(name):
    juggler = Juggler.get(Juggler.name == name)
    return juggler


def update_catches(name, new_catches):
    Juggler.update(catches=new_catches).where(Juggler.name == name).execute()


def delete_by_name(name_to_delete):
    Juggler.delete().where(Juggler.name == name_to_delete).execute()


"""Set up function"""
def make_menu():
    menu = Menu()
    menu.add_menu_option('1', 'Add new juggler.', add_juggler_ui)
    menu.add_menu_option('2', 'Search juggler by name.', search_by_name_ui)
    menu.add_menu_option('3', 'Update juggler catches.', update_catches_ui)
    menu.add_menu_option('4', 'Delete juggler by name.', delete_by_name_ui)
    menu.add_menu_option('5', 'Display all jugglers.', display_all)
    menu.add_menu_option('Q', 'Quit program.', quit_program)
    return menu


"""These functions act as the user interface for the application"""
def display_menu(menu):
    while True:
        print(menu)
        choice = input('What would you like to do? ').upper()
        if menu.is_valid_choice(choice):
            return choice
        else:
            print('Please enter a valid menu option.')


def add_juggler_ui():
    name = input('New juggler name: ')
    country = input('New juggler country: ')
    catches = get_number_catches()
    add_juggler(name, country, catches)

    
def search_by_name_ui():
    name = input('Juggler to search for: ')
    juggler = search_by_name(name)
    print(juggler)
    

def update_catches_ui():
    name = input('Name of juggler to update: ')
    catches = get_number_catches()
    update_catches(name, catches)


def delete_by_name_ui():
    name = input('Name of juggler to delete: ')
    delete_by_name(name)


def display_all():
    print('\n')
    for juggler in Juggler.select():
        print(juggler)
    print('\n')


def get_number_catches():
    while True:
        catches = input('New number of catches: ')
        if catches.isdigit():
            return catches
        else:
            print('Please enter a valid integer.')


def quit_program():
    print('GOODBYE.')


"""Main function of the program"""
def main():
    print('\nChainsaw Juggling Record Holders as of July 2018\n\n')
    menu = make_menu()
    while True:
        user_choice = display_menu(menu)
        function = menu.get_function(user_choice)
        function()
        if user_choice == 'Q':
            quit_program()


main()

