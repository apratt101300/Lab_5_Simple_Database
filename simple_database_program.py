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


def delete_by_name(name):
    juggler_to_delete = search_by_name(name)
    juggler_to_delete.delete_instance()



def main():
    add_juggler('Andrea', 'US', 60)
    add_juggler('Bob', 'UK', 500)
    add_juggler('Maria', 'UK', 520)
    add_juggler('Eric', 'Venezuala', 300)
    add_juggler('Eric', 'Venezuala', 300)
    add_juggler('Eric', 'Venezuala', 300)


    for juggler in Juggler.select():
        print(juggler)
    

    delete_by_name('Bob')
    delete_by_name('Eric')
    print('\nWhat it looks like after update')

    for juggler in Juggler.select():
        print(juggler)
    


main()
