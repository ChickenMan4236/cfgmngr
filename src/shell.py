import subprocess
import os

FNULL = open(os.devnull, "w")

def run_blind(cmd):
    return subprocess.call(cmd, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
def run(cmd):
    subprocess.call(cmd, shell=True)
