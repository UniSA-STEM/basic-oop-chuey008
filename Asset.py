"""
File: Asset.py
Description: <The class represents a digital Asset object that has a name, description, a new Boolean attribute that is encrypted.>
Author: <Emily Chuong>
ID: <110448094>
Username: <Chuey008>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    """
    Represents a digital asset and checks to see if the asset is encrypted
    """
    def __init__(self, name, description, encrypted, meta):
        self._name = name
        self._description = description
        self._encrypted = encrypted
        self._meta = meta or {}  # added another attribute, consumable meaning if it gets consumed or destroyed after a single use

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def isEncrypted(self):
        return self._encrypted

    def encrypt(self):
        self._encrypted = True

    def decrypt(self):
        self._encrypted = False

    def getMeta(self):
        return self._meta

    def setMeta(self, meta):
        self._meta = meta

    # String conversion method format as described in the spec sheet
    def __str__(self):
        format_str = f"<{self.getName()}>:<{self.getDescription()}>"
        return f"{format_str} [Encrypted]" if self._encrypted else format_str

# ----------------------Core Assets Section----------------------
class CryptoToken:
    """
    CryptoToken: used to acquire or repair rigs, this is to be used.
    """
    def __init__(self):
        self._name = "CryptoToken"
        self._description = "A single-use token to acquire or repair rigs."
        self._encrypted = False
        self._meta = {"consumable": True}

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def isEncrypted(self):
        return self._encrypted

    def encrypt(self):
        self._encrypted = True

    def decrypt(self):
        self._encrypted = False

    def getMeta(self):
        return self._meta

    def __str__(self):
        format_str = f"<{self.getName()}>:<{self.getDescription()}>"
        return f"{format_str} [Encrypted]" if self._encrypted else format_str

class DataSpike:
    """
    DataSpike: used in battles
    """
    def __init__(self):
        self._name = "DataSpike"
        self._description = "Used to attack rigs."
        self._encrypted = False
        self._meta = {"consumable": True}

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def isEncrypted(self):
        return self._encrypted

    def encrypt(self):
        self._encrypted = True

    def decrypt(self):
        self._encrypted = False

    def getMeta(self):
        return self._meta

    def __str__(self):
        format_str = f"<{self.getName()}>:<{self.getDescription()}>"
        return f"{format_str} [Encrypted]" if self._encrypted else format_str

class RemovableDrive:
    """
    RemovableDrive: found in rigs and used for extraction
    """
    def __init__(self):
        self._name = "RemovableDrive"
        self._description = "Used to extract data from broken rigs."
        self._encrypted = False
        self._meta = {"Consumable": True}

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def isEncrypted(self):
        return self._encrypted

    def encrypt(self):
        self._encrypted = True

    def decrypt(self):
        self._encrypted = False

    def getMeta(self):
        return self._meta

    def __str__(self):
        format_str = f"<{self.getName()}>:<{self.getDescription()}>"
        return f"{format_str} [Encrypted]" if self._encrypted else format_str

class SecurityChip:
    """
    SecurityChip: used to encrypt and decrypt assets
    """
    def __init__(self):
        self._name = "SecurityChip"
        self._description = "Used to encrypt and decrypt assets."
        self._encrypted = False
        self._meta = {"Consumable": False}

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def isEncrypted(self):
        return self._encrypted

    def encrypt(self):
        self._encrypted = True

    def decrypt(self):
        self._encrypted = False

    def getMeta(self):
        return self._meta

    def __str__(self):
        format_str = f"<{self.getName()}>:<{self.getDescription()}>"
        return f"{format_str} [Encrypted]" if self._encrypted else format_str

class HardwarePatch:
    """
    HardwarePatch: used to upgrade rigs
    """
    def __init__(self):
        self._name = "HardwarePatch"
        self._description = "Used to upgrade rigs."
        self._encrypted = False
        self._meta = {"Consumable": True}

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def isEncrypted(self):
        return self._encrypted

    def encrypt(self):
        self._encrypted = True

    def decrypt(self):
        self._encrypted = False

    def getMeta(self):
        return self._meta

    def __str__(self):
        format_str = f"<{self.getName()}>:<{self.getDescription()}>"
        return f"{format_str} [Encrypted]" if self._encrypted else format_str