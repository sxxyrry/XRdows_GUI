import time
import os
import sys
import subprocess
import zipfile
import pygame
from XRdows_text import(
    XRdows,
    Edition_logs,
    command_table
)
from consts import (
    folder,
    _14_E,
    _15_E,
    _16_E,
    _17_E,
    _18_E
)

def V():
    E_L_T = ''.join(Edition_logs)
    E_L_T_L = E_L_T.split('\n')
    L_ = []
    for text in E_L_T_L:
        if 'V' and 'BETA' in text:
            L_.append(text)
    text_1 = L_[len(L_) - 1].split(' > ')
    text_2 = text_1[1].split(' V')
    Version = text_2[0]
    return Version

Version = V()

def XRDOWS():
    time.sleep(0.5)
    print(f'{XRdows}')
    time.sleep(0.5)

def prompt():
    print(' > Processor/running interpreter : python')
    time.sleep(0.5)
    print(f' > python_version : {sys.version}')
    time.sleep(0.5)
    print(' > Program name : XRdows')
    time.sleep(0.5)
    print(' > by : \'是星星与然然呀\'')
    time.sleep(0.5)
    print(' > Note that the \'BETA\' in the version number is the major version number 0 (beta version)')
    print(' > For example, \'XRdows 1.0 BETA __0.0.1__ V\' means that the XRdows version is \'0.1.0_0.0.1\'')
    time.sleep(0.5)
    print(' > Storage location of the mods file: \'./mods_file/...\'')
    time.sleep(0.5)
    print(' > The mods file has to go to the afdian.net website to find \'是星星与然然呀\' to download the file')
    time.sleep(0.5)
    print(f' > Version : {Version}')

def E_L():
    time.sleep(0.5)
    print(f'{Edition_logs}')
    time.sleep(0.5)

def P_T():
    XRDOWS()
    prompt()

def C_T():
    time.sleep(0.5)
    print(f'{command_table}')
    time.sleep(0.5)

def E_P():
    time.sleep(0.5)
    print(' > Is exiting')

def P_W():
    subprocess.run(os.path.join(folder, './py_C_F/P_W/plane_war_normal_edition.exe'))

def C_Z(source_folder, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), source_folder))

def hex_to_str(h):
    return ''.join([chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2)])

def M_P(self_, mode='F_D' or 'T_D'):
    try:
        file_path = os.path.join(input(f'{_14_E}'))
        self_.play_music(file_path, mode=mode)
    except:
        print(f'{_15_E}')
        M_P(self_, mode)

def R_py_F():
    try:
        file_path = os.path.join(input(f'{_16_E}'))
        with open(file_path, 'r', encoding='UTF-8') as file:
            try:
                while 1:
                    exec(file.read())
                    break
            except Exception as error:
                print(f' > Error is {error}')
                R_py_F()
    except:
        print(f'{_15_E}')
        R_py_F()

def R_exe_F():
    try:
        file_path = input(f'{_17_E}')
        subprocess.run(file_path)
    except:
        print(f'{_15_E}')
        R_exe_F()

def image_p(self_, mode='F_D' or 'T_D'):
    try:
        image_path = input(f'{_18_E}')
        screen = pygame.display.set_mode((600,600))
        image = pygame.image.load(os.path.join(image_path)).convert()
        self_.draw_images_(image, screen, mode)
    except:
        print(f'{_15_E}')
        image_p(self_, mode)

if __name__ == '__main__':
    P_T()
    E_L()
