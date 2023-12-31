import subprocess
from sys import platform

# Execute build_luamake.py
subprocess.run(["python", "build_luamake.py"])

# Execute build_luadebug.py

if platform == "win32":
    scriptPath = os.path.join(os.getcwd(), "build_luadebug.py")
    command = ["powershell.exe", "-File", scriptPath]
else:
    subprocess.run(["python", "build_luadebug.py"])