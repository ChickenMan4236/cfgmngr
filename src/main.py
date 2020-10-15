import os
import sys
import commands
import env
import files

def show_help():
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

files.generate_structure()

if len(sys.argv) == 3:
    if sys.argv[1] == "set-repo":
        commands.set_repo(sys.argv[2])
    elif sys.argv[1] == "add-file":
        commands.add_file(sys.argv[2], None)
    elif sys.argv[1] == "rm-file":
        commands.rm_file(sys.argv[2])
    else: show_help()
elif len(sys.argv) == 2:
    if sys.argv[1] == "repo":
        commands.get_repo()
    elif sys.argv[1] == "push":
        commands.push()
    elif sys.argv[1] == "pull":
        commands.pull()
    elif sys.argv[1] == "files":
        commands.show_files()
    else: show_help()
elif len(sys.argv) == 4:
    if sys.argv[1] == "add-file":
        commands.add_file(sys.argv[3], sys.argv[2])
    else: show_help()
else: show_help()
