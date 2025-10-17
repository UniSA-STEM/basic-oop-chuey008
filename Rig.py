"""
File: Rig.py
Description: <The class represents a computer, that has a name, damage counter (starting at 0), broken state (False) and storage for assets.>
Author: <Emily Chuong>
ID: <110448094>
Username: <Chuey008>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import DataSpike, RemovableDrive, CryptoToken, HardwarePatch, SecurityChip

class Rig:
    """
    Creating a rig that contains the below attributes.
    """
    def __init__(self, name: str):
        self._name = name
        self._damage = 0
        self._broken = False
        self._upgrade_level = 0
        self._storage = [DataSpike(), DataSpike(), RemovableDrive()]  # starting with 2 DataSpikes and 1 RemovableDrive

    # ----------------------Public Storage API Section----------------------
    # creating a storage for the asset to be stored and extracted from
    def store_asset(self, asset):
        self._storage.append(asset)

    # checks to see if there are any assets in storage
    def has_asset(self, name):
        return any(a.name == name for a in self._storage)

    def release_asset_by_name(self, n):
        """
        Remove and return the first matching asset by name if it is not encrypted.
        Return Empty if missing or encrypted.
        """
        for i, a in enumerate(self._storage):
            if a.name == n:  # directly accesses the asset's name
                if a.encrypted:  # checks if asset is encrypted
                    return None # if encrypted it will not release
                return self._storage.pop(i)  # return and remove encrypted asset
        return None

    def release_all_unencrypted(self):
        """
        Remove and return all unencrypted assets. Used for extraction.
        """
        unencrypt = [a for a in self._storage if not a.encrypted is False]  # not sure if this is needed
        self._storage = [a for a in self._storage if a.encrypted is False]  # check
        return unencrypt

    def get_storage_summary(self, name):
        """
        Return a summary of what is currently stored inside storage.
        Read-only, for testing purposes.
        """
        return [a.name for a in self._storage]

    def encrypt_asset_in_storage(self, name):
        """
        Encrypt an asset by name in storage.
        Return False if asset is not found.
        """
        for a in self._storage:
            if a.name == name:
                a.encrypt()
                return True
            return False

    def decrypt_asset_in_storage(self, name):
        """
        Decrypt an asset from storage.
        Return False if not found.
        """
        for a in self._storage:
            if a.name == name:
                a.decrypt()
                return True
            return False

    # ---------------------- Damage/ Repair/ Upgrade Section----------------------
   def damage_threshold(self):
       """
       Base threshold is 2 plus the upgrade level. Used to calculate when the rig breaks.
       The more upgrades the rig has, the more damage it can take
       """
       return 2 + self._upgrade_level

    def take_hit(self):
        """
        Apply a single hit, rig is broken if threshold of damage is reached.
        """
        if self._broken:  # if rig is already broken, does nothing
            return
        self._damage += 1
        if self._damage >= self.damage_threshold():
            self._broken = True

    def repair(self, token: object):
        """
        Repair with a CryptoToken. Hacker will consume token.
        Returns False if no CryptoToken or if nothing is used to repair rig.
        """
        if not isinstance (token, CryptoToken):  # checks if the object is valid, e.g. CryptoToken
            return False
        if self._damage == 0 and not self._broken:  # if the rig isn't damaged or broken
            print(f"{self._name}: No repair is needed.")
            return False
        self._damage = 0  # reset back to 0
        self._broken = False
        return True

    def upgrade(self, patch: object):
        """
        Upgrade rig using a HardwarePatch. Hack will consume patch.
        Returns True on success.
        """
        if not isinstance(patch, HardwarePatch):  # checks if the object is valid, e.g. HardwarePatch
            return False
        self._upgrade_level += 1
        return True

