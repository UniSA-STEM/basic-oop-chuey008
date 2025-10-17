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
        # starting with 2 DataSpikes and 1 RemovableDrive
        self._storage = [DataSpike(), DataSpike(), RemovableDrive()]

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

    def

    def decrypt_asset_in_storage(self, name):
        """
        Decrypt an asset from storage.
        Return False if not found.
        """
        for a in self.

    def take_hit(self):
        effective_threshold = 2 + self.upgrade_level
        self.damage += 1
        if self.damage >= effective_threshold:
            self.broken = True

    def upgrade(self, patch: HardwarePatch) -> bool:
        # consume patch externally (caller removes it from inventory)
        self.upgrade_level += 1
        return True

    def repair(self, token: CryptoToken) -> bool:
        if self.damage == 0 and not self.broken:
            print("No repair needed.")
            return False
        self.damage = 0
        self.broken = False
        return True

