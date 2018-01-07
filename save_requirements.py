# Generating file with required packages for this project

import os
import pip


def get_packages(upgrade=False):
    print("Getting packages...")
    current = []
    for dist in pip.get_installed_distributions():
        if upgrade:
            current.append(dist)
        else:
            current.append(str(dist.as_requirement()))
    return current


def get_requirements_location(next_to=None):
    if next_to is not None:
        location = None
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if str(file) == str(next_to):
                    location = os.path.join(root, "requirements.txt")
                    return location
    return None


def save_requirements(next_to='save_requirements.py'):
    packages = get_packages()
    print("Saving requirements.txt")
    location = get_requirements_location(next_to=next_to)
    if location is None:
        location = os.path.join(os.getcwd(), "requirements.txt")
    with open(location, "w") as f:
        for pkg in sorted(packages, key=str.lower):
            f.write(str(pkg) + "\n")


save_requirements()
