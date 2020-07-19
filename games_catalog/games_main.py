#!/usr/bin/env python3

"""This script is mainly me practicing a couple of different ways to use OOP/Classes 
in python.
It is used to maintain a list of games, their systems and completion status.
Yes, I realize OOP may not be the best way of doing some of this, but I'm new to it. 
Written on/for Python 3.7+ on MacOS.
"""

import os
import random
import subprocess
from pathlib import Path

from colorama import Fore, Style, init

from art import disp_art
from games_class import Game

init()  # Initialize colorama
CWD = Path(os.path.realpath(__file__)).parent
RED = Fore.LIGHTRED_EX
BLUE = Fore.LIGHTBLUE_EX
RESET = Style.RESET_ALL
DELIM = ','


def read_data():
    """Read data from csv file, compiles and returns a list of Games objects."""
    games = []
    with open(f'{CWD}/games.csv', 'r') as f:
        for line in f:
            nm, sy, pl, cp = line.strip('\n').split(DELIM)
            games.append(Game(nm, sy, pl, cp))
    return games


def write_file(games, conf='n'):
    """Writes data to csv file after confirming changes if 'conf' flag is 'y'.
    'conf= is defaulted to 'n' and save is defaulted to 'y'.
    """
    save = 'y'
    if conf == 'y':
        save = input("Save changes?: ")
    if save.lower() == 'y':
        with open(f"{CWD}/games.csv", "w") as f:
            for game in games:
                f.write(
                    f"{game.name},{game.system},{game.played},{game.completed}\n")


def view_games(games):
    """Prints Games items from list to console.
    Switches output colors on each print."""

    # TODO: Change this to switch between color vars
    disp_title()
    color_switch = 1
    for game in games:
        if color_switch == 1:
            print(f"{RED}", end='')
            color_switch = 0
        else:
            print(f"{BLUE}", end='')
            color_switch = 1
        print(game)
        print(f"{RESET}", end='')
    input("ENTER to return...")


def search_games(games):
    """Allows for search of list of Games objects by name, system, 
    played, and completion and prints to console.
    """
    # TODO: Possibly update this to use menu_disp

    options = {'1': 'Name', '2': 'System',
               '3': 'Played', '4': 'Completed'}

    for num, opt in options.items():
        print(f"[{num}]: {opt}")
    selection = input("Selection: ")

    to_find = input("Search string: ")

    for game in games:
        if selection == '1':
            if to_find.lower() in game.name.lower():
                print(game)
        if selection == '2':
            if to_find.lower() in game.system.lower():
                print(game)
        if selection == '3':
            if to_find.lower() in game.played.lower():
                print(game)
        if selection == '4':
            if to_find.lower() in game.completed.lower():
                print(game)


def random_game(games):
    """Randomly pull a game from the list and display to console."""
    print(random.choice(games))


def add_game(games):
    """Creates a new Game object and adds it to the games list."""
    nm = input("Game name: ")
    sy = input("Which system: ")
    pl = input("Played it?: ")
    cp = input("Finished it?: ")

    games.append(Game(nm, sy, cp, pl))
    games.sort()
    view_games(games)
    write_file(games, 'y')


def name_search(games):
    """Searches for Game object in the list by name and returns 
    the located Game object's list index.
    """
    find = input("Enter at least 3 letters to search: ")

    found = [g for g in games if find.lower() in g.name.lower()]
    for i, gm in enumerate(found, 1):
        print(f"{i}: {gm}")

    sel = input("Selection: ")

    for game in games:
        if found[int(sel)-1] == game:
            return games.index(game)


def update_game(games):
    """Locates Game object in the list and allows info updates."""
    ndx = name_search(games)

    options = {
        '1': ("Name", games[ndx].set_name),
        '2': ("System", games[ndx].set_system),
        '3': ("Played", games[ndx].set_played),
        '4': ("Completed", games[ndx].set_completed)
    }

    method_call = menu_display(options)

    update = input("New info: ")
    method_call(update)
    games.sort()


def remove_game(games):
    """Locates and deletes Game objects from the list."""
    ndx = name_search(games)

    print(games[ndx])
    if input("Remove?: ").lower() == 'y':
        del games[ndx]
        view_games(games)
        write_file(games, 'y')


def clear_screen():
    """MacOS clear screen command."""
    subprocess.run('clear', shell=True)


def disp_title():
    """Clear screen and display ASCII art."""
    clear_screen()
    disp_art()


def menu_display(options):
    """Displays passed dictionary of menu items to the console, 
    returns 2nd item in tuple value.
    """
    while True:
        disp_title()
        for num, pair in options.items():
            print(f"\t   {BLUE}[{num}]: {pair[0]}{RESET}")

        sel = input("\nSelection: ")
        if options.get(sel):
            return options.get(sel)[1]
        input("ENTER to try again...")


def main_menu(games):
    """Display menu and run function based on return from menu_display, 
    passing games list.
    """

    options = {
        '1': ('View Games', view_games),
        '2': ('Search Games', search_games),
        '3': ('Random Game', random_game),
        '4': ('Add Game', add_game),
        '5': ('Update Game', update_game),
        '6': ('Remove Game', remove_game)
    }

    menu_display(options)(games)


def main():
    """Main-Reads data from csv, creates Games objects based on the file, 
    generates the main list of objects and calls the main menu. 
    """
    games = read_data()
    while True:
        disp_title()
        main_menu(games)


if __name__ == "__main__":
    main()
