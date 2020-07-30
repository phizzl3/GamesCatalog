"""This script is mainly me practicing a couple of different ways to use OOP/Classes 
in python.
It is used to maintain a list of games, their systems and completion status.
Yes, I realize OOP may not be the best way of doing some of this, but I'm new to it. 
"""


import random
from pathlib import Path

from art import disp_art

FILE = f"{Path(__file__).resolve().parent}/data/games.csv"


class Game:
    """Instantiates Game objects.
    """
    # Class attribute used to count the number of game objects created
    number_of_games = 0

    def __init__(self, name, system, played, completed):
        """Initializes the attributes for each object created.
        """
        self.name = name
        self.system = system
        self.played = played
        self.completed = completed

        # Adds to number of games each time a Game object is created
        Game.number_of_games += 1

    def __str__(self):
        """Sets string output for objects.
        """
        return f"{self.name:43}: {self.system:>6} - {self.played:>6} - {self.completed:>9}"

    def __eq__(self, other):
        """Sets equal to.
        """
        return self.name == other.name and self.system == other.system

    def __lt__(self, other):
        """Sets less than comparison to use to compare objects for sort function.
        """
        return self.name < other.name

    @classmethod
    def get_total_games(cls):
        """Returns the total number of games (Class object).
        """
        return cls.number_of_games

    def set_name(self, name):
        """Changes the object's name.
        """
        self.name = name

    def set_system(self, system):
        """Changes the object's system.
        """
        self.system = system

    def set_played(self, played):
        """Changes the object's played status.
        """
        self.played = played

    def set_completed(self, completed):
        """Changes the object's completion status.
        """
        self.completed = completed


class GamesList(list):
    """Instantiates a list-like object used to hold the Games objects.
    """

    def read_data(self):
        """Reads data from csv file, creates Games objects and 
        compiles a list object.
        """
        with open(FILE, 'r') as f:
            for line in f:
                nm, sy, pl, cp = line.strip('\n').split(',')
                self.append(Game(nm, sy, pl, cp))

    def write_file(self):
        """Writes data to csv file after confirming changes.
        """
        save = input("Save changes? (y/n): ")
        if save.lower() == 'y':
            with open(FILE, "w") as f:
                for game in self:
                    f.write(
                        f"{game.name},{game.system},{game.played},{game.completed}\n")

    @staticmethod
    def disp_header():
        """Display's ASCII art and headers to console.
        """
        disp_art()
        # Print header
        print("{:43}: {:>6} - {:>6} - {:>9}".format(
            "Game", "System", "Played", "Completed"
        ))
        print("="*72)

    def view_games(self):
        """Prints Games items from list to console.
        """
        GamesList.disp_header()
        for game in self:
            print(game)
        # Display total number of games
        print(f"\nTotal Games: {Game.get_total_games()}")

        input("\nENTER to return...")

    def random_game(self):
        """Randomly pulls a game from the list and displays to console.
        """
        GamesList.disp_header()
        print(random.choice(self))

        input("\nENTER to return...")

    def search_games(self):
        """Searches list of Games objects by name, system,
        played, and completion and prints to console.
        """
        options = {
            '1': ('Name', '1'),
            '2': ('System', '2'),
            '3': ('Played', '3'),
            '4': ('Completed', '4')
        }

        # Display menu and gets user inputs
        sel = GamesList.menu_display(options)
        to_find = input("Search string: ")

        # Display games info based on selection
        GamesList.disp_header()
        for game in self:
            if sel == '1' and to_find.lower() in game.name.lower():
                print(game)
            if sel == '2' and to_find.lower() in game.system.lower():
                print(game)
            if sel == '3' and to_find.lower() in game.played.lower():
                print(game)
            if sel == '4' and to_find.lower() in game.completed.lower():
                print(game)

        input("\nENTER to return...")

    def add_game(self):
        """Creates a new Game object and adds it to the games list.
        """
        nm = input("Game name: ")
        sy = input("Which system: ")
        pl = input("Played it?: ")
        cp = input("Finished it?: ")

        # Add new object
        self.append(Game(nm, sy, cp, pl))

        # Sort, display, and write list
        self.sort()
        self.view_games()
        self.write_file()

    def name_search(self):
        """Searches for Game object in the list by name and returns
        the located Game object's list index.
        """
        find = input("Search string: ")

        # Generate list of found objects and display to console
        found = [g for g in self if find.lower() in g.name.lower()]
        if found:
            GamesList.disp_header()
            for i, gm in enumerate(found, 1):
                print(f"{i}: {gm}")

            # Get user input and return index of selection
            sel = input("Selection: ")
            for game in self:
                if found[int(sel)-1] == game:
                    return self.index(game)

        else:
            input("Game not found. Press ENTER.")

    def update_game(self):
        """Locates Game object in the list and allows info updates.
        """
        # Get index of game to update
        ndx = self.name_search()

        if ndx:
            options = {
                '1': ("Name", self[ndx].set_name),
                '2': ("System", self[ndx].set_system),
                '3': ("Played", self[ndx].set_played),
                '4': ("Completed", self[ndx].set_completed)
            }

            # Display menu and get returned method to call
            method = GamesList.menu_display(options)

            # Get replacement info and call method using it
            update = input("New info: ")
            method(update)

            # Sort, view, and write list
            self.sort()
            self.view_games()
            self.write_file()

    def remove_game(self):
        """Locates and deletes Game object from the list.
        """
        # Get index of game to remove
        ndx = self.name_search()

        if ndx:
            # Display game info
            GamesList.disp_header()
            print(self[ndx])

            # Get user input and remove Game object by index
            if input("Remove? (y/n): ").lower() == 'y':
                del self[ndx]

                # View and write list
                self.view_games()
                self.write_file()

    @staticmethod
    def menu_display(options):
        """Displays menu to console and returns a value from tuple 
        based on user selection.
        """
        while True:
            disp_art()
            # Display menu
            for num, pair in options.items():
                print(f"\t  [{num}]: {pair[0]}")

            # Get user selection and return
            sel = input("\nSelection: ")
            if options.get(sel):
                return options.get(sel)[1]

            input("ENTER to try again...")
