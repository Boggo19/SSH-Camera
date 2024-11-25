import subprocess

ui_file = "SSHmealDesigner.ui"  
output_file = "SSHmealDesignerPython.py"  

try:
    print(f"Converting {ui_file} to {output_file}...")
    subprocess.run(["pyuic5", "-x", ui_file, "-o", output_file], check=True)
    print(f"Successfully updated {output_file}!")
except subprocess.CalledProcessError as e:
    print(f"Error: Failed to update {output_file}.")
    print(e)
