#!/usr/bin/env python3
"""
Structure verification script for Sci-Fi OOP project.
This script checks that the actual file structure matches the documented structure.
"""

import os
import sys
from pathlib import Path

def check_structure():
    """Verify the project structure matches the README documentation."""
    
    # Expected structure from README.md
    expected_structure = {
        'Sci_Fi_Code/': {
            'Sci_Fi.py': 'Main game implementation'
        },
        'Sci_Fi_Documentation/': {
            'logbook.md': 'Development log',
            'README.md': 'Documentation',
            'Sci_Fi_Flowchart/': {
                'OOP_SciFi_Flowchart.drawio': 'Game flow diagram',
                'Sci_Fi_Movement_Flowchart.drawio': 'Movement flowchart',
                'Sci_Fi_Use_Tool.drawio': 'Tool usage flowchart'
            },
            'Sci_Fi_Storyboard/': {
                'OOP_Sci_Fi_Storyboard.drawio': 'Storyboard diagram',
                'OOP_SciFi_Storyboard.drawio': 'Alternative storyboard'
            }
        },
        'README.md': 'Main project documentation'
    }
    
    print("🔍 Checking Sci-Fi OOP Project Structure...")
    print("=" * 50)
    
    all_good = True
    
    def check_directory(path, expected_items, indent=0):
        nonlocal all_good
        prefix = "  " * indent
        
        if not os.path.exists(path):
            print(f"{prefix}❌ Missing: {path}")
            all_good = False
            return
        
        print(f"{prefix}📁 {path}/")
        
        for item, description in expected_items.items():
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                if isinstance(description, dict):
                    check_directory(item_path, description, indent + 1)
                else:
                    print(f"{prefix}  📁 {item}/ - {description}")
            else:
                if os.path.exists(item_path):
                    print(f"{prefix}  ✅ {item} - {description}")
                else:
                    print(f"{prefix}  ❌ Missing: {item} - {description}")
                    all_good = False
    
    # Check root level files
    for item, description in expected_structure.items():
        if item.endswith('/'):
            # Directory
            dir_name = item[:-1]
            check_directory(dir_name, expected_structure[item])
        else:
            # File
            if os.path.exists(item):
                print(f"✅ {item} - {description}")
            else:
                print(f"❌ Missing: {item} - {description}")
                all_good = False
    
    print("=" * 50)
    if all_good:
        print("🎉 All files and directories are present and match the README structure!")
        print("✅ Project structure is correctly implemented.")
    else:
        print("⚠️  Some files or directories are missing.")
        print("❌ Project structure needs to be completed.")
    
    return all_good

def show_structure():
    """Display the current project structure."""
    print("📂 Current Project Structure:")
    print("=" * 50)
    
    def print_tree(path, prefix="", is_last=True):
        if not os.path.exists(path):
            return
        
        items = os.listdir(path)
        items = [item for item in items if not item.startswith('.')]  # Skip hidden files
        items.sort()
        
        for i, item in enumerate(items):
            item_path = os.path.join(path, item)
            is_last_item = i == len(items) - 1
            
            if os.path.isdir(item_path):
                print(f"{prefix}{'└── ' if is_last_item else '├── '}{item}/")
                new_prefix = prefix + ('    ' if is_last_item else '│   ')
                print_tree(item_path, new_prefix, is_last_item)
            else:
                print(f"{prefix}{'└── ' if is_last_item else '├── '}{item}")
    
    print_tree(".")
    print("=" * 50)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--show":
        show_structure()
    else:
        check_structure() 