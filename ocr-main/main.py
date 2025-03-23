import subprocess
import os

# Get the absolute path of the current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to detect.py and extract_number.py
detect_script = os.path.join(script_dir, "detect.py")
extract_script = os.path.join(script_dir, "extract_number.py")

# Run detect.py
print("Running detect.py...")
subprocess.run(["python", detect_script])

# Run extract_number.py
print("Running extract_number.py...")
subprocess.run(["python", extract_script])

print("Processing completed!")
