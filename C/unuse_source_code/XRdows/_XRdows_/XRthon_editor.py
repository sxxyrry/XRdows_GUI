import os
from consts import (
    folder,
    configs
)

def XRthon_editor():
    if 'XRthon_editor' in configs:
        if configs['XRthon_editor'] == True:
            XRthon_F_isexists = os.path.exists(os.path.join(folder, './mods_file/XRthon_editor_mods_file/main.py'))
            if XRthon_F_isexists == True:
                from mods_file.XRthon_editor_mods_file.main import mains
                try:
                    mains()
                except SystemExit:
                    pass
            elif XRthon_F_isexists == False:
                print(' > The mods file (XRthon_editor) file does not exist')
        elif configs['XRthon_editor'] == False:
            print(' > You don\'t have XRthon enabled')
        else:
            print(' > The XRthon_editor value must be True or False')
    else:
        print(' > The XRthon_editor key does not exist')