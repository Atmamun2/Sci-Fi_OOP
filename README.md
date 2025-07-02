# Sci-Fi OOP Adventure Game

A text-based adventure game built with Object-Oriented Programming principles, set in a futuristic space station where players must navigate through maintenance tunnels, interact with droids, and collect items to escape.

## 🚀 Features

- **Object-Oriented Design**: Clean separation of concerns with distinct classes for different game entities
- **Interactive Gameplay**: Text-based commands for movement, item collection, and puzzle solving
- **Dynamic Environment**: Locations that change based on player actions
- **Scoring System**: Points awarded for successful actions and hazard tracking
- **Item Management**: Collect and use tools to solve obstacles
- **Win Condition**: Escape the station by collecting the energy crystal and reaching the docking bay

## 🎮 Game Mechanics

### Locations
- **Maintenance Tunnels**: Starting location with a diagnostic tool and a blocking droid
- **Docking Bay**: Final destination with an energy crystal

### Items
- **Diagnostic Tool**: Used to repair the damaged maintenance droid
- **Energy Crystal**: Required item to win the game

### Characters
- **Player**: The main character who navigates the station
- **Damaged Maintenance Droid**: Obstacle that blocks the path until repaired

### Commands
- `move <direction>` - Move in a specified direction (e.g., "move east")
- `pick up tool` - Collect the diagnostic tool
- `pick up crystal` - Collect the energy crystal
- `use tool` - Repair the damaged droid
- `status` - Check current score, hazards, and location
- `win` - Escape the station (only available when conditions are met)

## 🏗️ Code Structure

### Core Classes

#### `StationItem` (Base Class)
- Abstract base class for items in the game
- Subclasses: `DiagnosticTool`, `EnergyCrystal`

#### `Location`
- Represents game locations with descriptions, exits, and item states
- Manages location-specific properties (tools, crystals, droids)

#### `DamagedMaintenanceDroid`
- Represents the blocking droid obstacle
- Can be repaired using the diagnostic tool

#### `Player`
- Manages player state (location, inventory, score, hazards)
- Handles movement, item collection, and tool usage

#### `GameController`
- Main game loop and command processing
- Manages game state and win conditions

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Sci-Fi_OOP
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

3. Run the game:
```bash
python Sci_Fi_Code/Sci_Fi.py
```

## 🎯 How to Play

1. **Start the Game**: Enter your name when prompted
2. **Explore**: Use `move east` to navigate between locations
3. **Collect Items**: Pick up the diagnostic tool in the maintenance tunnels
4. **Solve Puzzles**: Use the tool to repair the damaged droid
5. **Progress**: Move to the docking bay and collect the energy crystal
6. **Win**: Type `win` to escape the station

### Game Flow
1. Start in Maintenance Tunnels
2. Pick up the diagnostic tool
3. Use the tool on the damaged droid
4. Move east to the Docking Bay
5. Pick up the energy crystal
6. Type "win" to complete the game

## 📊 Scoring System

- **Pick up diagnostic tool**: +10 points
- **Repair droid**: +20 points
- **Pick up energy crystal**: +50 points
- **Escape station**: +30 points
- **Hazard encounters**: Tracked separately (increases when blocked by droid)

## 🔧 Technical Details

### Object-Oriented Design Principles

- **Encapsulation**: Private attributes with controlled access
- **Inheritance**: `StationItem` as base class for items
- **Polymorphism**: Different `examine()` methods for items
- **Composition**: Locations contain items and droids

### Key Design Patterns

- **Command Pattern**: Centralized command processing in `GameController`
- **State Management**: Location and player state tracking
- **Observer Pattern**: Location descriptions update based on player actions

## 📁 Project Structure

```
Sci-Fi_OOP/
├── Sci_Fi_Code/
│   └── Sci_Fi.py          # Main game implementation
├── Sci_Fi_Documentation/
│   ├── logbook.md         # Development log
│   ├── README.md          # Documentation
│   ├── Sci_Fi_Flowchart/  # Game flow diagrams
│   └── Sci_Fi_Storyboard/ # Visual storyboards
└── README.md              # This file
```

## 🎨 Game Features

- **Dynamic Descriptions**: Location descriptions change based on player actions
- **Context-Aware Commands**: Available actions update based on current state
- **Error Handling**: Graceful handling of invalid commands
- **State Persistence**: Game state maintained throughout the session

## 🔮 Future Enhancements

- Additional locations and items
- More complex puzzle mechanics
- Save/load game functionality
- Multiple difficulty levels
- Sound effects and visual improvements
- Multiplayer support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as an educational project demonstrating Object-Oriented Programming concepts in game development.

---

**Enjoy your adventure in the Sci-Fi Station!** 🚀 