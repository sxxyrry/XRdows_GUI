import tkinter as tk
import os, pathlib
from typing import Sized
from C.API import get_API

API = get_API()()

folder = pathlib.Path(__file__).parent.resolve()

def _len(__obj : Sized) -> int:
    '''Return the number of items in a container.'''
    return len(__obj) - 1

class RUNEXECFILE():
    def __init__(self, root: tk.Tk, roots=None):
        self.RUNEXECFILE = f"<class \'RUNEXECFILE\'> <RUNEXECFILE object at {hex(id(self))}> - Author: XR"
        self.root_ = tk.Frame(root)
        self.roots = roots
        self.root = root

    #def raise_error(self):
        
    def run(self, file_path: str, API: API):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                code: bytes = f.read()
                i = -1
                list_1 = code.split(b'\r\n')
                if list_1[0] != b'\x23\x58\x52\x00\x00\x00\x45\x58\x45\x43':
                    raise Exception("This file is not a EXEC file.")
                if list_1[_len(list_1)] != b'\x11\x11\x11\x45\x4E\x44\x5F\x45\x58\x45\x43':
                    raise Exception("This file is not a EXEC file.")
                for text_1 in list_1:
                    if b'\x00\x00\x10' in text_1:
                        for text_2 in text_1.split(b'\x00\x00\x10'): #调用函数
                            if text_2 == '':
                                continue
                            elif b'\x00\x00\x01' in text_2:
                                i_ = -1
                                for text_3 in [i.decode() for i in text_2.split(b'\x00\x00\x01 ')]: #获取并使用方法
                                    i_ += 1
                                    if i_ != 0 and text_3 == '':
                                        raise Exception('SyntaxError')
                                    elif text_3 == 'API.create_and_get_Terminal_API':
                                        print('API.create_and_get_Terminal_API')
                                        API.create_and_get_Terminal_API()(self.root, self.roots)
                                    else:
                                        pass
                        

    def __eq__(self, other):
        try:
            temp = other.RUNEXECFILE
            return True
        except:
            return False
        
    def __str__(self):
        return self.RUNEXECFILE
    
root = tk.Tk()
root.geometry('800x600')

CustomNotebook = API.get_CustomNotebook_API()()
last_maxsize = (root.winfo_screenheight(), root.winfo_screenwidth())

def on_resize():
    global last_maxsize
    if root.wm_maxsize() != last_maxsize:
        last_maxsize = (root.winfo_screenheight(), root.winfo_screenwidth())
        CustomNotebook.config(height=last_maxsize[0], width=last_maxsize[1])
        CustomNotebook.update()

    CustomNotebook.after(1, on_resize)

CustomNotebook.after(100, on_resize)
#CustomNotebook.config(width=800, height=600)
CustomNotebook.pack()

runexecfile = RUNEXECFILE(root, CustomNotebook)

runexecfile.run(os.path.join(folder, './C/XRdows/terminal/terminal.exec'), API)

root.mainloop()
