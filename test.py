import os, subprocess

# Settings
TEST_DIR = "."     # Directory with the program
CODE_FILE = "main.c"    # C code
COMPILER_TIMEOUT = 10.0 # Compiler timeout (seconds)
RUN_TIMEOUT = 10.0      # Tun timeout (seconds)

# Create absolute path
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Compile program
print("Building...")

try:
        ret= subprocess.run(["gcc", code_path, "-o", app_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            timeout=COMPILER_TIMEOUT)
except Exception as e:
        print("ERROR: Compilation failed.", str(e))
        exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print(output)
output = ret.stderr.decode("utf-8")
print(output)

# Check to see if the program compiled successfully
if ret.returncode != 0:
        print("Compilation failed.")
        exit(1)

# Run the compiled program
print("Running...")
try:
        ret = subprocess.run([app_path],
                             stdout=subprocess.PIPE,
                             timeout=RUN_TIMEOUT)
except Exception as e:
        print("ERROR: Runtime failed.", str(e))
        exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print("Outout: ", output)

# All tests passed! Exit gracefullly
print("All tests passed!")
exit(0)
