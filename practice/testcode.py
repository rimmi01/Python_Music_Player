import os

class DesktopImport:
    def __init__(self):
        desktop_directory = '/home/rimmi/Desktop'
        vscode_desktop_directory = 'practice/desktop_import'
        for desktop_import in os.listdir(desktop_directory):
            src = os.path.join(desktop_directory, desktop_import)
            dest = os.path.join(vscode_desktop_directory, desktop_import)
            if os.path.isfile(src):
                with open(src, 'r') as source_file, open(dest, 'w') as destination_file:
                    destination_file.write(source_file.read())

DesktopImport()
