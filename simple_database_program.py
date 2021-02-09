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

    

def add_juggler(name, country, catches):
    new_juggler = Juggler(name=name, country=country, catches=catches)
    new_juggler.save()
    return new_juggler
        

def search_by_name(name):
    juggler = Juggler.get(Juggler.name == name)
    return juggler


def update_catches(name, new_catches):
    juggler_to_update = search_by_name(name)
    juggler_to_update.catches = new_catches
    juggler_to_update.save()




#def delete_by_name():


def main():
    add_juggler('Andrea', 'US', 60)
    #some_other_person = add_juggler('Andrea', 'US', 60)

    andrea_info = search_by_name('Andrea')
    print(andrea_info)

    update_catches('Andrea', 500)
    print('\nWhat it looks like after update')
    andrea_info = search_by_name('Andrea')
    print(andrea_info)


main()
