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
    # create a hacker
    hacker = Hacker("Fidelius")
    print(hacker)

def test_acquire_and_upgrade():
    hacker = Hacker("Fidelius")
    print(hacker)

    hacker.upgrade_rig()

    # acquire rig
    hacker.add_to_inventory(CryptoToken())
    hacker.acquire_rig()

    # upgrade rig
    hacker.add_to_inventory(HardwarePatch())
    hacker.upgrade_rig()

    print(hacker.get_rig())

def test_data_spike_attack():
    attacker = Hacker("Fidelius")
    defender = Hacker("Cypher")

    attacker.add_to_inventory(CryptoToken())
    defender.add_to_inventory(CryptoToken())
    attacker.acquire_rig()
    defender.acquire_rig()

    # load attacker rig with DataSpikes
    attacker.store_to_rig([DataSpike().getName(), DataSpike().getName()])

    # launch attack
    attacker.launch_data_spike(defender.get_rig(), spikes=2)
    print(defender.get_rig())

def test_trace_blocking():
    hacker = Hacker("Fidelius")
    hacker.add_to_inventory(CryptoToken())
    hacker.acquire_rig()

    # artificially raise trace and exceed threshold
    hacker.increase_trace(10)
    hacker.store_to_rig([DataSpike().getName()])
    hacker.launch_data_spike(Rig("DummyRig"), spikes=1)

def test_encryption_flow():
    hacker = Hacker("Fidelius")
    hacker.add_to_inventory(CryptoToken())
    hacker.acquire_rig()

    hacker.add_to_inventory(SecurityChip())
    hacker.add_to_inventory(DataSpike())

    # encrypt asset in inventory
    hacker.encrypt_asset("DataSpike", "inventory")

    # decrypt asset in inventory
    hacker.decrypt_asset("DataSpike", "inventory")

def test_extraction_edge_case():
    hacker = Hacker("Fidelius")
    target_rig = Rig("BrokenRig")

    # simulate broken rig with unencrypted assets
    target_rig.take_hit()
    target_rig.take_hit()
    target_rig.store_asset(DataSpike())
    target_rig.store_asset(RemovableDrive())

    hacker.add_to_inventory(RemovableDrive())
    hacker.extract_from_rig(target_rig)

def run_all_tests():
    print("\n--- Test: Acquire and Upgrade ---")
    test_acquire_and_upgrade()

    print("\n--- Test: Data Spike ---")
    test_data_spike_attack()

    print("\n--- Test: Trace Blocking ---")
    test_trace_blocking()

    print("\n--- Test: Encryption Flow ---")
    test_encryption_flow()

    print("\n--- Test: Extraction Edge Case ---")
    test_extraction_edge_case()

if __name__ == "__main__":
    run_all_tests()