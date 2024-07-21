import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Menu, Listbox, Scrollbar, PhotoImage, scrolledtext # type: ignore
from PIL import Image, ImageTk
# from C.ERROR_CLASS import Not_Implemented
# from C.XRdows.custom import CustomNotebook
# from C.folders import folder
# from C.config import config, switch_language, config_init
from C.init import __inits__
from C.API import get_API
import shutil
import os
import pygame
import random
import time

pygame.init()
pygame.mixer.init()

time_label = None

API = get_API()()

config_and_function_tuple = API.config_and_config_function_API()

config = config_and_function_tuple[0]

config_init = config_and_function_tuple[1]
get_config = config_and_function_tuple[2]
switch_file_language = config_and_function_tuple[3]

find_largest_integer = API.create_windows_auxiliary_functions_API()

folder = API.get_folder_API()


with open(os.path.join(folder, './XRdows/Edition_logs/Edition_logs.text'), 'r') as fp:
    Edition_logs: str = fp.read()

if 'language' in config:
    language: str = config['language']  # type: ignore
else:
    '''
    try:
        temp = OS_initiates_self_test_pro # type: ignore
    except:
        OS_initiates_self_test_pro: str = 'BIOS'
    '''
    try:
        temp = language # type: ignore
    except:
        language: str = 'zh-cn'
    
    config_init('zh-cn')
    config = API.Recapture_config_API()

'''

if 'OS_initiates_self-test_pro' in config:
    OS_initiates_self_test_pro: str = config['OS_initiates_self-test_pro'] # type: ignore
else:
    try:
        temp = OS_initiates_self_test_pro
    except:
        OS_initiates_self_test_pro: str = 'BIOS'
    try:
        temp = language
    except:
        language: str = 'zh-cn'
    
    config_init(language, 'BIOS')
    config = API.Recapture_config_API()

if OS_initiates_self_test_pro == 'BIOS':
    import C.XRdows.OS_initiates_self_test_pro.BIOS as BIOS
    os.startfile(os.path.join(folder, './XRdows/OS_initiates_self_test_pro/BIOS.py'))
    time.sleep(BIOS.get_all_sleep_num_sum())
elif OS_initiates_self_test_pro == 'UEFI':
    import C.XRdows.OS_initiates_self_test_pro.UEFI as UEFI
    os.startfile(os.path.join(folder, './XRdows/OS_initiates_self_test_pro/UEFI.py'))
    time.sleep(UEFI.get_all_sleep_num_sum())
'''


try:
    __inits__()
except:
    pass

class ListBoxItem:
    def __init__(self, image, text):
        self.image = image
        self.text = text

    def __repr__(self):
        return self.text

