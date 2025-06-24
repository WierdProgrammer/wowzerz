#Welcome to the source code, here at the top is where the ascii art is set in a variable.
banner = r"""
 _    _  _____  _    _  ______ ___________ ______
| |  | ||  _  || |  | ||___  /|  ___| ___ \___  /
| |  | || | | || |  | |   / / | |__ | |_/ /  / / 
| |/\| || | | || |/\| |  / /  |  __||    /  / /  
\  /\  /\ \_/ /\  /\  /./ /___| |___| |\ \./ /___
 \/  \/  \___/  \/  \/ \_____/\____/\_| \_\_____/
"""
#This code over here prints out the banner and the little message.
print(banner)
print('Powered by RAM')
#These are the lists that hold information about what the user saves.
fileNames=[]
fileCommands=[]
user_scripts=[]
user_modules=[]
user_commandNames=[]
user_commandFunctions=[]
#This divider function prints out a 50 character long line.
def divider():
    print('='*50)
divider()
#WowzerzExec is just a function that runs python code but includes error handeling, so the whole terminal doesn't crash.
def WowzerzExec(code):
    try:
        exec(code)
    except Exception as e:
        print(f'[Error] {e}')
#MultiLine just allows the user to write code in multiple lines instead of in one.
def multiLine(prompt='>'):
    print(f"{prompt} (Enter an empty line to run the code)")
    lines = []
    while True:
        line = input()
        if line.strip() == '':
            break
        lines.append(line)
    return '\n'.join(lines)
print('[RECOMMENDED] Tip: Type "help" for a list of commands.')
#This main() function is extremely important, its a loop that holds the command input stuff.
def main():
    while True:
        if user_scripts:
            for script in user_scripts:
                WowzerzExec(script)
        iQ=input('>')
        if iQ.lower() == 'help':
            print("┌─[HELP]")
            print(" (COMMAND LIST):")
            print('exit: Exits the program| run: Runs python| mfile: Makes a python file| rfile: Runs a python file| lfile: Lists your files| dfile: Deletes a file| cfile: Deletes all the files you made| import: Allows you to import modules used in python| userscript: Allows you to write code that runs on a loop| listmodules: Lists the modules you imported via the import command| clearuserscripts: Deletes your user scripts| makecommand: Allows you to make a custom command| deleteusercommand: Lets you delete custom commands| listusercommands: Lists your custom commands| clear: Deletes most of the data you saved on the terminal to free up some memory')
            print("└────────────")
        elif iQ.lower() == 'exit':
            break
        elif iQ.lower() == 'run':
            runCommandInput=multiLine('>run>')
            WowzerzExec(runCommandInput)
        elif iQ.lower() == 'mfile':
            fileNameInput=input('>mfile>File-Name:')
            if fileNameInput not in fileNames:
                fileContentInput=multiLine('>mfile>Python-Code:')
                fileNames.append(fileNameInput)
                fileCommands.append(fileContentInput)
                print('File Saved')
            else:
                print('File Name Already Exists.')
        elif iQ.lower() == 'rfile':
            runfileInput=input('>rfile>File-Name:')
            fileToRunOrder=fileNames.index(runfileInput)
            WowzerzExec(fileCommands[fileToRunOrder])
            print(f'{runfileInput}.py ran successfully')
        elif iQ.lower() == 'lfile':
            print("┌─[YOUR FILES]")
            print(fileNames)
            print("└────────────")
        elif iQ.lower() == 'dfile':
            deleteFileInput=input('>delete-file>File-Name:')
            fileToDeleteOrder=fileNames.index(deleteFileInput)
            del fileCommands[fileToDeleteOrder]
            del fileNames[fileToDeleteOrder]
            print(f'{deleteFileInput} Successfully Deleted')
        elif iQ.lower() == 'cfile':
            fileCommands.clear()
            fileNames.clear()
            print('Files Successfully Deleted')
        elif iQ.lower() == 'import':
            modulesInput=input('>import>module to install:')
            mti=f'import {modulesInput}'
            WowzerzExec(mti)
            user_modules.append(modulesInput)
            print(f'"{modulesInput}" Successfully Imported')
        elif iQ.lower() == 'userscript':
            usInput=multiLine('>userscript>Python Code To Loop:')
            user_scripts.append(usInput)
        elif iQ.lower() == 'listmodules':
            print("┌─[YOUR MODULES]")
            print(user_modules)
            print("└────────────")
        elif iQ.lower() == 'clearuserscripts':
            user_scripts.clear()
            print('User Scripts Deleted')
        elif iQ.lower() == 'makecommand':
            customCommandInputName=input('>make-command>command-name:')
            if customCommandInputName not in user_commandNames:
                customCommandInputCode=multiLine('>make-command>Python-Code:')
                user_commandNames.append(customCommandInputName)
                user_commandFunctions.append(customCommandInputCode)
                print(f'Successfully saved your custom command! Now you can run it by entering {customCommandInputName}')
            else:
                print('Custom Command Name Already Exists')
        elif iQ.lower() == 'deleteusercommand':
            customcommandtodel=input('>deleteUserCommand>custom-command-name:')
            orderOfCustomCommandToDelete=user_commandNames.index(customcommandtodel)
            del user_commandFunctions[orderOfCustomCommandToDelete]
            del user_commandNames[orderOfCustomCommandToDelete]
            print('Custom Command Deleted.')
        elif iQ.lower() == 'listusercommands':
            print("┌─[YOUR COMMANDS]")
            print(user_commandNames)
            print("└────────────────")
        elif iQ.lower() == 'clear':
            divider()
            fileNames.clear()
            fileCommands.clear()
            print('Files Deleted')
            user_scripts.clear()
            print('User Scripts Deleted')
            user_commandNames.clear()
            user_commandFunctions.clear()
            print('Custom Commands Deleted')
            divider()
        elif iQ in user_commandNames:
            orderOfCustomCommand=user_commandNames.index(iQ)
            WowzerzExec(user_commandFunctions[orderOfCustomCommand])
        else:
            print(f"'{iQ}' is not a valid command")
#This starts the main() function, so you can actually use the commands
main()