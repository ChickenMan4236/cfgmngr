import os
import sys
import commands
import env
import files

def show_help():
    print("Usage: cfgmngr [ACTION] [OPTION]")
    print("Actions:")
    print(" repo [URL] - add remote git repository to store your configs")
    print(" repo - show current git repository")
    print(" track [FILE PATH] - track file storage")
    print(" track [CUSTOM NAME] [FILE PATH] - track file with custom name")
    print(" untrack [FILE NAME] - end file tracking")
    print(" files - show tracked files")
    print(" pull - pull your files from remote repository and replace your current files with downloaded")
    print(" push - push your tracked files to remote repository")

files.generate_structure()

if len(sys.argv) == 3:
    if sys.argv[1] == "repo":
        commands.set_repo(sys.argv[2])
    elif sys.argv[1] == "track":
        commands.add_file(sys.argv[2], None)
    elif sys.argv[1] == "untrack":
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
    if sys.argv[1] == "track":
        commands.add_file(sys.argv[3], sys.argv[2])
    else: show_help()
else: show_help()
