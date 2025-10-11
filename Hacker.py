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

    """Acquiring a rig using the already given CryptoToken
    Checks to see if a rig already exists using a Boolean and if it doesn't exist
    Will create one if the Hacker has a CryptoToken in their inventory"""
    def acquire_rig(self, rig=None):
        if self.rig:
            print("Rig already acquired.")
            return False
        if rig is None:
            self.rig = Rig(f"{self.name}'s Rig")
        else:
            self.rig = rig
        #Consume one CryptoToken
        token = self.scan_inventory_for_type(CryptoToken)  #scans for a CrytoToken to be used to acquire a rig
        if token:
            self.inventory.remove(token)
            print(f"{self.name} acquired rig: {self.rig.name}")
            return True
        else:
            print("No CryptoToken to activate rig")
            return False

