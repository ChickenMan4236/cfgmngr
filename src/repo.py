import shell
import env

def test():
    print("Testing repository")
    cmd = "cd ~/.config/cfgmngr/files && git ls-remote"
    res = shell.run(cmd)
    if res == 0: print("Fine")
    return res == 0

def err():
    print("Cant connect to repository")

def show():
    cmd = "cd "+env.configDir+"files/ && git remote -v"
    shell.run(cmd)


