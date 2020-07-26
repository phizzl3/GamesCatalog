"""This script is mainly me practicing a couple of different ways to use OOP/Classes 
in python.
It is used to maintain a list of games, their systems and completion status.
Yes, I realize OOP may not be the best way of doing some of this, but I'm new to it. 
"""


import random
from pathlib import Path


from art import disp_art



FILE = f"{Path(__file__).resolve().parent}/games.csv"


class Game:

    # Class attribute used to count the number of game objects created
    number_of_games = 0

    def __init__(self, name, system, played, completed):
        # Initialize the attributes for each object created using the Class
        # Set each attribute
        # Add to number of games each time a Game object is created
        self.name = name
        self.system = system
        self.played = played
        self.completed = completed
        Game.number_of_games += 1

    def __str__(self):
        # Create my own string output for my objects
        return f"{self.name:43}: {self.system:>6} - {self.played:>6} - {self.completed:>9}"

    def __eq__(self, other):
        # set up equal to
        return self.name == other.name and self.system == other.system

    def __lt__(self, other):
        # Create less than comparison to use to compare objects for sort function
        return self.name < other.name

    @classmethod
    def get_total_games(cls):
        """Returns the total number of games (Class objects)."""
        return cls.number_of_games

    def set_name(self, name):
        """Allows for changing the object's name."""
        self.name = name

    def set_system(self, system):
        """Allows for changing the object's system."""
        self.system = system

    def set_played(self, played):
        """Allows for changing the object's played status."""
        self.played = played

    def set_completed(self, completed):
        """Allows for changing the object's completion status."""
        self.completed = completed


class GamesList(list):

    def read_data(self):
        """Read data from csv file, creates Games objects and 
        compiles a list object.
        """

        with open(FILE, 'r') as f:
            for line in f:
                nm, sy, pl, cp = line.strip('\n').split(',')
                self.append(Game(nm, sy, pl, cp))

    def write_file(self):
        """Writes data to csv file after confirming changes."""

        save = input("Save changes? (y/n): ")
        if save.lower() == 'y':
            with open(FILE, "w") as f:
                for game in self:
                    f.write(
                        f"{game.name},{game.system},{game.played},{game.completed}\n")

    @staticmethod
    def disp_header():

        disp_art()

        # Print header
        print("{:43}: {:>6} - {:>6} - {:>9}".format(
            "Game", "System", "Played", "Completed"
        ))
        print("="*72)

    def view_games(self):
        """Prints Games items from list to console.
        Switches output colors on each print."""


        GamesList.disp_header()

        for game in self:
            print(game)


        input("\nENTER to return...")

    def random_game(self):
        """Randomly pull a game from the list and display to console."""

        GamesList.disp_header()
        print(random.choice(self))

        input("\nENTER to return...")

    def search_games(self):  # TODO
        """Allows for search of list of Games objects by name, system,
        played, and completion and prints to console.
        """

        options = {     # TODO: FIX THIS
            '1': ('Name', '1'),
            '2': ('System', '2'),
            '3': ('Played', '3'),
            '4': ('Completed', '4')
        }

  

        sel = GamesList.menu_display(options)

        to_find = input("Search string: ")

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
        """Creates a new Game object and adds it to the games list."""

        nm = input("Game name: ")
        sy = input("Which system: ")
        pl = input("Played it?: ")
        cp = input("Finished it?: ")

        self.append(Game(nm, sy, cp, pl))

        self.sort()
        self.view_games()
        self.write_file()

    def name_search(self):
        """Searches for Game object in the list by name and returns
        the located Game object's list index.
        """

        find = input("Enter at least 3 letters to search: ")

        found = [g for g in self if find.lower() in g.name.lower()]

        if found:
            for i, gm in enumerate(found, 1):
                print(f"{i}: {gm}")

            sel = input("Selection: ")

            for game in self:
                if found[int(sel)-1] == game:
                    return self.index(game)

        else:
            input("Game not found. Press ENTER.")

    def update_game(self):
        """Locates Game object in the list and allows info updates."""

        ndx = self.name_search()

        if ndx:
            options = {
                '1': ("Name", self[ndx].set_name),
                '2': ("System", self[ndx].set_system),
                '3': ("Played", self[ndx].set_played),
                '4': ("Completed", self[ndx].set_completed)
            }

            # method_call = menu_display(options) #TODO

            method = GamesList.menu_display(options)

            update = input("New info: ")

            method(update)

            self.sort()

            self.view_games()
            self.write_file()

    def remove_game(self):
        """Locates and deletes Game objects from the list."""

        ndx = self.name_search()

        if ndx:

            [self[ndx]].view_games()

            if input("Remove?: ").lower() == 'y':
                del self[ndx]
                self.view_games()
                self.write_file()

    @staticmethod
    def menu_display(options):

        while True:
            disp_art()
            for num, pair in options.items():
                print(f"\t  [{num}]: {pair[0]}")

            sel = input("\nSelection: ")
            if options.get(sel):
                return options.get(sel)[1]
                
            input("ENTER to try again...")
