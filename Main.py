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

def test_data_spike_attack():
    attacker = Hacker("Trinity")
    defender = Hacker("Cypher")

    attacker.add_to_inventory(CryptoToken())
    defender.add_to_inventory(CryptoToken())
    attacker.acquire_rig()
    defender.acquire_rig()

    # Load attacker rig with DataSpikes
    attacker.store_to_rig([DataSpike().getName(), DataSpike().getName()])

    # Launch attack
    attacker.launch_data_spike(defender.get_rig(), spikes=2)
    print(defender.get_rig())

def run_all_tests():
    print("\n--- Test: Acquire and Upgrade ---")
    test_acquire_and_upgrade()

    print("\n--- Test: Data Spike ---")
    test_data_spike_attack()

if __name__ == "__main__":
    run_all_tests()