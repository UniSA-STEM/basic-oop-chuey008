"""
File: main.py
Description: <This is the main program that allows to test the different classes to simulate what could happen.>
Author: <Emily Chuong>
ID: <110448094>
Username: <Chuey008>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset, CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
from Rig import Rig
from Hacker import Hacker

def main():
    # Create a hacker
    hacker = Hacker("Fidelius")
    print(hacker)

    # Acquire a rig
    print("\n-- Acquiring Rig --")
    hacker.acquire_rig()
    print(hacker)

if __name__ == "__main__":
    main()