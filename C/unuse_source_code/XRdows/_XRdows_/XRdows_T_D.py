import webbrowser
import pygame
import os
import time
from S_D import (
    E_P,
    P_W,
    E_L,
    C_T,
    C_Z,
    M_P,
    R_py_F,
    R_exe_F,
    image_p
)
from consts import (
    folder,
    _1_E,
    _2_E,
    _3_E,
    _5_E,
    _6_E,
    _7_E,
    _11_E,
    _12_E,
    _13_E
)

pygame.init()
pygame.mixer.init()

def XRdows_T_D(self):

    running = True

    while running:
        time.sleep(0.5)
        command = input(f'{_1_E}')
        if command == 'C_T':
            C_T()
        elif command == 'P_W':
            print(f'{_2_E}')
            P_W()
            print(f'{_3_E}')
            time.sleep(0.5)
        elif command == '_EXIT':
            E_P()
            time.sleep(1)
            running = False
            return
        elif command == ':wq':
            print(' > :wq')
        elif command == '_E_L':
            E_L()
        elif command == '_I_H_':
            webbrowser.open(os.path.join(folder, './py_C_F/html/introduce.html'))
            time.sleep(1)
        elif command == 'Deve_mode_False':
            running = False
            self.XRdows_F_D(self)
        elif command == 'C_F':
            try:
                time.sleep(0.5)
                C_F_P = input(f'{_5_E}')
                path = os.path.join(C_F_P)
                with open(path, 'w') as file:
                    time.sleep(0.5)
                    D_C = input(f'{_6_E}')
                    file.write(D_C)
            except:
                time.sleep(1)
                print(f'{_7_E}')
        elif command == '__code__':
            try:
                path = os.path.join(folder, input(f'{_11_E}'))
                C_Z(os.path.join(folder), path + '\\code.CODE')
            except:
                time.sleep(1)
                print(f'{_7_E}')
        elif command == '__mode__':
            time.sleep(1)
            print(f' > Deve_mode is True')
        elif command == '__Self_destruction__':
            time.sleep(1)
            print(f'{_12_E}')
            try:
                time.sleep(1)
                path = os.path.join(folder, input(f'{_11_E}'))
                C_Z(os.path.join(folder), path + '\\code.CODE')
            except:
                time.sleep(1)
                print(f'{_7_E}')
            time.sleep(1)
            os.remove(os.path.join(folder, './S_D.py'))
            os.remove(os.path.join(folder, './XRdows_text.py'))
        elif command == 'print()':
            content = input(f'{_13_E}')
            print(f' > {content}')
        elif command == 'M_P':
            M_P(self, 'T_D')
        elif command == 'R_py_F':
            R_py_F()
        elif command == 'R_exe_F':
            R_exe_F()
        elif command == 'M_P_D':
            folder_path = os.path.join(folder, './music_file')
            print(' > The file name format is \'music_{i(1 start)}_{name}\'')
            file_list_ = []
            i = 0
            for filename in os.listdir(folder_path):
                i += 1
                if f'music_{i}_' in filename:
                    temp = ''.join(filename)
                    list_temp_ = temp.split('music')
                    if list_temp_[0] == '':
                        if os.path.isfile(os.path.join(folder_path, filename)):
                            file_list_.append([os.path.join(folder_path+'/'+filename)])
                            with open(os.path.join(folder_path, filename), 'r', encoding='UTF-8') as file:
                                file_name = ''.join(file.name)
                                list_ = file_name.split('.')
                                list_len_ = len(list_) - 1
                                if list_[list_len_] == 'mp3' or list_[list_len_] == 'flac':
                                    self.play_music(file_list=file_list_, mode='F_D')
                                else:
                                    print(f' > This file ({filename}) is not playable (mp3 or flac file suffix required)')
                    else:
                        print(' > The file name is formatted incorrectly')
        elif command == '再醒':
            self.music_file = pygame.mixer.Sound(os.path.join(folder, './music_file/music_1_wake——中文填词 《再醒》.flac'))
            self.music_file.play()
            time.sleep(14)
            print(' > 青涩的笔\n > 描绘火柴\n > 电子动脉\n > 迸发热爱\n > 鼠标摇摆\n > 次元铺排\n > 没有对白\n > 却无比精彩\n > 弱小抗争迫害\n > 哪怕失败（受害者）\n > 谁说蝴蝶\n > 难逃沧海\n > 无敌背后\n > 力量诅咒（天选）\n > 为了自由赌上所有\n > 我从混沌中醒来（火动4）\n > 生命不止破坏\n > 创造千奇百怪\n > 有惊喜才会等待\n > 我穿越壁垒归来（天选归来）\n > 网络无需主宰\n > 我挡在黑刃之外（四色就义）\n > 伙伴是无可替代\n > 【匠心雕饰 力求精致】绿\n > 【谨慎矜持 冷静多智】黄\n > 【羽落惊矢 广布绿植】蓝\n > 【纵意心赤 英勇耿直】红\n > 觉醒之时\n > 超越生死\n > 再次降临的神识\n > 请容我在此\n > 跪下身姿\n > 挥手是新的开始\n > 没有复杂台词\n > 仍是史诗\n > 源于童稚\n > 忠于本质\n > 无限故事\n > 无穷构思\n > 威力加持\n > 热血永不消逝（猪猪）\n > 向往着安逸自在\n > 突然神游天外\n > 来一场 友谊赛\n > 享受新维度感慨\n > 我已经心潮澎湃\n > 生存大师登台\n > 不自觉 向前迈\n > Welcome to the MC（麦快）（MINECRAFT）！\n > 【钓竿缠丝 音符诠释】绿\n > 【发明务实 令晶红石】黄\n > 【偏爱疣食 魔药调制】蓝\n > 【愿作先斥 万兽为侍】红\n > 并肩去旅行\n > 冒险不停\n > 这风光一览无尽\n > 那一刻温情\n > 援手握紧\n > 像黄金闪耀我心\n > 别离开\n > 别离开\n > 别离开\n > 我身边\n > 打不开\n > 打不开\n > 打不开\n > 生死间\n > 我的爱\n > 我的爱\n > 我的爱\n > 已不见\n > 让悲哀\n > 让阴霾\n > 让魔怪\n > 变尘埃\n > 难舍至亲被吞噬（ko心结）\n > 憎欲一念灭世\n > 弱小的\n > 被无视（小紫心结）\n > 握不住落花飘逝\n > 告别了恶魔天使\n > 此刻不再迷失\n > 又回到\n > 末地时\n > 别回头向前冲刺\n > 【歌尽心事 花火疾驰】紫\n > 【我即我誓 心作鞘翅】紫\n > 【舍命对峙 过往交织】橙王\n > 【恨不能消 唯爱能止】紫、橙王\n > 继续前进\n > 互掷登顶\n > 生命是永无止境\n > 伤痛抚平\n > 万众归心\n > 创盛世举杯共赢')
        elif command == 'I_P':
            image_p(self, 'T_D')
        elif command == 'R_I_P':
            pygame.display.quit()
        elif command == 'Force_quit':
            os._exit(0)
        elif '__scode__' in command:
            file_t = {
                'consts',
                'S_D',
                'XRdows_text',
                'XRdows',
            }
            lists = command.split('__scode__')
            print(lists)
            if len(lists) == 2:
                if lists[1] != '':
                    lists[::-1]
                    if lists[1] in file_t:
                        with open(os.path.join(folder, './', lists[1] + '.py'), 'r', encoding='UTF-8') as f:
                            text = ''.join(f.read())
                            lists_ = text.split('\n')
                            for texts in lists_:
                                print(' > ' + texts)
                    else:
                        print(' > ')
                else:
                    print(' > ')
        elif command == 'XRthon_editor':
            from XRthon_editor import XRthon_editor
            XRthon_editor()