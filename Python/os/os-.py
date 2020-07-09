import os

def basics():
    # returns the current working directory
    print(os.getcwd())

    # changes the working directory
    os.chdir('C:/Users/Max Mustermann/Desktop')
    print(os.getcwd())

    # lists all files and directories in the current working directory
    print(os.listdir())

    # creates a new directory
    os.makedirs('os-test/sub-dir')
    os.makedirs('test')

    # deletes a directory
    os.removedirs('os-test/sub-dir')

    # changes the name of a file or directory
    os.rename('test', 'new name')

    #returns a tuple of the splited path
    print(os.path.split('Desktop/test.txt'))

    #returns the connected path of the two pieces
    print(os.path.join('Desktop', 'test.txt'))

    # executes a command on the console
    os.system('shutdown -s -t 3600')

def os_Walk():
    # goes trough all directories in the path and lists the files and directories within the directory
    for dirpath, dirnames, filenames in os.walk('C:/Users/Max Mustermann/Desktop'):
        print('Current Path: ' + str(dirpath))
        print('Directories: ' + str(dirnames))
        print('Files: '+ str(filenames) + '\n')