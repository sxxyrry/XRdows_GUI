from consts import folder
import os

with open(os.path.join(folder, './py_C_F/all_text/command_table_English.txt'), 'r', encoding='UTF-8') as file:
    command_table = f'{file.read()}'

with open(os.path.join(folder, './py_C_F/all_text/XRdows.txt'), 'r', encoding='UTF-8') as file:
    XRdows = f'{file.read()}'

with open(os.path.join(folder, './py_C_F/all_text/Edition_logs.txt'), 'r', encoding='UTF-8') as file:
    Edition_logs = f'{file.read()}'

if __name__ == '__main__':
    print(f'{command_table}\n{XRdows}\n{Edition_logs}')
