import subprocess
from jit.master.colors import bcolors
from jit.models.subModule import SubModule
from pathlib import Path


def printMainStatus():

    pds = subprocess.run(
        ['git', 'status'], capture_output=True).stdout.splitlines()

    if len(pds) >= 2:
        r1 = str(pds[0])
        r2 = str(pds[1])

        if r1.find('On branch') != -1:
            s = r1.find('On branch')
            print('Current branch: ' + bcolors.OKCYAN + r1[s:].replace(
                'On branch ', '').replace('\'', '') + bcolors.ENDC)
        else:
            print(bcolors.FAIL + 'Not select branch' + bcolors.ENDC)

        if r2.find('Your branch is up to date') != -1:
            print(bcolors.OKGREEN + 'Your branch is up to date' + bcolors.ENDC)
        else:
            start = r2.find(' by ') + 3
            end = r2.find('commit')
            commit = r2[start:end].strip()
            print('Have ' + commit + ' pull requests')


def printSubmoduleData(subModule: SubModule):
    print('Name: ' + bcolors.OKCYAN + subModule.name + bcolors.ENDC)
    print('Branch: ' + bcolors.OKCYAN + subModule.branch + bcolors.ENDC)
    print('Pull request: ' + bcolors.OKCYAN +
          subModule.pullRequest + bcolors.ENDC)
