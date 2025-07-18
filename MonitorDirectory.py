import os
import time
from FreeCAD import *
from pathlib import Path

class MonitorDirectoryCommand:
    def __init__(self):
        self.script_directory = "/home/tym/ReferenceDesk/freecad/scripts"  # Corrected path, crucial!
        self.monitor_errors_file = os.path.join(self.script_directory, "monitor_errors.txt")

    def execute(self):
        try:
            while True:
                for filename in os.listdir(self.script_directory):
                    if filename.endswith(".py"):
                        filepath = os.path.join(self.script_directory, filename)
                        try:
                            # Execute the script within the FreeCAD interpreter
                            FreeCADGui.runScript(filepath)
                            print(f"Executed {filename} successfully.")  # Add confirmation message

                        except Exception as e:
                            error_message = f"Error executing {filename}:\n{e}\n"
                            with open(self.monitor_errors_file, "a") as f:
                                f.write(error_message)
                            print(f"Error in {filename}. See {self.monitor_errors_file} for details.") # Print to console

                time.sleep(5)  # Check every 5 seconds. Adjust as needed.

        except KeyboardInterrupt:
            print("Monitoring stopped.")


    def isEnabled(self):
       return True
