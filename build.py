import subprocess

# Execute build_luamake.py
subprocess.run(["python", "build_luamake.py"])

# Execute build_luadebug.py
subprocess.run(["python", "build_luadebug.py"])