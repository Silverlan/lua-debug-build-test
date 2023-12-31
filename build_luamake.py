import subprocess
import os
from sys import platform

# Git clone
subprocess.run(["git", "clone", "https://github.com/actboy168/luamake"])

# Change directory to luamake
os.chdir("luamake")

# Git submodule init
subprocess.run(["git", "submodule", "init"])

# Git submodule update
subprocess.run(["git", "submodule", "update"])

def reset_to_commit(sha):
	subprocess.run(["git","fetch"],check=True)
	subprocess.run(["git","checkout",sha,"--recurse-submodules"],check=True)

reset_to_commit("0bf6041")

# Check OS and execute the appropriate installation script
if platform == "win32":  # Windows
    subprocess.run([".\compile\install.bat", "msvc"])
else:  # Other OS (assuming Unix-like)
    subprocess.run(["./compile/install.sh", "other"])

# Move back to the previous directory
os.chdir("..")