class startup_():
    def __init__(self, root: tk.Tk):
        self.roots = API.get_CustomNotebook_API()()
        self.API = get_API()()
        self.File_API = self.API.get_file_API()()
        self.i:list[int] = []
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        global config
        if 'user_data_user_1' in config: # type: ignore
            self.user_data_user_1: dict[str, str] = config['user_data_user_1'] # type: ignore
            self.user_1_name = self.user_data_user_1['name'] # type: ignore
            self.user_1_states = self.user_data_user_1['states'] # type: ignore
            self.user_1_password = self.user_data_user_1['password'] # type: ignore
            if self.user_1_password is None:

                self.user_1_password = ''
        else:
            config_init(language)
            config = API.Recapture_config_API()
            self.user_data_user_1: dict[str, str] = config['user_data_user_1'] # type: ignore
            self.user_1_name = self.user_data_user_1['name'] # type: ignore
            self.user_1_states = self.user_data_user_1['states'] # type: ignore
        root.after(1000, self.__dels__)
        pass

    def Version_(self) -> str:
        E_L_T: str = ''.join(Edition_logs)
        E_L_T_L: list[str] = E_L_T.split('\n')
        L_: list[str] = []
        for text in E_L_T_L:
            if 'V' and 'BETA' in text:
                L_.append(text)
        #print(L_)
        text_1: list[str] = L_[len(L_) - 1].split(' > ')
        text_2: list[str] = text_1[1].split(' V')
        #print(text_2)
        '''
        if '(BETA VERSION IN DEVELOPMENT)' in text_1[1]:
            Version = text_2[0] + ' V' + text_2[1]
        else:
        '''
        Version: str = text_2[0]
        #print(Version)
        return Version

    def on_closing(self):
        self.exit_program()

    def __dels__(self):
        shutil.rmtree(os.path.join(folder, './__pycache__'))

    def exit_program(self):
        """退出程序的函数"""
        is_quit = False
        if language == 'zh-cn':
            if messagebox.askyesno("关机", "确定要关机吗?"):
                is_quit = True
        elif language == 'en-us':
            if messagebox.askyesno("Shutdown", "Are you sure you want to Shutdown?"):
                is_quit = True

        if is_quit:
            music = pygame.mixer.Sound(os.path.join(folder, './XRdows/music/XRdows Shutdown.wav'))
            music.set_volume(100)
            music.play()
            time.sleep(music.get_length())
            root.destroy()

    def btn_c(self):
        btn_c_root = tk.Frame(root)
        if language == 'zh-cn':
            self.roots.add(btn_c_root, text=f"按钮注释")
        elif language == 'en-us':
            self.roots.add(btn_c_root, text=f"button comments")

        if language == 'zh-cn':
            drop_down_list = ['系统',
                                         '关机']

        drop_down_box = ttk.Combobox(btn_c_root, values=drop_down_list)

    def c_w_e_d(self):
        for i in self.i:
            if i == 0:
                continue
            try:
                self.roots.forget(i)
            except:
                continue

    def terminal(self):
        """创建终端"""
        API.create_and_get_Terminal_API()(root, self.roots)

        self.i = [self.roots.tab(i)['padding'][0] + i for i in range(self.roots.index(tk.END))]

        self.roots.select(find_largest_integer(self.i))

        '''
    def create_menu(self, root: tk.Tk):
        """创建菜单栏"""
        # 创建主菜单
        main_menu = Menu(root)
        root.config(menu=main_menu)
'''
    def _startup_(self):
        global screens, time_label
        
        for widget in screens.winfo_children():
            widget.destroy()

        screens.destroy()

        #self.roots = CustomNotebook()
        self.roots.pack(side="top", fill="both", expand=True)

    def del_back_files(self):
        for dirpath, dirnames, filenames in os.walk(os.path.join(folder, './XRdows')):
            for filename in filenames:
                if filename.endswith('.back'):
                    file_path = os.path.join(dirpath, filename)
                    os.remove(file_path)

    def Document_renderer(self, file_path: str):
        API.get_Document_renderer_API()    \
        ().                                 \
        Document_display(os.path.join(file_path), root, self.roots)

        self.i = [self.roots.tab(i)['padding'][0] + i for i in range(self.roots.index(tk.END))]

        self.roots.select(find_largest_integer(self.i))

    def show_main_ui(self):
        """显示主界面函数"""
        global screens, time_label
        
        screens = tk.Frame(root, bg='white', height=500)
        screens.config(bg='lightblue')
        if language == 'zh-cn':
            self.roots.add(screens, text='桌面')
        elif language == 'en-us':
            self.roots.add(screens, text='desktop')

        self.i = [self.roots.tab(i)['padding'][0] + i for i in range(self.roots.index(tk.END))]

        self.roots.protect_tab(0)
        self.roots.select(0)
        
        images_ = Image.open(os.path.join(folder, './XRdows/image/XR.png'))
        _images = images_.resize((44, 32), Image.LANCZOS)
        _image = ImageTk.PhotoImage(_images)

        btn_f = tk.Frame(screens, bg='lightblue')

        sys_btn_f = tk.Frame(btn_f, bg='lightblue')

        ter_btn_f = tk.Frame(btn_f, bg='lightblue')
        
        if language == 'zh-cn':
            sys_button = tk.Button(sys_btn_f, image=_image, width=44, height=32, command=self.system_)
            sys_button.image = _image # type: ignore
            sys_button.pack(side=tk.LEFT, padx=0, pady=0)
            
            sys_lbl = tk.Label(sys_btn_f, text="系统", font=("黑体", 12), bg='lightblue')
            sys_lbl.pack(padx=10, pady=0)

            terminal_btn = tk.Button(ter_btn_f, image=_image, width=44, height=32, command=self.terminal)
            terminal_btn.image = _image # type: ignore
            terminal_btn.pack(side=tk.LEFT, padx=0, pady=0)

            terminal_lbl = tk.Label(ter_btn_f, text="终端", font=("黑体", 12), bg='lightblue')
            terminal_lbl.pack(padx=10, pady=0)

            sys_btn_f.pack(side=tk.TOP, padx=0, pady=0)

            ter_btn_f.pack(side=tk.TOP, padx=0, pady=10)

            btn_f.pack(side=tk.LEFT, padx=20, pady=0)

            self.File_API.fetch_file_folder(screens, root, self.roots) # type: ignore

            # 显示主界面内容
            #self.create_menu(root)
            taskbar = tk.Frame(root, bg='gray', height=50)
            taskbar.pack(side=tk.BOTTOM, fill=tk.X)

            label = tk.Label(screens, bg='lightblue', text="欢迎来到XRdows操作系统!", font=("黑体", 16))
            label.pack(side=tk.BOTTOM, pady=20)

            root.after(1000, label.destroy)

            time_label = tk.Label(taskbar, text="", font=("黑体", 12), fg="white", bg="gray")
            time_label.pack(side=tk.RIGHT, padx=10)
            user_anme = tk.Label(taskbar, text=self.user_1_name, font=("黑体", 12), fg="white", bg="gray")
            user_anme.pack(side=tk.LEFT)
            btn_exit = tk.Button(taskbar, text="关机", command=self.exit_program)
            btn_exit.pack(side=tk.LEFT, padx=10)
            btn_c_w_e_d = tk.Button(taskbar, text="关闭除桌面外的所有窗口", command=self.c_w_e_d)
            btn_c_w_e_d.pack(side=tk.LEFT, padx=10)

            self.update_time()
        elif language == 'en-us':
            sys_button = tk.Button(sys_btn_f, image=_image, width=44, height=32, command=self.system_)
            sys_button.image = _image # type: ignore
            sys_button.pack(side=tk.LEFT, padx=0, pady=0)
            
            sys_lbl = tk.Label(sys_btn_f, text="system", font=("黑体", 12), bg='lightblue')
            sys_lbl.pack(padx=10, pady=0)

            sys_btn_f.pack(side=tk.LEFT, padx=20, pady=0)

            self.File_API.fetch_file_folder(screens, root, self.roots) # type: ignore

            # 显示主界面内容
            #self.create_menu(root)
            taskbar = tk.Frame(root, bg='gray', height=40)
            taskbar.pack(side=tk.BOTTOM, fill=tk.X)

            label = tk.Label(screens, bg='lightblue', text="Welcome to the XRdows operating system!", font=("黑体", 16))
            label.pack(side=tk.BOTTOM, pady=20)

            root.after(1000, label.destroy)

            start_button = tk.Button(taskbar, text="start", width=6)
            start_button.pack(side=tk.LEFT, padx=10)
            time_label = tk.Label(taskbar, text="", font=("黑体", 12), fg="white", bg="gray")
            time_label.pack(side=tk.RIGHT, padx=10)
            btn_exit = tk.Button(taskbar, text="Shutdown", command=self.exit_program)
            btn_exit.pack(side=tk.LEFT, padx=10)
            self.update_time()

    def update_time(self):
        global time_label
        if language == 'zh-cn':
            time_label.config(text=time.strftime("%Y-%m-%d %A %H:%M:%S")) # type: ignore
        elif language == 'en-us':
            time_label.config(text=time.strftime("%d-%m-%Y %A %H:%M:%S")) # type: ignore

        root.after(500, self.update_time)

    def system_(self):
        global sys_root
        sys_root = tk.Frame(root)
        if language == 'zh-cn':
            text_lbl = tk.Label(sys_root, text="系统")
            text_lbl.pack()



            temp_ = self.Version_()
            if '(indev BETA version)' in temp_:
                version_text: str = temp_.replace(' (indev BETA version)', '（开发中的测试版本)')
            else:
                version_text = temp_

            about_system = scrolledtext.ScrolledText(sys_root, state='disabled')
            about_system.pack()

            about_system.config(state='normal')
            about_system.insert(tk.END, f"""\
作者（B站）：                   是星星与然然呀
CustomNotebook的作者（B站）：   LoveProgramming
关于：
    系统：XRdows GUI
    系统版本：{version_text}
    系统语言：简体中文
赞助链接：
    ······
（整个系统，除了CustomNotebook他全是是星星与然然呀独自一人完成）\
""")
            about_system.config(state='disabled')

            languages = ['简体中文', 'English']

            fae = tk.Frame(sys_root, bg='white')
            fae.pack()
            lbl = tk.Label(fae, text="选择语言（重启后生效）")
            lbl.pack()



        elif language == 'en-us':
            text_lbl = tk.Label(sys_root, text="system")
            text_lbl.pack()

            about_sys = tk.Label(sys_root, text=f"System verison：{self.Version_()}")
            about_sys.pack()

            languages = ['English', '简体中文']

            fae = tk.Frame(sys_root, bg='white')
            fae.pack()
            lbl = tk.Label(fae, text="Select Language (Effective after Restart)")
            lbl.pack()

        self.language_dropdown = ttk.Combobox(fae, values=languages)
        self.language_dropdown.bind("<<ComboboxSelected>>", self.on_language_change)
        self.language_dropdown.pack()

        if language == 'zh-cn':
            self.roots.add(sys_root, text="系统")
        elif language == 'en-us':
            self.roots.add(sys_root, text="system")

        self.i = [self.roots.tab(i)['padding'][0] + i for i in range(self.roots.index(tk.END))]

        self.roots.select(find_largest_integer(self.i))

    def on_language_change(self, event):
        selected_language = self.language_dropdown.get()
        switch_file_language(selected_language)
        global config
        config = API.Recapture_config_API()

    def startup_screen(self):
        """开机界面"""
        global screens
        screens = tk.Frame(root, bg='white')
        screens.pack(fill=tk.BOTH, expand=True)

        images_ = Image.open(os.path.join(folder, './XRdows/image/XR.png'))
        startup_images = images_.resize((176, 128), Image.LANCZOS)
        startup_image = ImageTk.PhotoImage(startup_images)

        time.sleep(random.randint(1, 2))
        music = pygame.mixer.Sound(os.path.join(folder, './XRdows/music/XRdows Startup.wav'))

        if language == 'zh-cn':
            images = tk.Label(screens, width=176, height=128, image=startup_image)
            images.pack()

            text1 = tk.Label(screens, text="XRdows操作系统", font=("黑体", 24), pady=50)
            text1.pack()

            label = tk.Label(screens, text="系统正在启动   ", font=("黑体", 24), pady=50)
            label.pack()

            for i in range(3):
                label.config(text=f"系统正在启动" + "." * int(i + 1) + " " * int(3 - i - 1))
                root.update()
                time.sleep(1)

        elif language == 'en-us':
            images = tk.Label(screens, width=176, height=128, image=startup_image)
            images.pack()

            text1 = tk.Label(screens, text="XRdows operating system", font=("黑体", 24), pady=50)
            text1.pack()

            label = tk.Label(screens, text="System is starting   ", font=("黑体", 24), pady=50)
            label.pack()

            for i in range(3):
                label.config(text=f"System is starting" + "." * int(i + 1) + " " * int(3 - i - 1))
                root.update()
                time.sleep(1)
        
        music.set_volume(100)
        music.play()

        time.sleep(0.5)

        self._startup_()

        root.after(0, self.show_main_ui)

def inits():
    pass

def main():
    """主函数"""
    global root
    root = tk.Tk('root')
    startup: startup_ = startup_(root)
    root.geometry("800x600")
    if language == 'zh-cn':
        root.title("XRdows操作系统")
    elif language == 'en-us':
        root.title("XRdows operating system")

    #root.update()

    startup.startup_screen()  # 首先显示开机界面

    root.mainloop()

if __name__ == "__main__":
    main()
