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
        



    #def search_by_name():


    #def update_catches():


    #def delete_by_name():


def main():
    add_juggler('Andrea', 'US', 60)


main()
