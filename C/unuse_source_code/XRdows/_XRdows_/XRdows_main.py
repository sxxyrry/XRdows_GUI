import ctypes

ctypes.windll.kernel32.SetConsoleTitleW('XRdows')

import shutil
import pygame
import os
import time
#from XRdows_F_D import XRdows_F_D
#from XRdows_T_D import XRdows_T_D
from S_D import P_T
from consts import folder

pygame.init()
pygame.mixer.init()

class __XRdows_total__():
    def __init__(self):
        with open(os.path.join(folder, './XRdows_F_D.py'), 'r', encoding='UTF-8') as f:
            r_F_D = f.read()
            a_F_D = r_F_D + '''
        else:
            print(f' > No "{command}"')'''
        with open(os.path.join(folder, './XRdows_T_D.py'), 'r', encoding='UTF-8') as f:
            r_T_D = f.read()
            a_T_D = r_T_D + '''
        else:
            print(f' > No "{command}"')'''
        with open(os.path.join(folder, './py_C_F/XRdows/XRdows_F_D.py'), 'w', encoding='UTF-8') as f:
            f.write(a_F_D)
        with open(os.path.join(folder, './py_C_F/XRdows/XRdows_T_D.py'), 'w', encoding='UTF-8') as f:
            f.write(a_T_D)
        
        from py_C_F.XRdows.XRdows_F_D import XRdows_F_D
        from py_C_F.XRdows.XRdows_T_D import XRdows_T_D
        
        self.XRdows_F_D = XRdows_F_D
        self.XRdows_T_D = XRdows_T_D

        with open(os.path.join(folder, './py_C_F/XRdows/XRdows_F_D.py'), 'w', encoding='UTF-8') as f:
            f.write('')
        with open(os.path.join(folder, './py_C_F/XRdows/XRdows_T_D.py'), 'w', encoding='UTF-8') as f:
            f.write('')

        self.music = 0

        P_T()

        self.XRdows_F_D(self)

        pycache1 = os.path.join(folder, './__pycache__')
        pycache2 = os.path.join(folder, './py_C_F/XRdows/__pycache__')
        if os.path.exists(pycache1):
            shutil.rmtree(pycache1)
        if os.path.exists(pycache2):
            shutil.rmtree(pycache2)

    def draw_img(self, surf, img, size, x, y):
        self.surf = surf
        self.img_rect = img.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y
        self.img_size = pygame.transform.scale(img, (size))
        self.surf.blit(self.img_size,self.img_rect)

    def draw_images_(self, image, screen, mode='F_D' or 'T_D'):
        self.screen = screen
        self.image = image
        self.mode_2 = mode
        pygame.display.set_caption('XRdows I P')
        clock = pygame.time.Clock()
        pygame.display.set_icon(pygame.image.load(os.path.join(folder, './py_C_F/image/My avatar.png')).convert())
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
        self.screen.fill((0,0,0))
        self.draw_img(self.screen, self.image, (500, 500), 10, 10)
        pygame.display.update()
        if self.mode_2 == 'F_D':
            self.XRdows_F_D(self)
        elif self.mode_2 == 'T_D':
            self.XRdows_T_D(self)
            
    def sleep(self, music_file):
        self.music_file = music_file
        self.music_file_len_ = int(music_file.get_length()) + 1
        self.start = time.time()
        while 1:
            self.now = time.time()
            if int(self.now - self.start) <= self.music_file_len_:
                if self.mode_1 == 'F_D':
                    self.XRdows_F_D(self)
                elif self.mode_1 == 'T_D':
                    self.XRdows_T_D(self)
            else:
                raise RuntimeWarning()

    def play_music(self, file_path = '', file_list = [], mode = 'F_D'):
        self.mode_1 = mode
        self.file_path = file_path
        self.file_list = file_list
        if self.music >= 1:
            self.music = 0
            self.music_file.stop()
        try:
            if self.file_list != []:
                try:
                    self.music += 1
                    self.next_music = ''.join(file_list.pop(0))
                    self.music_file = pygame.mixer.Sound(self.next_music)
                    self.music_file.play()
                    self.sleep(self.music_file)
                except IndexError:
                    return
            elif self.file_path != '':
                self.music += 1
                self.music_file = pygame.mixer.Sound(os.path.join(file_path))
                self.music_file.play()
                self.sleep(self.music_file)
                return
        except:
            return


# XRdows_T = __XRdows_total__()
