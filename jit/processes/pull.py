import subprocess

from jit.master.colors import bcolors
from jit.processes.utils import getAllSubmodulesName
from jit.processes.utils import getSubModuleData


def pullAllSubmodules():
    submodules = getAllSubmodulesName()

    for n in submodules:
        pullSubmodule(n)


def pullSubmodule(submoduleName: str):
    print('Pulling: ' + bcolors.OKCYAN + submoduleName + bcolors.ENDC)

    pds = subprocess.run(
        ['git', '-C', submoduleName, 'pull'], capture_output=True).stdout.splitlines()

    if len(pds) > 0:
        txt = str(pds[0])

        if txt.find('You are not currently') != -1:
            print(bcolors.FAIL + 'You are not currently on a branch.' + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + 'Already up to date.' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + 'You are not currently on a branch.' + bcolors.ENDC)


def pullMain():
    print('Pulling main')
    pds = subprocess.run(
        ['git', 'pull'], capture_output=True).stdout.splitlines()

    if len(pds) > 0:
        txt = str(pds[0])

        if txt.find('You are not currently') != -1:
            print(bcolors.FAIL + 'You are not currently on a branch.' + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + 'Already up to date.' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + 'You are not currently on a branch.' + bcolors.ENDC)


def pull():
    pullMain()
    print()
    pullAllSubmodules()
