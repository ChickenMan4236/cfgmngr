import os

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


