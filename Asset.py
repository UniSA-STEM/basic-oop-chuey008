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

"""Using subclasses to inherit from the parent class of Asset and adds a description as to what it's used for as per the spec sheet"""
class CryptoToken(Asset):
    def __init__(self):
        super().__init__("CryptoToken", "Used to acquire or repair rigs.")

class DataSpike(Asset):
    def __init__(self):
        super().__init__("DataSpike", "Used in battles.")

class RemovableDrive(Asset):
    def __init__(self):
        super().__init__("RemovableDrive","Found in rigs and used for extraction.")

class SecurityChip(Asset):
    def __init__(self):
        super().__init__("SecurityChip", "Used to encrypt or decrypt assets.")

class HardwarePatch(Asset):
    def __init__(self):
        super().__init__("HardwarePatch", "Used to upgrade rigs.")