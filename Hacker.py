"""
File: Hacker.py
Description: <The class represents a hacker with a name, has a CryptoToken, trace level, able to launch data spike
from rigs, encrypt their assets, upgrade their rig through a Hardware Patch, store and retrieve assets.>
Author: <Emily Chuong>
ID: <110448094>
Username: <Chuey008>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
from Rig import Rig

class Hacker:
    """
    Represents a Hacker with an inventory, a rig and trace level with a level and threshold.
    Inventory will hold the Assets and contains one CryptoToken.
    """
    def __init__(self, name: str):
        self._name = name
        self._inventory = [CryptoToken()]
        self._rig = None
        self._trace_level = 0
        self._trace_threshold = 5

    # ---------------------- Inventory Enablers Section----------------------
    def find_index_by_class(self, cls):
        """
        Return index of first item that is the instance of a given class (cls), or None.
        Used to locate items like DataSpike and RemovableDrive.
        """
        for i, a in enumerate(self._inventory):
            if isinstance(a, cls):
                return i
        return None

    def find_index_by_name(self, name):
        """
        Return index of first item with matching _name or class name.
        """
        for i, a in enumerate(self._inventory):
            try:
                if a._name == name or type(a).__name__ == name:
                    return i
            except AttributeError:  # if a doesn't have _name, catches the AttributeError and checks the class name
                if type(a).__name__ == name:
                    return i
        return None

    def add_to_inventory(self, Asset: object):
        """
        Add an asset to the inventory.
        """
        self._inventory.append(Asset)

    def scan_inventory_for(self, name: str):
        """
        Scans the inventory for a certain item by _name or class name.
        """
        item = self._find_item_by_name(name)
        if item is None:
            return None
        return self._inventory.pop(item)

    def inventory_summary(self):
        """
        Returns a simple summary of the inventory contents to be displayed.
        """
        if not self._inventory:
            return "Empty Inventory"
        return "; ".join(str(a) for a in self._inventory)

    def acquire_rig(self, rig=None):
        """
        Acquiring a rig using the already given CryptoToken
        Checks to see if a rig already exists using a Boolean and if it doesn't exist
        Will create one if the Hacker has a CryptoToken in their inventory
        """
        if self.rig:
            print("Rig already acquired.")
            return False
        if rig is None:
            self.rig = Rig(f"{self.name}'s Rig")
        else:
            self.rig = rig
        #Consume one CryptoToken
        token = self.scan_inventory_for_type(CryptoToken)  # scans for a CryptoToken to be used to acquire a rig
        if token:
            self.inventory.remove(token)
            print(f"{self.name} acquired rig: {self.rig.name}")
            return True
        else:
            print("No CryptoToken to activate rig")
            return False

    def launch_data_spike(self, target_rig: Rig) -> bool:
        """
        Launching Data Spikes on other rigs and consuming a Data Spike from their own rig storage
        Checks to see if there is a rig to launch Data Spikes from
        True if there is, False if there isn't.
        """
        if self.rig is None:
            print("No rig to launch spikes from.")  # checks to see if a rig exists
            return False
        if self.trace_level > self.trace_threshold:  # trace level greater than trace threshold than no launch of data spike
            print("Trace level is too high to launch attack.")
            return False
        spike = self.rig.release_asset_by_name('DataSpike')
        if spike is None:
            print("No Data Spike is available.")
            return False
        target_rig.take_hit()
        self.increase_trace(2)
        return True


