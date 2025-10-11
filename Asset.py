"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# File: Asset.py
# Description: The class represents a digital Asset object that has a name, description, a new Boolean attribute that is encrypted.
# Author: Emily Chuong
# ID: 110448094
# Username: Chuey008
# This is my own work as defined by the University's Academic Misconduct Policy.

class Asset:
    """Represents a digital asset and checks to see if the asset is encrypted"""
    def __init__(self, name: str, description: str, encrypted: bool = False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def encrypt(self):
        self.encrypted = True

    def decrypt(self):
        self.encrypted = False

    def __str__(self):
        s = f"{self.name}: {self.description}"
        return f"{s} [Encrypted:" if self.encrypted else s

