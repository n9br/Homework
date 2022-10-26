from decimal import Decimal
import os
from tkinter import commondialog
from rich import print
from rich.console import Console
from rich.table import Table
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, update
from sqlalchemy.orm import declarative_base, sessionmaker
from turtle import window_height

# rich console
console = Console()

# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///Friends.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()
# # # ###########################################


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_nr = Column(String)
    nick_name = Column(String)
    address = Column(String)
    birthday = Column(String)
    email = Column(String)

    # Foreignkeys
    language_id = Column(Integer, ForeignKey("languages.id"))
    bike_id = Column(Integer, ForeignKey("bikes.id"))

class Bike(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    tyre_width = Column(Integer)
    weight = Column(Integer)
    gears = Column(Integer)
    brand = Column(String)
    model = Column(String)

def initialize_database():
    """
    Initializes the database and creates all tables.

    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.
    """
    session.add(friend)
    # ORM - Object Relational Mapper 
    session.commit()

def database_delete_friend(id: str):
    """
    DB delete record
    """
    delFriend = session.get(Friend, id)
    session.delete(delFriend)
    session.commit()
    # session.query.filter(User.id == 123).delete()


def database_get_all_friends():
    """
    Database command to get all friends.
    """
    #os.
    all_friends = session.query(Friend).all()
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("id", style='dim')
    table.add_column("FirstName")
    table.add_column("LastName")
    table.add_column("Phone")
    table.add_column("Nick")
    table.add_column("Address")

    for friend in all_friends:
    #    print(f"{friend.first_name} {friend.last_name}")
        table.add_row(str(friend.id),friend.first_name,friend.last_name,friend.phone_nr,friend.nick_name,friend.address)
    console.print(table)


def add_friends():
    """
    Freunde eingeben
    """
    addingFriends = True

    while addingFriends:
        new_friend = Friend()

        new_friend.first_name = input("Name \t: ")
        new_friend.last_name = input("Surname \t:")
        new_friend.phone_nr = input("Phone# \t:")
        new_friend.nick_name = input("Nick \t:")
        new_friend.address = input("Address \t:")
        new_friend.birthday = input("BDay \t:")
        new_friend.email = input("Email \t:")
        addingFriends = input("Add more friends? Leave blank to not.")

    # new_friend = Friend(first_name = "Robert", last_name = "Kozljanic", phone_nr = "0157 24 88 357", nick_name = "Roberto", 
    #    address = "MUC", birthday = "30.3.1970", email = "roberto@gmail.com")

    # !? Validierung ?!

    database_add_friend(new_friend)

def database_update_friend(id: int, ucol: str, ustr: str):
    """
    DB update record
    """
    session.execute(
        update(Friend)
        .where(Friend.id == id)
        .values(ucol=ustr)
    )
    session.commit()

def update_friends():
    """
    Freunde aktualisieren
    """

    updateId = input("Which ID do you want to update? :")
    print("""
        Which Column do you want to update ? Spell correctly.
        first_name
        last_name
        phone_nr
        nick_name
        address
        birthday
        email
    """
    )
    updateCol = input()
    updateStr = input("Enter new value: ")

    database_update_friend(updateId,updateCol,updateStr)


def delete_friends():
    """
    select and delete friend
    """
       
    delId = input("Which id do you want to delete? :")

    database_delete_friend(str(delId))

    
def getUserInput():
    print('''
    What do you want to do ?

    (a)dd user
    (l)ist users
    (d)elete user
    (u)pdate user
    (e)xit    
    
    ''')

    userInput = input()
    userInput = userInput.lower()

    return(userInput)

# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

    while True:

        userInput = getUserInput()

        match userInput:
            case 'e':
                exit(1)

            case 'a':
                add_friends() 

            case 'l':
                # Example to list all friends
                database_get_all_friends()
            
            case 'u':
                database_get_all_friends()
                update_friends()

            case 'd':
                delete_friends()
