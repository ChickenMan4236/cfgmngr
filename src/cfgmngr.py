#!/usr/bin/env python

import sys
import subprocess
import os
import shutil

FNULL = open(os.devnull, "w")
configDir = "/home/"+os.getlogin()+"/.config/cfgmngr/"

#Path actions

def add_username(path):
    return path.replace("$USER$", os.getlogin())

def remove_username(path):
    if(not path.startswith("/home/")):
        return path
    return "/home/$USER$/"+path[len(os.getlogin())+7:]

def remove_tilde(path):
    if(path.startswith("~")):
        return "/home/"+os.getlogin()+"/"+path[1:]
    return path

#Repo actions

def test_repo():
    print("Testing repository")
    cmd = "cd ~/.config/cfgmngr/files && git ls-remote"
    res = subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    if res == 0: print("Fine")
    return res == 0

def repo_err():
    print("Cant connect to repository")

def get_repo():
    cmd = "cd "+configDir+"files/ && git remote -v"
    subprocess.call(cmd, shell=True)

#File actions

def check_exists(fileName):
    try:
        if fileName.startswith('/'):
            file = open(fileName)
        else:
            file = open(os.getcwd() +"/"+ fileName)
    except IOError:
       return False
    else:
        file.close()
    return True

def check_already_saved(customName):
    locations = open(configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
        if lines[i-1] == customName:
            return True
    return False

def save_file(fileName, customName):
    locations = open(configDir + "files/locations", "a")
    locations.write(os.path.basename(customName)+"\n")
    if(fileName.startswith('/')):
        path = fileName
    else:
        path = os.getcwd()+"/"+fileName
    locations.write(remove_username(path)+"\n")
    locations.close()
    print("File saved")

def unsave_file(fileName):
    locations = open(configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()
    newLines = ""

    for i in range(1, len(lines), 2):
        if lines[i-1] != fileName:
            newLines += lines[i-1] + '\n' + lines[i] + '\n'

    locations = open(configDir + "files/locations", "w");
    locations.write(newLines)
    locations.close()

def copy_file(path, name, toConfig):
    if toConfig:
        shutil.copy(path, configDir+"files/"+name)
    else:
        shutil.copy(configDir+"files/"+name, path)
def backup_file(path, name):
    if os.path.exists(path):
        shutil.copy(path, configDir+"backup/"+name) 

#Command actions

def show_files():
    locations = open(configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
        print(lines[i-1] + ": "+lines[i])

    if len(lines) == 1 or len(lines) == 0:
        print("You have no saved files")

def pull():
    print("Downloading files")

    cmd = "cd "+configDir+"files/ && git fetch --all; git reset --hard origin/master"
    res = subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    if res != 0:
        repo_err()
        return

    print("Moving files")
    locations = open(configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
        backup_file(add_username(lines[i]), lines[i-1])
        copy_file(add_username(lines[i]), lines[i-1], False)

    print("Done")

def push():
    print("Packing files")
    locations = open(configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
       copy_file(add_username(lines[i]), lines[i-1], True)

    print("Uploading files")

    cmd = "cd "+configDir+"files/"+" && git add . && git commit -m \"test\"; git push -u origin master"

    res = subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    if res != 0:
        repo_err()

    print("Done")

def rm_file(fileName):
    unsave_file(fileName)
    cmd = "cd "+configDir+"files/ && rm -f "+fileName
    subprocess.call(cmd, shell=True)

def add_file(fileName, customName):
    fileName = remove_tilde(fileName)

    if(customName == None):
        customName = fileName

    if check_already_saved(customName):
        print("This filename is alredy taken. Try using custom name for this file.")
        return

    if check_exists(fileName):
        save_file(fileName, customName)
    else:
       print("There is no file like this")

def set_repo(repo):
    cmd = "cd ~/.config/cfgmngr/files && git remote rm origin; git init; git remote add origin "+repo
    res = subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    if res != 0:
       repo_err()
       return

def help():
    print("Usage: cfgmngr [ACTION] [OPTION]")
    print("Actions:")
    print(" set-repo [URL] - add remote git repository to store your configs")
    print(" repo - show current git repository")
    print(" add-file [FILE PATH] - add file to storage")
    print(" add-file [CUSTOM NAME] [FILE PATH] - add file to storage with custom name")
    print(" rm-file [FILE NAME] - remove file from storage")
    print(" files - show your stored files")
    print(" pull - pull your config files from remote repository and replace your current files with downloaded")
    print(" push - push your saved config files to remote repository")

#Readme
def generate_readme():
    readme = open(configDir + "files/README.MD", "w");
    readme.write("# ![](https://github.com/ChickenMan4236/cfgmngr/blob/master/logoFull.png)\n")
    readme.write("## Theese dotfiles have been uploaded with [cfgmngr](https://github.com/ChickenMan4236/cfgmngr)\n")
    readme.write("### [cfgmngr](https://github.com/ChickenMan4236/cfgmngr) is a simple tool, that makes storing your dotfiles on github easier\n")
    readme.close()

#Main

def main():
    if not os.path.exists(configDir):
        os.makedirs(configDir)

    if not os.path.exists(configDir + "files/"):
        os.makedirs(configDir + "files/")

    if not os.path.exists(configDir + "backup/"):
        os.makedirs(configDir + "backup/")

    if not os.path.exists(configDir + "files/locations"):
        open(configDir + "files/locations", "w").close()

    if len(sys.argv) == 3:
        if sys.argv[1] == "set-repo":
            set_repo(sys.argv[2])
        elif sys.argv[1] == "add-file":
            add_file(sys.argv[2], None)
        elif sys.argv[1] == "rm-file":
            rm_file(sys.argv[2])
        else: help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "repo":
            get_repo()
        elif sys.argv[1] == "push":
            if not test_repo():
                repo_err()
                exit()
            generate_readme()
            push()
        elif sys.argv[1] == "pull":
            if not test_repo():
                repo_err()
                exit()
            pull()
        elif sys.argv[1] == "files":
            show_files()
        else: help()
    elif len(sys.argv) == 4:
        if sys.argv[1] == "add-file":
            add_file(sys.argv[3], sys.argv[2])
        else: help()
    else: help()

main()
