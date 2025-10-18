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
    def __init__(self, name):
        self._name = name
        self._inventory = [CryptoToken()]
        self._rig = None
        self._trace_level = 0
        self._trace_threshold = 5

    # ---------------------- Inventory Enablers Section----------------------
    def find_index_by_name(self, name):
        """
        Search inventory for first asset whose name or class matches given class.
        Return matching, None if not found.
        """
        for i, asset in enumerate(self._inventory):
            if asset.getName() == name or type(asset).__name__ == name:
                return i
        return None

    def find_index_by_class(self, cls):
        """
        Search inventory for first asset that is an instance of given class.
        Returns matching, None if not found.
        """
        for i, asset in enumerate(self._inventory):
            if isinstance(asset, cls):
                return i
            return None

    def add_to_inventory(self, asset):
        """
        Add an asset to the inventory.
        """
        self._inventory.append(asset)

    def scan_inventory_for(self, name):
        """
        Scans the inventory for a certain item by _name or class name.
        Removes the first asset in inventory that matches the given name.
        """
        idx = self.find_index_by_name(name)  # find index of matching asset
        if idx is None:
            return None
        return self._inventory.pop(idx)  # remove and return the asset

    def inventory_summary(self):
        """
        Generates and returns a simple summary of the inventory contents to be displayed.
        """
        if not self._inventory:
            return "Empty Inventory"
        return "; ".join(str(a) for a in self._inventory)

    # ---------------------- Trace Management Section----------------------
    def increase_trace(self, amount=None):
        """
        Increases the hacker's trace level by given amount.
        Defaults to one if none is specified.
        """
        if amount is None:
            amount = 1
        self._trace_level += amount

    def reduce_trace(self, amount=None):
        """
        Reduces the hacker's trace level by given amount.
        Stops at zero.
        """
        if amount is None:
            amount = 1
        self._trace_level = max(0, self._trace_level - amount)  # cannot fall below zero

    def is_exposed(self):
        """
        Checks to see if the hacker's trace level exceeds the threshold.
        Returns True if exposed and False otherwise.
        """
        return self._trace_level > self._trace_threshold

    # ---------------------- Rig Management Section----------------------
    def acquire_rig(self):
        """
        Acquiring a rig using the already given CryptoToken.
        Checks to see if a rig already exists using a Boolean and if it doesn't exist
        Will create one if the Hacker has a CryptoToken in their inventory
        """
        token_idx = self.find_index_by_name("CryptoToken")  # scans for a CryptoToken to be used to acquire a rig
        if token_idx is None:
            print(f"{self._name}: Need a CryptoToken to acquire a rig")
            return False

        self._rig = Rig(f"{self._name}'s Rig")  # create and assign a new rig

        self._inventory.pop(token_idx)  # remove the CryptoToken from inventory

        print("{self._name} activated rig a rig")
        return True

    def upgrade_rig(self):
        """
        Upgrade the rig using a HardwarePatch from inventory.
        Returns True if upgrade is successful, False otherwise.
        """
        if self._rig is None:
            print(f"{self._name}: No rig to upgrade")
            return False

        patch_idx = self.find_index_by_name("HardwarePatch")
        if patch_idx is None:
            print(f"{self._name}: No HardwarePatch is available.")
            return False

        # Remove patch and apply upgrade
        patch = self._inventory.pop(patch_idx)
        success = self._rig.upgrade(patch)

        if success:
            print(f"{self._name}: Upgraded rig to level {self._rig.get_upgrade_level()}.")
        return success

    def repair_rig(self):
        """
        Repairs the rig using a CryptoToken from inventory and is consumed.
        """
        if self._rig is None:
            print(f"{self._name}: No rig to repair.")
            return False

        token_idx = self.find_index_by_class(CryptoToken)
        if token_idx is None:
            print(f"{self._name}: No CryptoToken is available for repair")
            return False

        # Remove token and attempt to repair
        token = self._inventory.pop(token_idx)
        success = self._rig.repair(token)

        if success:
            print(f"{self._name}: Repaired rig {self._rig.get_name()}.")
        return success

    # ---------------------- Battle Section----------------------
    def launch_data_spike(self, target, spikes):
        """
        Launching Data Spikes on target rig, successful launch increases trace level by 2.
        Does not launch if target rig becomes broken.
        Checks to see if there is a rig to launch Data Spikes from
        True if there is, False if there isn't.
        """
        if self._rig is None:
            print(f"{self._name}: No rig to launch spikes from.")  # checks to see if a rig exists
            return False

        if self.is_exposed():
            print(f"{self.get_name()}: Trace level is too high to launch attack.")
            return False

        if target is None:  # checks to see if there is a target to launch DataSpike at
            print(f"{self._name}: No target rig detected.")
            return False

        launched = 0  # count successful launches

        for _ in range(spikes):
            spike = self._rig.release_asset_by_name("DataSpike")  # try to release a DataSpike from rig Storage
            if spike is None:
                print(f"{self._name}: No DataSpike is available in this rig.")
                continue

            # apply damage to target and increase trace
            target.take_hit()
            self.increase_trace(2)
            launched += 1

            print(f"{self._name}: Launched DataSpike at {target.get_name()}; target damage now {target.get_damage()}.")

            if target.is_broken():  # stops if rig is broken
                print(f"{target.get_name()} is broken.")
                break

        return launched > 0

    # ---------------------- Extraction Section----------------------
    def extract_from_rig(self, target):
        """
        Extract all unencrypted assets from a broken rig using a RemovableDrive in inventory.
        Increases trace level by 3 after extraction
        Consumes the RemovableDrive and transfers unencrypted assets to hacker's inventory.
        """
        if not target.is_broken():  # checks to see if the targeted rig is broken
            print(f"{self._name}: Target rig is not broken; cannot extract.")
            return False

        rd_idx = self.find_index_by_class(RemovableDrive)  # checks for a RemovableDrive in inventory
        if rd_idx is None:
            print(f"{self._name}: No RemovableDrive available to extract.")
            return False

        # consume the RemovableDrive
        self._inventory.pop(rd_idx)

        # extract all unencrypted assets from target rig
        extracted = target.release_all_unencrypted()

        # add extracted assets into own inventory
        for a in extracted:
            self._inventory.append(a)

        self.increase_trace(3)  # increase trace level due to extraction
        print(f"{self._name}: Extracted {len(extracted)} assets.")
        return True

    # ---------------------- Encrypt/ Decrypt Section----------------------
    def has_security_chip(self, include_rig):
        """
        Return True if SecurityChip is in inventory or in rig storage.
        """
        if self.find_index_by_class(SecurityChip) is not None:
            return True
        if include_rig and self._rig is not None:
            return self._rig.has_asset("SecurityChip")
        return False

    def encrypt_asset(self, name, location):
        """
        Encrypt an asset in either inventory or rig storage.
        """
        if location == "inventory":  # checks inventory for SecurityChip
            if not self.has_security_chip(False):  # checks inventory for SecurityChip and checks encryption
                print(f"{self._name}: No SecurityChip available to encrypt.")
                return False
            idx = self.find_index_by_name(name)
            if idx is None:
                print(f"{self._name}: Asset {name} not found in inventory.")
                return False
            self._inventory[idx].encrypt()
            print(f"{self._name}: Encrypted {name} in inventory.")
            return True

        elif location == "rig":  # checks rig for SecurityChip and checks encryption
            if self._rig is None:
                print(f"{self._name}: No rig to encrypt assets in.")
                return False
            if not self.has_security_chip(True):
                print(f"{self._name}: No SecurityChip available to encrypt in rig.")
                return False
            success = self._rig.encrypt_asset_in_storage(name)
            if not success:
                print(f"{self._name}: Asset {name} not found in rig storage.")
                return False
            print(f"{self._name}: Encrypted {name} in rig storage.")
            return True

        else:
            print("Invalid location; use 'inventory' or 'rig'.")
            return False

    def decrypt_asset(self, name, location):
        """
        Decrypt an asset in either inventory or rig storage.
        """
        if location == "inventory":  # checks inventory for SecurityChip and checks decryption
            if not self.has_security_chip(False):
                print(f"{self._name}: No SecurityChip available to decrypt.")
                return False
            idx = self.find_index_by_name(name)
            if idx is None:
                print(f"{self._name}: Asset {name} not found in inventory.")
                return False
            self._inventory[idx].decrypt()
            print(f"{self._name}: Decrypted {name} in inventory.")
            return True

        elif location == "rig":  # checks rig for SecurityChip and checks decryption
            if self._rig is None:
                print(f"{self._name}: No rig to decrypt assets in.")
                return False
            if not self.has_security_chip(True):
                print(f"{self._name}: No SecurityChip available to decrypt in rig.")
                return False
            success = self._rig.decrypt_asset_in_storage(name)
            if not success:
                print(f"{self._name}: Asset {name} not found in rig storage.")
                return False
            print(f"{self._name}: Decrypted {name} in rig storage.")
            return True

        else:
            print("Invalid location; use 'inventory' or 'rig'.")
            return False

    # ---------------------- Transfers of Asset Section----------------------
    def store_to_rig(self, names):
        """
        Store assets from inventory to rig storage, if names is None, move all assets.
        Returns list of moved asset names.
        """
        if self._rig is None:
            print(f"{self._name}: No rig to store assets in.")
            return []
        moved = []

        if not names:
            to_move = list(self._inventory)  # move all assets
            self._inventory.clear()
            for a in to_move:
                self._rig.store_asset(a)
                moved.append(a.getName())
        else:
            for n in list(names):  # Move specified assets
                idx = self.find_index_by_name(n)
                if idx is None:
                    continue
                a = self._inventory.pop(idx)
                self._rig.store_asset(a)
                moved.append(a.getName())

        print(f"{self._name}: Stored {len(moved)} assets to rig.")
        return moved

    def retrieve_from_rig(self, names):
        """
        Retrieve assets from rig storage into inventory
        If names is None, retrieve all unencrypted assets.
        Returns list of retrieved asset names.
        """
        if self._rig is None:
            print(f"{self._name}: No rig to retrieve assets from.")
            return []
        moved = []

        if not names:
            assets = self._rig.release_all_unencrypted()  # Retrieve all unencrypted assets
            for a in assets:
                self._inventory.append(a)
                moved.append(a.getName())
        else:
            for n in list(names):  # Retrieve specified assets
                a = self._rig.release_asset_by_name(n)
                if a:
                    self._inventory.append(a)
                    moved.append(a.getName())

        print(f"{self._name}: Retrieved {len(moved)} assets from rig.")
        return moved

    # ---------------------- Explicit Getters Section----------------------
    def get_name(self):
        return self._name

    def get_rig(self):
        return self._rig

    def get_trace_level(self):
        return self._trace_level

    def __str__(self):
        rig_name = self._rig.get_name() if self._rig else "None"
        trace_info = f"{self._trace_level}/{self._trace_threshold}"
        inventory_info = self.inventory_summary()
        return f"{self._name} - Rig: {rig_name} - Trace: {trace_info} - Inventory: {inventory_info}"
