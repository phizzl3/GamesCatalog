#!/usr/bin/env python3

"""This script is mainly me practicing a couple of different ways to use OOP/Classes
in python.
It is used to maintain a list of games, their systems and completion status.
Yes, I realize OOP may not be the best way of doing some of this, but I'm new to it.
Written on/for Python 3.7+ on MacOS.
"""



from art import disp_art
from classes import Game, GamesList




def menu_display(options):
    """Displays passed dictionary of menu items to the console,
    returns 2nd item in tuple value.
    """
    while True:
        disp_art()
        for num, pair in options.items():
            print(f"\t  [{num}]: {pair[0]}")

        sel = input("\nSelection: ")
        if options.get(sel):
            return options.get(sel)[1]
        input("ENTER to try again...")


def main_menu(games):
    """Display menu and run function based on return from menu_display,
    passing games list.
    """

    options = {
        '1': ('View Games', games.view_games),
        '2': ('Search Games', games.search_games),
        '3': ('Random Game', games.random_game),
        '4': ('Add Game', games.add_game),
        '5': ('Update Game', games.update_game),
        '6': ('Remove Game', games.remove_game)
    }

    menu_display(options)()


def main():
    """Main-Reads data from csv, creates Games objects based on the file,
    generates the main list of objects and calls the main menu.
    """
    games = GamesList()
    games.read_data()
    while True:
        disp_art()
        main_menu(games)


if __name__ == "__main__":
    main()
