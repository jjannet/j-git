from jit.models.commandHelper import CommandHelper
from jit.master.config import Config;
from tabulate import tabulate

def getCommands():
    commands: list[CommandHelper] = []

    commands.append(CommandHelper(
        Config.appName + " status", "view main and all submodule status"))
    
    commands.append(CommandHelper(
        Config.appName + " switch [branch]", "switch only all submodule branch"))
    
    commands.append(CommandHelper(
        Config.appName + " pull", "pull main and all submodule status"))
    

    return commands


def printHelp():
    commands = getCommands()
    datas = []

    for cmd in commands:
        datas.append([cmd.command, cmd.detail])

    print("Command helper")

    print(tabulate(datas,
          headers=['Command', 'Description'], tablefmt='orgtbl'))
