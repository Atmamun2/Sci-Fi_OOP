import utils, setup
from utils import DiagnosticTool, EnergyCrystal
from setup import GameController

'''
This file contains the Location class and the DamagedMaintenanceDroid class.
'''

class Location:
    def __init__(self, name, description, exits, has_tool, has_crystal, droid_present):
        self.name = name
        self.description = description
        self.exits = exits
        self.has_tool = has_tool
        self.has_crystal = has_crystal
        self.droid_present = droid_present

    def add_exit(self, direction, other_location):
        self.exits[direction] = other_location

    def describe(self):
        print(self.name + "\n" + self.description + "\n")
        if self.has_tool:
            print(f"You see a diagnostic tool here. \n")
        if self.has_crystal:
            print("You see an energy crystal here. \n")
        if self.droid_present:
            print("A maintenance droid blocks the way! \n")
        print(f"Exits: {', '.join(self.exits.keys())}.")

    def remove_tool(self):
        if self.has_tool:
            self.has_tool = False
            return True
        else:
            return False
            
    def remove_crystal(self):
        if self.has_crystal:
            self.has_crystal = False
            return True
        else:
            return False
        
    def set_droid_present(self, present):
        self.droid_present = present

class DamagedMaintenanceDroid:
    def __init__(self, blocking):
        self.blocking  = True

    def repair(self):
        self.blocking = False
        return self.blocking

    def is_blocking(self):
        if self.blocking:
            print("The droid is still blocking the way. \n")
            return True
        else:
            print("The droid is no longer blocking the way. \n")
            return False