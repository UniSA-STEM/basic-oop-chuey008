"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# File: Hacker.py
# Description: This class represents a hacker that has a name, a rig name, trace level and inventory contents.
# Author: Emily Chuong
# ID: 110448094
# Username: Chuey008
# This is my own work as defined by the University's Academic Misconduct Policy.

class Hacker:
    """Represents a Hacker with an inventory, a rig and trace level with a level and threshold.
    Inventory will hold the Assets and contains one CryptoToken."""
    def __init__(self, name):
        self.name = name
        self.inventory: List[Asset] = [CryptoToken()]
        self.rig = None
        self.trace_level = 0
        self.trace_threshold = 5

