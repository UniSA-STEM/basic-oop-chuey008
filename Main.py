"""
File: main.py
Description: <This is the main program that allows to test the different classes to simulate what could happen.>
Author: <Emily Chuong>
ID: <110448094>
Username: <Chuey008>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import DataSpike, CryptoToken, RemovableDrive, SecurityChip, HardwarePatch
from Rig import Rig

def main():
    # Create a hacker
    hacker = Hacker("Fidelius")
    print(hacker)

def test_acquire_and_upgrade():
    hacker = Hacker("Fidelius")
    print(hacker)

    hacker.upgrade_rig()

    # Acquire rig
    hacker.add_to_inventory(CryptoToken())
    hacker.acquire_rig()

    # Upgrade rig
    hacker.add_to_inventory(HardwarePatch())
    hacker.upgrade_rig()

    print(hacker.get_rig())

if __name__ == "__main__":
    main()