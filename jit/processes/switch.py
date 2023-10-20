import subprocess
from jit.master.colors import bcolors
from jit.processes.utils import getAllSubmodulesName


def switchMain(branchName: str):
    print('Switching main')
    pds = subprocess.run(
        ['git', 'switch', branchName], capture_output=True).stdout.splitlines()

    if len(pds) > 0:
        txt = str(pds[0])

        if txt.find('invalid reference') != -1:
            print(bcolors.FAIL +
                  'Not found branch ' + branchName + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN +
                  'Current in branch ' + branchName + bcolors.ENDC)
    else:
        print(bcolors.FAIL +
              'Not found branch ' + branchName + bcolors.ENDC)


def switchSubmodule(submoduleName: str, branchName: str):
    print('switching: ' + bcolors.OKCYAN + submoduleName + bcolors.ENDC)
    pds = subprocess.run(
        ['git', '-C', submoduleName, 'switch', branchName], capture_output=True).stdout.splitlines()

    if len(pds) > 0:
        txt = str(pds[0])

        if txt.find('invalid reference') != -1:
            print(bcolors.FAIL +
                  'Not found branch ' + branchName + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN +
                  'Current in branch ' + branchName + bcolors.ENDC)
    else:
        print(bcolors.FAIL +
              'Not found branch ' + branchName + bcolors.ENDC)


def switchAllSubmodules(branchName: str):
    submodules = getAllSubmodulesName()

    for name in submodules:
        switchSubmodule(name, branchName)


def switchBranch(branchName: str):
    switchAllSubmodules(branchName)
