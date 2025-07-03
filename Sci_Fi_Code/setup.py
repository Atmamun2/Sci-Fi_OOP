import settings, utils
from settings import Location, DamagedMaintenanceDroid
from utils import DiagnosticTool, EnergyCrystal

'''
Another wey to verify the drone's existence in the location is:
# # Assume the droid object is accessible as self.current_location.droid
# if hasattr(self.current_location, 'droid') and self.current_location.droid:
checking if the current location has the attribute of droid.
'''

class GameController:
    def __init__(self):
        # location instances
        maint_tunnels = Location(
            name="Maintenance Tunnels",
            description="You're in the dim Maintenance Tunnels. Exposed wires hum with residual power. A diagnostic tool glows on the floor.\nTo the EAST, a flickering service droid blocks the path, its circuits sparking erratically.",
            exits={},
            has_tool=True,
            has_crystal=False,
            droid_present=True
        )
        docking_bay = Location(
            name="Docking Bay",
            description="A vast open space where ships dock and depart.",
            exits={},
            has_tool=False,
            has_crystal=True,
            droid_present=False
        )

        # Link locations
        maint_tunnels.add_exit("east", docking_bay)
        docking_bay.add_exit("west", maint_tunnels)
        # Instantiate droid and assign to maintenance tunnels
        droid = DamagedMaintenanceDroid(blocking=True)
        maint_tunnels.droid = droid
        # Instantiate tool and crystal
        diagnostic_tool = DiagnosticTool("Diagnostic Tool", "A device for interfacing with droids.")
        energy_crystal = EnergyCrystal("Energy Crystal", "A glowing, unstable power source.")
        # Instantiate player
        player = Player(name=input("Enter your name: "), current_location=maint_tunnels, has_tool=False, has_crystal=False, score=0, hazard_count=0)
        # Store references
        self.maintanence_tunnels = maint_tunnels
        self.docking_bay = docking_bay
        self.droid = droid
        self.diagnostic_tool = diagnostic_tool
        self.energy_crystal = energy_crystal
        self.player = player

    def start_game(self):
        print(f"Welcome to the Sci-Fi Adventure, {self.player.name}!")
        while True:
            self.player.current_location.describe()
            
            # # Show available exits
            # exits = ", ".join(self.player.current_location.exits.keys())
            # print(f"\nExits: {exits}")
            
            # Show available actions
            print("\nAvailable actions:")
            print("- move <direction> (e.g., 'move east')")
            if self.player.current_location.has_tool and not self.player.has_tool:
                print("- pick up tool")
            if self.player.current_location.has_crystal and not self.player.has_crystal:
                print("- pick up crystal")
            if self.player.current_location.droid_present and self.player.has_tool:
                print("- use tool")
            print("- status (check your score and hazards)")
            if self.player.current_location == self.docking_bay and self.player.has_crystal:
                print("- win (escape the station!)")
                
            command = input("\nWhat do you want to do? ").strip().lower()
            self.process_input(command) 
            if self.check_win_condition():
                break

    def process_input(self, command):
        self.last_command = command
        cmd = command.strip().lower()
        # Handle 'move <direction>' separately
        if cmd.startswith("move "):
            direction = cmd[5:].strip()
            self._handle_move(direction)
            return
        # Command map for exact matches
        command_map = {
            "pick up tool": self._handle_pick_up_tool,
            "use tool": self._handle_use_tool,
            "pick up crystal": self._handle_pick_up_crystal,
            "status": self._handle_status,
            "win": lambda: None
        }
        handler = command_map.get(cmd, self._handle_invalid)
        handler()

    def _handle_move(self, direction):
        success = self.player.move(direction)
        if success:
            print(f"You move {direction}.")
        else:
            if direction not in self.player.current_location.exits:
                print("You can't go that way.")
            elif self.player.current_location.droid_present:
                print("A maintenance droid blocks your way!")
            else:
                print("You can't go that way.") 

    def _handle_pick_up_tool(self):
        if self.player.pick_up_tool():
            self.maintanence_tunnels.description = "The tunnels are quieter now. The droid still blocks the east exit, whirring in distress."
        else:
            print("There is no tool to pick up.") 

    def _handle_use_tool(self):
        if self.player.use_tool_on_droid():
            self.maintanence_tunnels.description = "The tunnels are quiet now. The droid no longer blocks the east exit."
        else:
            print("Nothing happens.")

    def _handle_pick_up_crystal(self):
        if self.player.pick_up_crystal():
            self.docking_bay.description = "The crystal glows with a steady, stable energy. The docking bay is now safe to enter."
        else:
            print("There is no crystal to pick up.") 

    def _handle_status(self):
        print(self.player.get_status())

    def _handle_invalid(self):
        print("Invalid command. \n")

    def check_win_condition(self):
        # Check if the player is in Docking Bay, has the crystal, and last command was 'win'
        if (
            self.player.current_location == self.docking_bay and
            self.player.has_crystal and
            getattr(self, 'last_command', '').strip().lower() == 'win'
        ):
            self.player.score += 30
            print(f"You escaped the Sci-Fi Station! \n")
            print(f"Mission complete! (Final Score: {self.player.score} | Total Hazards: {self.player.hazard_count})")
            return True
        return False
    
class Player:
    def __init__(self, name, current_location, has_tool, has_crystal, score, hazard_count):
        self.name = name
        self.current_location = current_location
        self.has_tool = False
        self.has_crystal = False
        self.score = 0
        self.hazard_count = 0

    def move(self, direction):
        # Check if the direction exists in the current location's exits
        if direction not in self.current_location.exits:
            return False  # No tangible exit exists
        # Check if a droid is present and blocking
        if self.current_location.droid_present:
            self.hazard_count += 1
            return False  # Droid is blocking
        # Move to the new location
        self.current_location = self.current_location.exits[direction]
        return True
        
    def pick_up_tool(self):
        if self.current_location.has_tool:
            self.current_location.has_tool = False
            self.has_tool = True
            self.score += 10
            print(f"You pick up the diagnostic tool. (Score: {self.score} | Hazards: {self.hazard_count})")
            return True
        else:
            print("There is no tool to pick up. \n")
            return False
            
    def use_tool_on_droid(self):
        if self.has_tool and self.current_location.droid_present:
            self.current_location.droid.repair()
            self.current_location.droid_present = False
            self.score += 20
            print(f"You use the tool to repair the droid. It moves aside! (Score: {self.score} | Hazards: {self.hazard_count})")
            return True
        else:
            return False

    def pick_up_crystal(self):
        if self.current_location.has_crystal:
            self.current_location.has_crystal = False
            self.has_crystal = True
            self.score += 50
            print(f"You pick up the energy crystal. (Score: {self.score} | Hazards: {self.hazard_count})")
            return True
        else:
            print("There is no crystal to pick up. \n")
            return False
        
    def get_status(self):
        return f"You have {self.score} points, {self.hazard_count} hazards, and are in the {self.current_location.name}."