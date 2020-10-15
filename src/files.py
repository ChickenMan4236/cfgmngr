import os
import env

def generate_structure():
    if not os.path.exists(env.configDir):
        os.makedirs(env.configDir)

    if not os.path.exists(env.configDir + "files/"):
        os.makedirs(env.configDir + "files/")

    if not os.path.exists(env.configDir + "backup/"):
        os.makedirs(env.configDir + "backup/")

    if not os.path.exists(env.configDir + "files/locations"):
        open(env.configDir + "files/locations", "w").close()


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

def check_tracked(customName):
    locations = open(env.configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
        if lines[i-1] == customName:
            return True
    return False

def track(fileName, customName):
    locations = open(env.configDir + "files/locations", "a")
    locations.write(os.path.basename(customName)+"\n")
    if(fileName.startswith('/')):
        path = fileName
    else:
        path = os.getcwd()+"/"+fileName
    locations.write(files.remove_username(path)+"\n")
    locations.close()
    print("File saved")

def untrack(fileName):
    locations = open(env.configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()
    newLines = ""

    for i in range(1, len(lines), 2):
        if lines[i-1] != fileName:
            newLines += lines[i-1] + '\n' + lines[i] + '\n'

    locations = open(env.configDir + "files/locations", "w");
    locations.write(newLines)
    locations.close()

def copy(path, name, toConfig):
    if toConfig:
        shutil.copy(path, env.configDir+"files/"+name)
    else:
        shutil.copy(env.configDir+"files/"+name, path)
def backup(path, name):
    if os.path.exists(path):
        shutil.copy(path, env.configDir+"backup/"+name)


