import repo
import shell
import files
import paths
import env

def show_files():
    locations = open(env.configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
        print(lines[i-1] + ": "+lines[i])

    if len(lines) == 1 or len(lines) == 0:
        print("You have no saved files")

def pull():
    if not repo_test():
        repo_err()
        exit()

    print("Downloading files")

    cmd = "cd "+env.configDir+"files/ && git fetch --all; git reset --hard origin/master"
    res = shell.run_blind(cmd)
    if res != 0:
        repo.err()
        return

    print("Moving files")
    locations = open(env.configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
        files.backup(paths.add_username(lines[i]), lines[i-1])
        files.copy(paths.add_username(lines[i]), lines[i-1], False)

    print("Done")

def push():
    if not repo.test():
        repo.err()
        exit()
    files.generate_readme()
    print("Packing files")
    locations = open(env.configDir + "files/locations");
    lines = locations.read().split('\n')
    locations.close()

    for i in range(1, len(lines), 2):
       files.copy(add_username(lines[i]), lines[i-1], True)

    print("Uploading files")

    cmd = "cd "+env.configDir+"files/"+" && git add . && git commit -m \"test\"; git push -u origin master"

    res = shell.run_blind(cmd)
    if res != 0:
        repo.err()

    print("Done")

def get_repo():
    repo.show()

def rm_file(fileName):
    files.untrack(fileName)
    cmd = "cd "+env.configDir+"files/ && rm -f "+fileName
    shell.run(cmd)

def add_file(fileName, customName):
    fileName = paths.remove_tilde(fileName)

    if(customName == None):
        customName = fileName

    if files.check_tracked(customName):
        print("This filename is alredy taken. Try using custom name for this file.")
        return

    if files.check_exists(fileName):
        files.track(fileName, customName)
    else:
       print("There is no file like this")

def set(r):
    cmd = "cd ~/.config/cfgmngr/files && git remote rm origin; git init; git remote add origin "+r
    res = shell.run_blind(cmd)
    if res != 0:
       repo.err()
       return


