def get_API():
    import os, tkinter as tk
    from PIL import Image, ImageTk
    from tkinter import Listbox
    from typing import Callable, Sized, List, Literal, TypedDict, Any
    from tkinter import messagebox
    from tkinter import scrolledtext

    class File_notexists(BaseException):
        def __init__(self, *args, **kwargs):
            self.File_notexists = f'<class \'File_notexists\'> <File_notexists object at {hex(id(self))}> - Author: XR'
            super().__init__(*args, **kwargs)
        
        def __eq__(self, other):
            try:
                temp = other.File_notexists
                return True
            except:
                return False

        def __str__(self):
            return self.File_notexists
        
    class File_extension_notcorrect(BaseException):
        def __init__(self, *args, **kwargs):
            self.File_extension_notcorrect = f'<class \'File_extension_notcorrect\'> <File_extension_notcorrect object at {hex(id(self))}> - Author: XR'
            super().__init__(*args, **kwargs)
        
        def __ed__(self, other):
            try:
                temp = other.File_extension_notcorrect
                return True
            except:
                return False
        
        def __str__(self):
            return self.File_extension_notcorrect

    def create_and_get_CustomNotebook():
        import tkinter.ttk as ttk
        import tkinter as tk

        class CustomNotebook(ttk.Notebook):
            """A ttk Notebook with close buttons on each tab"""

            __initialized = False

            def __init__(self, *args, **kwargs):
                self.CustomNoteboot = f'<class \'CustomNothbook\'> <CustomNothbook object at {hex(id(self))}> - Author: XR'
                if not self.__initialized:
                    self.__initialize_custom_style()
                    self.__inititialized = True
                    self._protected_indices = set()

                # self.i: list[int] = []

                kwargs["style"] = "CustomNotebook"
                ttk.Notebook.__init__(self, *args, **kwargs)

                self._active = None

                self.bind("<ButtonPress-1>", self.on_close_press, True)
                self.bind("<ButtonRelease-1>", self.on_close_release)
                self.bind("<<NotebookTabClosed>>", self.on_tab_close)
                
            def protect_tab(self, index):
                """Mark the tab of the specified index as protected"""
                self._protected_indices.add(index)

            def unprotect_tab(self, index):
                """Deselect the protection status of the tab for the specified index"""
                if index in self._protected_indices:
                    self._protected_indices.remove(index)

            def on_close_press(self, event):
                """Called when the button is pressed over the close button"""

                element = self.identify(event.x, event.y)

                if "close" in element:
                    index = self.index("@%d,%d" % (event.x, event.y))
                    if index in self._protected_indices:
                        pass
                    else:
                        widget = event.widget  # 获取当前Notebook实例
                        index = widget.index("current")  # 获取当前选中的标签页索引
                        frame = widget.nametowidget(widget.tabs()[index])  # 获取对应的Frame
                        frame.destroy()  # 销毁Frame
                        self.state(['pressed'])
                        self._active = index
                        # self.i = super().tabs()
                

            def on_close_release(self, event):
                """Called when the button is released over the close button"""
                if not self.instate(['pressed']):
                    return

                element = self.identify(event.x, event.y)
                try:
                    index = self.index("@%d,%d" % (event.x, event.y))
                except:
                    return

                if "close" in element and self._active == index:
                    widget = event.widget  # 获取当前Notebook实例
                    index = widget.index("current")  # 获取当前选中的标签页索引
                    frame = widget.nametowidget(widget.tabs()[index])  # 获取对应的Frame
                    frame.destroy()  # 销毁Frame
                    self.forget(index)
                    self.event_generate("<<NotebookTabClosed>>")

                self.state(["!pressed"])
                self._active = None

            def on_tab_close(self, event):
                """
                当Notebook的标签页被关闭时，自动销毁对应的Frame。
                """
                widget = event.widget  # 获取当前Notebook实例
                index = widget.index("current")  # 获取当前选中的标签页索引
                frame = widget.nametowidget(widget.tabs()[index])  # 获取对应的Frame
                frame.destroy()  # 销毁Frame
                #widget.forget(index)  # 从Notebook中移除该标签页

            def __initialize_custom_style(self):
                style = ttk.Style()
                self.images = (
                    tk.PhotoImage("img_close", data='''
                        R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                        d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                        5kEJADs=
                        '''),
                    tk.PhotoImage("img_closeactive", data='''
                        R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                        AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                        '''),
                    tk.PhotoImage("img_closepressed", data='''
                        R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                        d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                        5kEJADs=
                    ''')
                )

                style.element_create("close", "image", "img_close",
                                    ("active", "pressed", "!disabled", "img_closepressed"),
                                    ("active", "!disabled", "img_closeactive"), border=8, sticky='')
                style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
                style.layout("CustomNotebook.Tab", [
                    ("CustomNotebook.tab", {
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.padding", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.focus", {
                                        "side": "top",
                                        "sticky": "nswe",
                                        "children": [
                                            ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                            ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                        ]
                                    })
                                ]
                            })
                        ]
                    })
                ])

            def __eq__(self, other):
                try:
                    temp = other.CustomNotebook
                    return True
                except:
                    return False
                
            def __str__(self):
                return self.CustomNoteboot

        return CustomNotebook

    def get_find_largest_integer():
        def find_largest_integer(numbers: list[int]):
            if type(numbers) != list:
                raise TypeError("参数必须是列表")
            if not numbers:
                raise ValueError("列表不能为空")
            if not all(isinstance(num, int) for num in numbers):
                raise TypeError("列表中的元素必须是整数")
            

            largest = numbers[0]
            for number in numbers:
                if number > largest:
                    largest = number
                if number == largest:
                    pass

            return largest

        return find_largest_integer

    def get_config_and_function() -> tuple[dict[str,
                                                str | dict[str, str]],
                                        Callable[[str#,
                                                  #str
                                                  ],
                                                    None],
                                        Callable[...,
                                                    dict[str,
                                                        str | dict[str, str]]],
                                        Callable[[str],
                                                    None]]:
        """
        Returns the config in the form of a tuple along with functions about the config
        (config, config_init, get_config, switch_file_language)
        config: Dictionary about config
        config_init: Initialize the config
        get_config: Get the config
        switch_file_language: Switch the language of the config file
        """
        import os, yaml
        import pathlib

        folder: pathlib.Path = pathlib.Path(__file__).parent.resolve()

        # Global variables without type annotations
        config: dict[str, str | dict[str, str]] = {}
        text = ""

        def _switch_language(language: str):
            if language == '简体中文':
                language = 'zh-cn'
            elif language == 'English':
                language = 'en-us'
            elif language == 'zh-cn':
                pass
            elif language == 'en-us':
                pass
            return language

        def config_init(language: str):
            nonlocal config
            language = _switch_language(language)
            with open(os.path.join(folder, './XRdows/config/config.yaml'), 'w', encoding='UTF-8') as f:
                yaml.dump({'language': language,
                           'OS_initiates_self-test_pro': 'BIOS',
                            'urse_data_administrator' : {
                                'name' : "administrator",
                                'states' : "administrator",
                            },
                            'user_data_user_1': {
                                'password': "null",
                                'name' : "user_1",
                                'states' : "normal_user",
                            }
                            }, f)
            
            config = get_config()

        def get_config() -> dict[str, str | dict[str, str]]:
            """Reads the configuration file"""
            with open(os.path.join(folder, './XRdows/config/config.yaml'), 'r') as f:
                text = f.read()  # text content read from file
                config = yaml.safe_load(text)  # parse YAML into dictionary
            if config is None:
                config = {}
            
            return config

        def switch_file_language(language: str) -> None:
            """Switch the language of the application."""
            language = _switch_language(language)
            with open(os.path.join(folder, './XRdows/config/config.yaml'), 'w') as f:
                yaml.dump({'language': language,
                            'urse_data_administrator' : {
                                'name' : "administrator",
                                'states' : "administrator",
                            },
                            'user_data_user_1': {
                                'password': "null",
                                'name' : "user_1",
                                'states' : "normal_user",
                            }
                            }, f)

        # Ensure the configuration is loaded when this module is imported
        config = get_config()

        return (config, config_init, get_config, switch_file_language)

    def get_folder():
        import pathlib

        folder = pathlib.Path(__file__).parent.resolve()

        return folder

    CustomNotebook = create_and_get_CustomNotebook()

    def get_terminal():
        with open(os.path.join(get_folder(), './XRdows/Terminal_C_T/Terminal_command_table.text'), 'r') as f:
            Terminal_C_T = f.read()
        
        with open(os.path.join(get_folder(), './XRdows/Edition_logs/Edition_logs.text'), 'r') as f:
            Edition_logs = f.read()

        class Terminal():
            def __init__(self, root: tk.Tk, roots, func: object | None=None, *func_arg, **func_kwargs):
                self.Terminal = f"<class \'Terminal\'> <Terminal object at {hex(id(self))}> - Author: XR"
                self.root = tk.Frame(root)
                self.roots = roots
                self.root_ = root

                # self.root.title("终端")
                # self.root.geometry("800x600")
                
                # 创建一个滚动文本框用于显示输出
                self.output_area = scrolledtext.ScrolledText(self.root, state='disabled', height=20)
                self.output_area.pack(fill=tk.BOTH, expand=True)              

                self.output_area.config(bg='black', fg='white')
                self.output_area.configure(state='normal')
                self.output_area.insert(tk.END, " >>> \n\n")
                self.output_area.configure(state='disabled')
                
                self.Frame = tk.Frame(self.root, bg='black')
                self.Frame.pack(fill=tk.X)
                
                self.text = tk.Label(self.Frame, text=" >>> ", bg='black', fg='white')
                self.text.pack(fill=tk.X, side=tk.LEFT, pady=1)
                # 创建一个输入框用于接收命令
                self.input_var = tk.StringVar()
                self.input_entry = tk.Entry(self.Frame, textvariable=self.input_var, bg='black', fg='white', insertbackground='white')
                self.input_entry.pack(fill=tk.X, pady=1)
                
                # 绑定回车键事件处理函数
                if func is None:
                    self.input_entry.bind("<Return>", lambda event: self.execute_command(event, root))
                else:
                    self.input_entry.bind("<Return>", lambda event: func(event, *func_arg, **func_kwargs)) # type: ignore

                self.button_Frame = tk.Frame(self.root, bg='black')
                self.button_Frame.pack(fill=tk.BOTH, side=tk.BOTTOM)
                # 添加一个执行按钮
                if func is None:
                    self.execute_button = tk.Button(self.button_Frame, text="执行", command=lambda event=None: self.execute_command(event, root), bg='black', fg='white')
                    self.execute_button.pack(side=tk.LEFT)
                else:
                    self.execute_button = tk.Button(self.button_Frame, text="执行", command=lambda event=None: func(event, *func_arg, **func_kwargs), bg='black', fg='white') # type: ignore
                    self.execute_button.pack(side=tk.LEFT)

                if language == "zh-cn":
                    roots.add(self.root, text="终端")

            def execute_command(self, event=None, root: tk.Tk=None, func: object | None=None, *func_arg, **func_kwargs): # type: ignore
                """执行用户输入的命令，并显示输出"""
                command = self.input_var.get()
                self.input_var.set("")  # 清空输入框
                '''
                get_text = self.output_area.get("1.0", tk.END)
                if get_text == " >>> ":
                    self.output_area.config(state='normal')  # 允许编辑以添加新内容
                    self.output_area.insert(tk.END, f"{command}\n")
                else:
                '''
                self.output_area.config(state='normal')  # 允许编辑以添加新内容
                self.output_area.insert(tk.END, f" >>> {command}\n")
                if func is None:
                    if command == "exit":
                        self.root.destroy()
                        return
                    elif command == "config":
                        self.output_area.insert(tk.END, ' > ' + str(config) + '\n')
                    elif command == "clear":
                        self.output_area.delete("1.0", tk.END)
                        self.output_area.config(state='normal')
                        self.output_area.insert(tk.END, " >>> \n\n")
                        self.output_area.config(state='disabled')
                    elif command in ["Terminal command table", "ter_C_T"]:
                        self.output_area.insert(tk.END, Terminal_C_T + '\n')
                    elif command == "Developers":
                        self.output_area.insert(tk.END, f' > command ({command}) isn\'t a coammand' + "\n")
                    elif command in ["Edition logs", "E_L"]:
                        self.output_area.insert(tk.END, Edition_logs + '\n')
                    elif "startfile" in command:
                        if command.split('startfile ')[0] == '':
                            path_ = command.split('startfile ')[1]
                            if path_.split('./')[0] == '':
                                path = os.path.join(get_folder(), path_)
                            else:
                                path = os.path.join(path_)
                            if os.path.exists(path):
                                roots = self.roots
                                File_API = get_API()().get_file_API()()
                                if path.split('.')[-1] == 'text':
                                    File_API.file_editor(root, roots, path)
                                elif path.split('.')[-1] == 'txt':
                                    File_API.file_editor(root, roots, path)
                                else:
                                    if os.path.exists(path):
                                        root_directory, item_name = os.path.split(path)
                                        with open(os.path.join(root_directory, item_name), 'r', encoding='UTF-8') as file:
                                            file_text = file.read()
                                            class MYFrame(tk.Frame):
                                                def destroy(self) -> None:
                                                    save_file()
                                                    return super().destroy()
                                            file_read_root = MYFrame(root)
                                            if language == 'zh-cn':
                                                text_lbl = tk.Label(file_read_root, text=f"文件编辑器（{item_name}）")
                                                text_lbl.pack()

                                                def save_file(event=None):
                                                    with open(os.path.join(root_directory, item_name), 'r', encoding='UTF-8') as file:
                                                        file_text = file.read()
                                                    new_list = file_read_area.get("1.0", tk.END).split("\n")
                                                    new_list.pop(len(new_list)-1)
                                                    new_text = '\n'.join(new_list)
                                                    
                                                    if new_text != file_text:
                                                        with open(os.path.join(root_directory, item_name + '.back'), 'w', encoding='UTF-8') as file1:
                                                            with open(os.path.join(root_directory, item_name), 'r', encoding='UTF-8') as file2:
                                                                file2_text = file2.read()
                                                            file1.write(file2_text)
                                                        
                                                        with open(os.path.join(root_directory, item_name), 'w', encoding='UTF-8') as file3:
                                                            file3.write(new_text)

                                                save_btn = tk.Button(file_read_root, text="保存", command=save_file)
                                                save_btn.pack()

                                                file_read_area = scrolledtext.ScrolledText(file_read_root, state='disabled', height=20)
                                                file_read_area.pack(fill=tk.BOTH, expand=True)   

                                                file_read_area.configure(state='normal', bg='lightblue')
                                                file_read_area.insert(tk.END, file_text)

                                                file_read_root.bind("<Control-S>", save_file)
                                                file_read_root.bind("<Control-s>", save_file)

                                                roots.add(file_read_root, text=f"文件编辑器（{item_name}）")
                                            elif language == 'en-us':
                                                text_lbl = tk.Label(file_read_root, text=f"File editor({item_name})")
                                                text_lbl.pack()

                                                file_read_area = scrolledtext.ScrolledText(file_read_root, state='disabled', height=20)
                                                file_read_area.pack(fill=tk.BOTH, expand=True)   

                                                file_read_area.configure(state='normal')
                                                file_read_area.insert(tk.END, file_text)
                                                #file_read_area.configure(state='disabled')

                                                roots.add(file_read_root, text=f"File editor({item_name})")
                                    else:
                                        if language == 'zh-cn':
                                            messagebox.showerror('错误', '文件不存在')
                                        elif language == 'en-us':
                                            messagebox.showerror('Error', 'File does not exist')
                                self.output_area.insert(tk.END, "The file has been opened\n")
                                
                        pass
                    elif command == "":
                        self.output_area.insert(tk.END, "\n")
                    else:
                        '''
                        temp = False
                        temps = False
                        try:
                            self.output_area.insert(tk.END, eval(command) + '\nPython expressions have been calculated\n' )
                        except:
                            try:
                                exec(command)
                            except Exception as e:
                                print(e)
                                self.output_area.insert(tk.END, f'command ({command}) isn\'t a coammandA' + "\n")
                                temp = True
                                temps = False
                            temps = True
                        try:
                            if temps == True:
                                self.output_area.insert(tk.END, "The python code has been runB\n")
                                return
                            exec(command)
                            self.output_area.insert(tk.END, "The python code has been runC\n")
                        except:
                            if temp == True:
                                self.output_area.config(state='disabled')
                                return
                            self.output_area.insert(tk.END, f'command ({command}) isn\'t a coammand' + "\n")
                            self.output_area.config(state='disabled')
                            return
                        '''
                        self.output_area.insert(tk.END, f' > command ({command}) isn\'t a coammand' + "\n")
                else:
                    func(*func_arg, **func_kwargs) # type: ignore
                self.output_area.config(state='disabled')

            def __eq__(self, other):
                try:
                    temp = other.Terminal
                    return True
                except:
                    return False
                
            def __str__(self):
                return self.Terminal

        return Terminal

    #Terminal = get_terminal()

    def get_command():
        class Item_(TypedDict):
            object: object
            sep: str
            end: str | None
            callback_func: Callable[[str], None] | None

        class Item(TypedDict):
            type: Literal['print', 'input']
            object: Item_

        class command():
            def __init__(self, root: tk.Tk, roots: CustomNotebook): # type: ignore
                self.command = f"<class \'command\'> <command object at {hex(id(self))}> - Author: XR"
                self.root = tk.Frame(root)
                self.roots = roots
                self.root_ = root
                self.is_input = False

                # 创建一个滚动文本框用于显示输出
                self.output_area = scrolledtext.ScrolledText(self.root, state='disabled', height=20)
                self.output_area.pack(fill=tk.BOTH, expand=True)              

                self.output_area.config(bg='black', fg='white')
                self.output_area.configure(state='normal')
                self.output_area.insert(tk.END, " >>> \n\n")
                self.output_area.configure(state='disabled')

                self.input_entry = tk.Entry(self.root)
                self.input_entry.pack(fill=tk.X)

                self.input_entry.config(bg='black', fg='white', insertbackground='white')
                self.input_entry.config(state='disabled')

                self.code_list: List[Item] = []

                self.roots.add(self.root, text="command")

            def print(self, *values: object, sep: str | None = " ", end: str | None = "\n"):
                if sep is None:
                    sep = ' '
                if end is None:
                    end = '\n'
                if self.is_input:
                    self.code_list.append({'type' : 'print', 'object' : {'object' : values, 'sep' : sep, 'end' : end, 'callback_func' : None}})
                    return
                all_text: str = ''
                for text in values:
                    all_text += str(text) + sep
                all_text += end

                self.output_area.config(state='normal')
                self.output_area.insert(tk.END, f" >>> {all_text}\n")
                self.output_area.config(state='disabled')
                
            def input(self, callback_func: Callable[[str], None] | None, *values: object, sep: str = " "):
                """
                Displays the input prompt and binds the Enter key to capture user input.
                Once input is captured, it calls the provided callback with the input.
                
                :param callback_func: A function to be called with the user's input as an argument.
                """
                if sep is None:
                    sep = ' '
                if self.is_input:
                    self.code_list.append({'type' : 'input', 'object' : {'object' : values, 'sep' : sep, 'end' : None, 'callback_func' : callback_func}})
                    return
                
                all_text: str = ''
                for text in values:
                    all_text += str(text) + sep

                self.output_area.config(state='normal')
                self.output_area.insert(tk.END, f" >>> {all_text} > ")
                self.output_area.config(state='disabled')

                self.input_entry.config(state='normal')

                self.is_input = True

                def handle_input():
                    user_input = self.input_entry.get()
                    
                    # Clear current line and reset for next input

                    # self.output_area.delete("end-2c", tk.END)
                    self.input_entry.delete(0, tk.END)
                    self.output_area.config(state='normal')
                    self.output_area.insert(tk.END, f"{user_input}\n\n")
                    self.output_area.config(state='disabled')
                    self.input_entry.unbind("<Return>")
                    self.input_entry.config(state='disabled')

                    self.is_input = False

                    if callback_func is not None:
                        callback_func(user_input)  # Invoke the callback with user input

                    #breakpoint()

                    while self.code_list != []:
                        item = self.code_list.pop(0)
                        if item['type'] == 'print':
                            self.print(*item['object']['object'], sep=item['object']['sep'], end=item['object']['end'])
                        elif item['type'] == 'input':
                            #self.code_list.clear()
                            self.is_input = False
                            self.input(item['object']['callback_func'], *item['object']['object'], sep=item['object']['sep'])
                            #self.code_list.clear()
                        else:
                            raise ValueError("Invalid command type")

                    # 如果代码队列为空，说明所有命令都已处理完成
                    #if not self.code_list:
                        # 清空代码队列，确保下次调用时从头开始
                        #self.code_list.clear()
                
                # Bind the Return key to trigger input handling
                self.input_entry.bind("<Return>", lambda event: handle_input())

                #self.input_entry.mainloop()

            def __eq__(self, other):
                try:
                    temp = other.command
                    return True
                except:
                    return False
                
            def __str__(self):
                return self.command

        return command

    def get_RUNEXECFILE():
        def _len(__obj : Sized) -> int:
            '''Return the number of items in a container.'''
            return len(__obj) - 1

        

        class Item(TypedDict):
            value_name: str
            value_value: Any
            value_len: int
            value_type: Literal['function'] | \
                        Literal['class'] | \
                        Literal['variable'] | \
                        Literal['module'] | \
                        Literal['package'] | \
                        Literal['method'] | \
                        Literal['number'] | \
                        Literal['boolean'] | \
                        Literal['string'] | \
                        Literal['list'] | \
                        Literal['tuple'] | \
                        Literal['dict'] | \
                        Literal['set']
            value_functionbody: str | None
            value_functionarg: str | None
            value_classbody: str | None
            value_classarg: str | None

        class RUNEXECFILE():
            def __init__(self, root: tk.Tk, roots=None):
                self.RUNEXECFILE = f"<class \'RUNEXECFILE\'> <RUNEXECFILE object at {hex(id(self))}> - Author: XR"
                self.root_ = tk.Frame(root)
                self.roots = roots
                self.root = root

                self.values: list[Item] = []

            #def raise_error(self):
                
            #def 

            def run(self, file_path: str, API: Application_Programming_Interface):
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        code: bytes = f.read()
                        i = -1
                        list_1 = code.split(b'\r\n')
                        if list_1[0] != b'\x23\x58\x52\x00\x00\x00\x45\x58\x45\x43' or \
                           list_1[_len(list_1)] != b'\x11\x11\x11\x45\x4E\x44\x5F\x45\x58\x45\x43':
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

        return RUNEXECFILE

    def get_Document_renderer():
        class Document_renderer():
            def __init__(self):
               self.Document_renderer = f'<class \'Document_renderer\'> <Document_renderer object at {hex(id(self))}> - Author: XR'

            def Document_display(self, file_path: str, root: tk.Tk | tk.Frame, func=None, roots: CustomNotebook | None=None, *func_args, **func_kwargs): # type: ignore
                if file_path.split('.')[-1] == 'docu':
                    if os.path.exists(file_path):
                        with open(file_path, 'r', encoding='UTF-8') as file:
                            content = file.read()
                        
                        ol_li_text = '·'

                        for text in content.split('\n'):
                            if '#' in text and text.startswith('#'):
                                table_ = {2 : 35, 3 : 30, 4 : 25, 5 : 20, 6 : 15}
                                list_ = text.split('#')
                                if len(list_) in table_:
                                    text_lbl = tk.Label(root, text=list_[-1], font=('黑体', table_[len(list_)]))
                                else:
                                    text_lbl = tk.Label(root, text=list_[-1], font=('黑体', 15))

                                text_lbl.pack(anchor=tk.W)
                            elif '!' in text and text.startswith('!'):
                                table_ = {'p' : 15, 'h1' : 35, 'h2' : 30, 'h3' : 25, 'h4' : 20, 'h5' : 15}
                                list_ = text.split('!')
                                if list_[1] in table_:
                                    text_lbl = tk.Label(root, text=list_[-1], font=('黑体', table_[list_[1]]))
                                    text_lbl.pack(anchor=tk.W)
                                else:
                                    i = -1
                                    for text_ in list_:
                                        i += 1
                                        if text_ == 'ol-li':
                                            if list_[i + 1] in table_:
                                                text_lbl = tk.Label(root, text=ol_li_text*i + list_[i + 2], font=('黑体', table_[list_[i + 1]]))
                                            else:
                                                text_lbl = tk.Label(root, text=ol_li_text*i + list_[i + 2], font=('黑体', 15))
                                    text_lbl.pack(anchor=tk.W)
                            elif '$' in text and text.startswith('$'):
                                list_ = text.split('$')
                                list_.remove('')
                                for t_ in list_:
                                    if t_ != '':
                                        list__ = t_.split(' = ')

                                        if list__[0] == 'ol-li':
                                            ol_li_text = list__[1]

                            else:
                                if not func is None:
                                    func(*func_args, **func_kwargs)
                                if not text == '':
                                    text_lbl = tk.Label(root, text=text, font=('黑体', 15))
                                    text_lbl.pack(anchor=tk.W)
                    else:
                        raise File_notexists('文件不存在')
                else:
                    raise File_extension_notcorrect('文件后缀名不正确')

                if not roots is None:
                    roots.add(root, 'Document_renderer')

            def __eq__(self, other):
                try:
                    temp = other.Document_renderer
                    return True
                except:
                    return False
                
            def __str__(self):
                return self.Document_renderer

        return Document_renderer

    command = get_command()

    folder = get_folder()

    config = get_config_and_function()[0]

    language = config['language']

    find_largest_integer = get_find_largest_integer()

    Document_renderer = get_Document_renderer()

    class Application_Programming_Interface:
        """
        API class
        """
        def __init__(self):
            self.Application_Programming_Interface = f"<class \'Application_Programming_Interface\'> <Application_Programming_Interface object at {hex(id(self))}> - Author: XR"
            pass

        def get_CustomNotebook_API(self):
            return CustomNotebook
        
        def get_Document_renderer_API(self):
            return Document_renderer

        def create_and_get_RUNEXECFILE_API(self):
            """
            Returns the RUNEXECFILE class
            """
            return get_RUNEXECFILE()

        def create_windows_auxiliary_functions_API(self):
            """
            Returns the find_largest_integer function
            (The find_largest_integer function is a helper function for creating a window)
            """

            return find_largest_integer

        def config_and_config_function_API(self):
            """
            Returns the config in the form of a tuple along with functions about the config
            (config, config_init, get_config, switch_file_language)
            config: Dictionary about config
            config_init: Initialize the config
            get_config: Get the config
            switch_file_language: Switch the language of the config file
            """
            return get_config_and_function()

        def Recapture_config_API(self):
            """
            Recapture the config
            """
            return get_config_and_function()[0]

        def get_folder_API(self):
            return get_folder()
        
        def create_and_get_Terminal_API(self):
            return get_terminal()

        def get_command_API(self):
            return command

        def get_file_API(self):
            """
            Returns the File_API class

            文件API
            提示：
            此API为测试版，且还有bug（漏洞）
            最好别用（可以的帮我修复一下）
            
            File API
            Prompt:
            This API is in beta and there are bugs
            It's better not to use it (you can fix it for me)

            """

            class File_API:
                """
                文件API
                提示：
                此API为测试版，且还有bug（漏洞）
                最好别用（可以的帮我修复一下）

                File API
                Prompt:
                This API is in beta and there are bugs
                It's better not to use it (you can fix it for me)
                """

                def __init__(self):
                    self.File_API = f"<class \'File_API\'> <File_API object at {hex(id(self))}> - Author: XR"
                    pass

                def file_editor(self,
                              root: tk.Tk,
                              roots: CustomNotebook, # type: ignore
                              file_path,
                              color='lightblue'):
                    
                    if os.path.exists(file_path):
                        root_directory, item_name = os.path.split(file_path)
                        with open(os.path.join(root_directory, item_name), 'r', encoding='UTF-8') as file:
                            file_text = file.read()
                            class MYFrame(tk.Frame):
                                def destroy(self) -> None:
                                    save_file()
                                    return super().destroy()
                            file_read_root = MYFrame(root)
                            if language == 'zh-cn':
                                text_lbl = tk.Label(file_read_root, text=f"文件编辑器（{item_name}）")
                                text_lbl.pack()

                                def save_file(event=None):
                                    with open(os.path.join(root_directory, item_name), 'r', encoding='UTF-8') as file:
                                        file_text = file.read()
                                    new_list = file_read_area.get("1.0", tk.END).split("\n")
                                    new_list.pop(len(new_list)-1)
                                    new_text = '\n'.join(new_list)
                                    
                                    if new_text != file_text:
                                        with open(os.path.join(root_directory, item_name + '.back'), 'w', encoding='UTF-8') as file1:
                                            with open(os.path.join(root_directory, item_name), 'r', encoding='UTF-8') as file2:
                                                file2_text = file2.read()
                                            file1.write(file2_text)
                                        
                                        with open(os.path.join(root_directory, item_name), 'w', encoding='UTF-8') as file3:
                                            file3.write(new_text)

                                save_btn = tk.Button(file_read_root, text="保存", command=save_file)
                                save_btn.pack()

                                file_read_area = scrolledtext.ScrolledText(file_read_root, state='disabled', height=20)
                                file_read_area.pack(fill=tk.BOTH, expand=True)   

                                file_read_area.configure(state='normal', bg=color)
                                file_read_area.insert(tk.END, file_text)

                                file_read_root.bind("<Control-S>", save_file)
                                file_read_root.bind("<Control-s>", save_file)

                                roots.add(file_read_root, text=f"文件编辑器（{item_name}）")
                            elif language == 'en-us':
                                text_lbl = tk.Label(file_read_root, text=f"File editor({item_name})")
                                text_lbl.pack()

                                file_read_area = scrolledtext.ScrolledText(file_read_root, state='disabled', height=20)
                                file_read_area.pack(fill=tk.BOTH, expand=True)   

                                file_read_area.configure(state='normal')
                                file_read_area.insert(tk.END, file_text)
                                #file_read_area.configure(state='disabled')

                                roots.add(file_read_root, text=f"File editor({item_name})")
                    else:
                        if language == 'zh-cn':
                            messagebox.showerror('错误', '文件不存在')
                        elif language == 'en-us':
                            messagebox.showerror('Error', 'File does not exist')
                    
                def fetch_file_folder(self,
                                    screens: tk.Tk | tk.Frame,
                                    root: tk.Tk,
                                    roots: CustomNotebook, # type: ignore
                                    path=os.path.join(folder, './XRdows/file'), # type: ignore
                                    color='lightblue',
                                    root_directory=os.path.join(folder, './XRdows/file'), # type: ignore
                                    is_root_dir=True,
                                    is_file_eq_root=True):

                    file_listbox = Listbox(root)

                    temp = False

                    item_type = None
                    item_name = None

                    for folder_path, subfolders, files in os.walk(path):
                        print(subfolders, files)
                        if root_directory == os.path.join(folder, './XRdows/file') and is_file_eq_root == True:
                            if folder_path == root_directory:
                                for item in subfolders + files:
                                    if is_root_dir:
                                        if os.path.isfile(os.path.join(folder_path, item)):
                                            print(folder_path, item)
                                            if folder_path == os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(os.path.join(folder, './XRdows/file')):
                                                    print(text)
                                                    if text == '':
                                                        temp = False
                                                    else:
                                                        temp = True
                                            elif folder_path != os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(os.path.join(folder, './XRdows/file')):
                                                    print(text)
                                                    if text == '':
                                                        temp = False
                                                    else:
                                                        temp = True

                                            if temp != True:
                                                file_listbox.insert(tk.END, 'file***' + item)
                                        elif os.path.isdir(os.path.join(folder_path, item)):
                                            print(folder_path, item)
                                            if folder_path == os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(os.path.join(folder, './XRdows/file') + '\\'):
                                                    print(text)
                                                    if '\\' in text:
                                                        temp = False
                                                    else:
                                                        temp = False
                                            elif folder_path != os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(os.path.join(folder, './XRdows/file') + '\\'):
                                                    print(text)
                                                    if '\\' in text:
                                                        temp = False
                                                    else:
                                                        temp = False

                                            if temp != True:
                                                file_listbox.insert(tk.END, 'folder*' + item)

                                    else:
                                        if os.path.isfile(os.path.join(folder_path, item)):
                                            print(folder_path, item)
                                            if folder_path == os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(root_directory):
                                                    print(text)
                                                    if text == '':
                                                        temp = False
                                                    else:
                                                        temp = True
                                            elif folder_path != os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(root_directory):
                                                    print(text)
                                                    if text == '':
                                                        temp = False
                                                    else:
                                                        temp = True

                                            if temp != True:
                                                file_listbox.insert(tk.END, 'file***' + item)
                                        elif os.path.isdir(os.path.join(folder_path, item)):
                                            print(folder_path, item)
                                            if folder_path == os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(root_directory + '\\'):
                                                    print(text)
                                                    if '\\' in text:
                                                        temp = False
                                                    else:
                                                        temp = False
                                            elif folder_path != os.path.join(folder, './XRdows/file'):
                                                for text in folder_path.split(root_directory + '\\'):
                                                    print(text)
                                                    if '\\' in text:
                                                        temp = False
                                                    else:
                                                        temp = False

                                            if temp != True:
                                                file_listbox.insert(tk.END, 'folder*' + item)
                                    
                                    print(temp)

                                    temp = False
                        elif is_file_eq_root != True:
                            print('a')
                            for item in subfolders + files:
                                if is_root_dir:
                                    if os.path.isfile(os.path.join(folder_path, item)):
                                        print(folder_path, item)
                                        if folder_path == os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(os.path.join(folder, './XRdows/file')):
                                                print(text)
                                                if text == '':
                                                    temp = False
                                                else:
                                                    temp = True
                                        elif folder_path != os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(os.path.join(folder, './XRdows/file')):
                                                print(text)
                                                if text == '':
                                                    temp = False
                                                else:
                                                    temp = True

                                        if temp != True:
                                            file_listbox.insert(tk.END, 'file***' + item)
                                    elif os.path.isdir(os.path.join(folder_path, item)):
                                        print(folder_path, item)
                                        if folder_path == os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(os.path.join(folder, './XRdows/file') + '\\'):
                                                print(text)
                                                if '\\' in text:
                                                    temp = False
                                                else:
                                                    temp = False
                                        elif folder_path != os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(os.path.join(folder, './XRdows/file') + '\\'):
                                                print(text)
                                                if '\\' in text:
                                                    temp = False
                                                else:
                                                    temp = False

                                        if temp != True:
                                            file_listbox.insert(tk.END, 'folder*' + item)

                                else:
                                    if os.path.isfile(os.path.join(folder_path, item)):
                                        print(folder_path, item)
                                        if folder_path == os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(root_directory):
                                                print(text)
                                                if text == '':
                                                    temp = False
                                                else:
                                                    temp = True
                                        elif folder_path != os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(root_directory):
                                                print(text)
                                                if text == '':
                                                    temp = False
                                                else:
                                                    temp = True

                                        if temp != True:
                                            file_listbox.insert(tk.END, 'file***' + item)
                                    elif os.path.isdir(os.path.join(folder_path, item)):
                                        print(folder_path, item)
                                        if folder_path == os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(root_directory + '\\'):
                                                print(text)
                                                if '\\' in text:
                                                    temp = False
                                                else:
                                                    temp = False
                                        elif folder_path != os.path.join(folder, './XRdows/file'):
                                            for text in folder_path.split(root_directory + '\\'):
                                                print(text)
                                                if '\\' in text:
                                                    temp = False
                                                else:
                                                    temp = False

                                        if temp != True:
                                            file_listbox.insert(tk.END, 'folder*' + item)
                                
                                print(temp)

                                temp = False
                    # '''
                    dicts_: dict[str, tk.Button] = {}

                    for index in range(file_listbox.size()):
                        item = file_listbox.get(index)

                        items = item.split('*')

                        item_type = None
                        item_name = None

                        for texts in items:
                            print(texts, items)
                            if texts == 'file':
                                item_type = 'file'
                            elif texts == 'folder':
                                item_type = 'folder'
                            elif texts != '':
                                item_name = texts

                        if item_type and item_name:
                            # 获取图片，这里假设所有文件和文件夹都有对应的图片
                            images_path = os.path.join(folder, f'./XRdows/image/{item_type}.png')  # 请确保图片路径正确

                            if os.path.exists(images_path):
                                images__ = Image.open(images_path)
                                if item_type == 'file':
                                    images_ = images__.resize((35, 44), Image.LANCZOS)
                                elif item_type == 'folder':
                                    images_ = images__.resize((29, 42), Image.LANCZOS)
                                forf_image = ImageTk.PhotoImage(images_)

                                fae = tk.Frame(screens, bg=color)
                                fae.pack()

                                # 使用字典存储Button，键是文件名，值是Button对象
                                button_id = f"{item_type}*{index}*{item_name}*{root_directory}"  # 使用item_type和index作为唯一标识
                                dicts_[button_id] = tk.Button(fae, image=forf_image)
                                dicts_[button_id].image = forf_image  # type: ignore
                                dicts_[button_id].pack(side=tk.LEFT, pady=10)
                                if item_type == 'file':
                                    dicts_[button_id].config(command=lambda button_id=button_id: self.handle_click('file',
                                                                                                                button_id,
                                                                                                                root,
                                                                                                                roots), width=35, height=44)
                                if item_type == 'folder':
                                    dicts_[button_id].config(command=lambda button_id=button_id: self.handle_click('folder',
                                                                                                                button_id,
                                                                                                                root,
                                                                                                                roots), width=29, height=42)
                                label = tk.Label(fae, text=item_name, font=("黑体", 12), bg=color)
                                label.pack(side=tk.LEFT, pady=0)
                                test_label_1 = tk.Label(fae, text=root_directory, font=("黑体", 12), bg=color)
                                test_label_1.pack(side=tk.LEFT, pady=0)

                def handle_click(self,
                                type,
                                button_id: str,
                                root: tk.Tk,
                                roots: CustomNotebook): # type: ignore
                    print(button_id)
                    item_name = button_id.split('*')[2] # 从button_id中提取文件或文件夹的名称
                    root_directory = button_id.split('*')[3]

                    if type == 'file':
                        self.file_editor(root, roots, os.path.join(root_directory, item_name))

                    elif type == 'folder':
                        '''
                        if language == 'zh-cn':
                            messagebox.showinfo(title="信息", message="未实现文件夹阅读器")
                        elif language == 'en-us':
                            messagebox.showinfo(title="Information", message="The folder reader is not implemented")
                        '''
                        
                        # print(os.path.join(folder, f'./XRdows/file/{item_name}'), os.listdir(os.path.join(folder, f'./XRdows/file/{item_name}')))
                        folder_read_root = tk.Frame(root)
                        if language == 'zh-cn':
                            # breakpoint()
                            text_lbl = tk.Label(folder_read_root, text=f"文件夹阅读器（{item_name}）")
                            text_lbl.pack()

                            if os.path.exists(os.path.join(root_directory, item_name)):
                                print(root_directory, item_name, 'a')
                                self.fetch_file_folder(folder_read_root,
                                                    root,
                                                    roots,
                                                    os.path.join(root_directory, item_name),
                                                    'white',
                                                    root_directory,
                                                    False,
                                                    False)
                            else:
                                
                                def temp__():
                                    # breakpoint()
                                    for file_folder in os.listdir(os.path.join(folder, './XRdows/file')):
                                        print(file_folder, 'b')
                                        if os.path.isdir(os.path.join(folder, './XRdows/file', file_folder)):
                                            if os.path.exists(os.path.join(folder, './XRdows/file', file_folder, item_name)):
                                                return (os.path.join(folder, './XRdows/file', file_folder, item_name),
                                                        os.path.join(folder, './XRdows/file', file_folder))
                                            else:
                                                continue

                                temp_ = temp__()
                                path: str = temp_[0] # type: ignore
                                root_directory: str = temp_[1] # type: ignore
                                print(path, root_directory, 'c')
                                self.fetch_file_folder(folder_read_root,
                                                    root,
                                                    roots,
                                                    path,
                                                    'white',
                                                    root_directory,
                                                    False,
                                                    False)

                            roots.add(folder_read_root, text=f"文件夹阅读器（{item_name}）")
                        elif language == 'en-us':
                            text_lbl = tk.Label(folder_read_root, text=f"Folder reader（{item_name}）")
                            text_lbl.pack()

                            self.fetch_file_folder(folder_read_root,
                                                root,
                                                roots,
                                                os.path.join(item_name),
                                                'white',
                                                root_directory)

                            roots.add(folder_read_root, text=f"File reader（{item_name}）")
                            
                        # raise Not_Implemented('The folder reader is not implemented')
                    
                    self.i = [roots.tab(i)['padding'][0] + i for i in range(roots.index(tk.END))]

                    roots.select(find_largest_integer(self.i))

                def __eq__(self, other):
                    try:
                        temp = other.File_API
                        return True
                    except:
                        return False
                
                def __str__(self):
                    return self.File_API


            return File_API

        def __eq__(self, other):
            try:
                temp = other.Application_Programming_Interface
                return True
            except:
                return False
        
        def __str__(self):
            return self.Application_Programming_Interface

    return Application_Programming_Interface
