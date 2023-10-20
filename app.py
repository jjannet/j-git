import sys
from jit.master.colors import bcolors
from jit.processes.printData import printMainStatus
from jit.processes.utils import checkAllSubModuleStatus
from jit.processes.help import printHelp
from jit.processes.switch import switchBranch
from jit.processes.switch import switchMain
from jit.processes.pull import pull

dir = "P:\ptt\digital\d-framework\\backends\dfw-be-config"


if len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "status":
        printMainStatus()
        print()
        print('submodules -------------------------------------')
        print()
        checkAllSubModuleStatus()

    elif command == "switch":
        if len(sys.argv) > 2:
            branchName = sys.argv[2]
            switchBranch(branchName)
        else:
            print(bcolors.WARNING + 'Please select branch name.' + bcolors.ENDC)

    elif command == "pull":
        pull()

else:
    printHelp()
