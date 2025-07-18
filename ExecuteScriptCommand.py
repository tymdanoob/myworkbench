import FreeCAD, FreeCADGui
import subprocess
import os
from pathlib import Path

class ExecuteScriptCommand:
    def Activated(self, signal, value):
        script_path = value  # Get the script path from the workbench's parameter.

        if not os.path.exists(script_path):
            FreeCADGui.ActiveDocument.MessageView.clear()
            FreeCADGui.ActiveDocument.MessageView.addMessage("Error: Script file does not exist.")
            return  # Exit if the script doesn't exist

        try:
            freecadcmd = "/usr/bin/freecadcmd" # Adjust this path to your FreeCAD installation!
            command = [freecadcmd, "-no-gui", "--edit", "PersistentProject.FCStd", script_path]  # Corrected command
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if stderr:
                FreeCADGui.ActiveDocument.MessageView.clear()
                FreeCADGui.ActiveDocument.MessageView.addMessage("Error executing script:\n" + stderr.decode())
            else:
                FreeCADGui.ActiveDocument.MessageView.clear()
                FreeCADGui.ActiveDocument.MessageView.addMessage("Script executed successfully.")

        except Exception as e:
            FreeCADGui.ActiveDocument.MessageView.clear()
            FreeCADGui.ActiveDocument.MessageView.addMessage("An unexpected error occurred:\n" + str(e))
