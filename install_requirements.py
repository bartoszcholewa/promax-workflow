# Installing required packages for running this project

import datetime
import os
import pip
from subprocess import call
import time


def set_snapshot_filepath(snapshot_path, filepath=None, item=0):
    if filepath is None:
        today = str(datetime.date.today())
        if item >= 0:
            item += 1
        base_filepath = os.path.join(
            snapshot_path, "snapshot_%s_%i.txt" % (today, item))
    else:
        if item >= 0:
            item += 1
        today = str(datetime.date.today())
        base_filepath = os.path.join(
            snapshot_path, "snapshot_%s_%i.txt" % (today, item))
    if os.path.exists(base_filepath):
        return set_snapshot_filepath(snapshot_path, filepath=base_filepath, item=item)
    return base_filepath


def save_snapshot(snapshot_list):
    snapshot_path = os.path.join(os.getcwd(), "snapshots")
    print("Checking for already existing snapshots...")
    if not os.path.exists(snapshot_path):
        print("Snapshots not detected. Creating folder... ")
        os.mkdir(snapshot_path)
        print("'snapshots' folder created.")
    filepath = set_snapshot_filepath(snapshot_path)
    with open(filepath, "w+") as snapshot:
        for rq in sorted(snapshot_list, key=str.lower):
            snapshot.write(str(rq) + "\n")
    print("Snapshot saved.")


def make_snapshot():
    current = get_packages()
    save_snapshot(current)


def get_packages(upgrade=False):
    print("Snapshotting  current packages versions...")
    current = []
    for dist in pip.get_installed_distributions():
        if upgrade:
            current.append(dist)
        else:
            current.append(str(dist.as_requirement()))
    return current


def install_requirements():
    call("pip install -r requirements.txt")
    print("Requirements installed.")
    print("Check 'snapshot' folder to return to previous packages version.")


make_snapshot()
install_requirements()
