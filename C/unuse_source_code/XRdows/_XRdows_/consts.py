import pathlib
import os
import yaml

folder = pathlib.Path(__file__).parent.resolve()

with open(os.path.join(folder, './config/config.yaml'), 'r') as f:
    configs = yaml.safe_load(f)

_1_E = ' > Please enter the command (_EXIT = exit , C_T = Command table , _I_H_ = introduce html) >>>'

_2_E = ' > The plane war game is game is launching'

_3_E = ' > The plane war game is closing'

_4_E = ' > Effective after restarting the program'

_5_E = ' > Enter File Path >>>'

_6_E = ' > Enter File Content >>>'

_7_E = ' > Error occurred'

_8_E = ' > Please enter the developer password >>>'

_9_E = ' > Open Developer Mode'

_10_E = ' > Password is wrong, please re-enter the password'

_11_E = ' > Please enter the path where the code is stored >>>'

_12_E = ' > Please back up first'

_13_E = ' > Please enter the text to print >>>'

_14_E = ' > Please enter the music file path >>>'

_15_E = ' > Please try again'

_16_E = ' > Please enter the python file path >>>'

_17_E = ' > Please enter the executable file path >>>'

_18_E = ' > Please enter the image file path >>>'
