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
    def __init__(self, name: str, description: str, encrypted: bool = False, meta: Dict = None) -> None:
        self.name = name
        self.description = description
        self.encrypted = encrypted
        self.meta = dict(meta) if meta else {}      # added another attribute to the asset

    def encrypt(self):
        self.encrypted = True

    def decrypt(self):
        self.encrypted = False

# String conversion method format as described in the spec sheet
    def __str__(self):
        format = f"{self.name}: {self.description}"
        return f"{format} [Encrypted]" if self.encrypted else format

class CryptoToken:
    """CryptoToken: used to acquire or repair rigs, this is to be used."""
    def __init__(self) -> None:
        self.name = "CryptoToken"
        self.description = "A single-use token to acquire or repair rigs."
        self.encrypted = False
        self.meta = {"consumable": True}



