"""
File: Rig.py
Description: <The class represents a computer, that has a name, damage counter (starting at 0), broken state (False) and storage for assets.>
Author: <Emily Chuong>
ID: <110448094>
Username: <Chuey008>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# from asset import Assets, DataSpike, RemovableDrive, CryptoToken, HardwarePatch, SecurityChip

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

    # creating a storage for the asset to be stored and extracted from
    def store_asset(self, asset): self._storage.append(asset)

    def release_asset_by_name(self, n):
        for i, a in enumerate(self._storage):
            if getattr(a, "name", "") == n:  # using getattr to safely access the asset name
                if getattr(a, "encrypted", False): return None  # if it is encrypted it will not release
                return self._storage.pop(i)  # if the asset matches and is not encrypted -> removed and returned
        return None

    def take_hit(self):
        effective_threshold = 2 + self.upgrade_level
        self.damage += 1
        if self.damage >= effective_threshold:
            self.broken = True

    def upgrade(self, patch: HardwarePatch) -> bool:
        #consume patch externally (caller removes it from inventory)
        self.upgrade_level += 1
        return True

    def repair(self, token: CryptoToken) -> bool:
        if self.damage == 0 and not self.broken:
            print("No repair needed.")
            return False
        self.damage = 0
        self.broken = False
        return True

