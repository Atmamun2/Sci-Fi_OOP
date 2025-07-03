'''
This file contains the StationItem class and its subclasses.
'''

class StationItem:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def examine(self):
        return f"{self._name}: {self._description}"
        # Returns a text description specific to the item. Both subclasses override this.

class DiagnosticTool(StationItem):
    def __init__(self, name, description):
        super().__init__(name, description)

    def examine(self):
        print("This diagnostic tool seems designed to interface with maintenance droids. \n")

class EnergyCrystal(StationItem):
    def __init__(self, name, description):
        super().__init__(name, description)

    def examine(self):
        print("The crystal pulses with an unstable, vibrant energy.")
