from FreeCAD import *
from pathlib import Path
import time

class ScriptWorkbench (Workbench):
    MenuText = "Scripts"
    def Initialize(self):
        import MyScriptWorkbench.commands.MonitorDirectoryCommand  # Import the monitor command
        Gui.addWorkbench(MyScriptWorkbench.commands.MonitorDirectoryCommand()) # Add the monitor workbench to FreeCAD
