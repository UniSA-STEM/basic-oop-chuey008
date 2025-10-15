"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

"""
File: Rig.py
Description: The class represents a computer, that has a name, damage counter (starting at 0), broken state (False) and storage for assets.
Author: Emily Chuong
ID: 110448094
Username: Chuey008
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# from asset import Assets, DataSpike, RemovableDrive, CryptoToken, HardwarePatch, SecurityChip

class Rig:
    def __init__(self, name: str):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        self.storage = [DataSpike(), DataSpike(), RemovableDrive()]

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

