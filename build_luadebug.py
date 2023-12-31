import subprocess
import os

# Git clone
subprocess.run(["git", "clone", "https://github.com/actboy168/lua-debug"])

# Change directory to lua-debug
os.chdir("lua-debug")

# Git submodule init
subprocess.run(["git", "submodule", "init"])

# Git submodule update
subprocess.run(["git", "submodule", "update"])

def reset_to_commit(sha):
	subprocess.run(["git","fetch"],check=True)
	subprocess.run(["git","checkout",sha,"--recurse-submodules"],check=True)

reset_to_commit("693549d")

# Run download_deps.lua using luamake
subprocess.run(["../luamake/luamake", "lua", "compile/download_deps.lua"])

# Build in release mode using luamake
subprocess.run(["../luamake/luamake", "-mode", "release"])
