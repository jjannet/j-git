import subprocess
from jit.master.colors import bcolors
from jit.models.subModule import SubModule
from pathlib import Path
from jit.processes.printData import printSubmoduleData





def getAllSubmodulesName():
    names = []
    pds = subprocess.run(
        ['git', 'submodule', 'foreach', '''git status'''], capture_output=True).stdout.splitlines()

    for p in pds:
        txt = str(p)

        if txt.find('Entering') != -1:
            s = txt.find('\'') + 1
            names.append(txt[s:].replace('\'"', ''))

    return names


def getSubModuleData(name: str):
    subModule = SubModule(name, '', '')

    pds = subprocess.run(
        ['git', '-C', name, 'status'], capture_output=True).stdout.splitlines()

    if len(pds) >= 2:
        r1 = str(pds[0])
        r2 = str(pds[1])

        if r1.find('On branch') != -1:
            s = r1.find('On branch')
            subModule.branch = r1[s:].replace(
                'On branch ', '').replace('\'', '')
        else:
            subModule.branch = '-'

        if r2.find('Your branch is behind') != -1:
            start = r2.find(' by ') + 3
            end = r2.find('commit')
            commit = r2[start:end].strip()
            subModule.pullRequest = commit
        else:
            subModule.pullRequest = '-'

    return subModule


def checkAllSubModuleStatus():

    names = getAllSubmodulesName()
    for n in names:
        sm = getSubModuleData(n)
        printSubmoduleData(sm)
        print()
