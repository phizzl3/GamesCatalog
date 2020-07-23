"""This script is mainly me practicing a couple of different ways to use OOP/Classes 
in python.
It is used to maintain a list of games, their systems and completion status.
Yes, I realize OOP may not be the best way of doing some of this, but I'm new to it. 
"""



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

