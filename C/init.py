import os
from C.API import get_API

API = get_API()()

config_and_function_tuple = API.config_and_config_function_API()

config = config_and_function_tuple[0]

config_init = config_and_function_tuple[1]
get_config = config_and_function_tuple[2]
switch_file_language = config_and_function_tuple[3]

folder = API.get_folder_API()

def __inits__() -> None:
    if not os.path.exists(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}")): # type: ignore
        os.makedirs(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}")) # type: ignore
    if not os.path.exists(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}/desktop")): # type: ignore
        os.makedirs(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}/desktop")) # type: ignore
    if not os.path.exists(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}/download")): # type: ignore
        os.makedirs(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}/download")) # type: ignore
    '''
    if not os.path.exists(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}/")): # type: ignore
        os.makedirs(os.path.join(folder, f"./XRdows/file/{config['user_data_user_1']['name']}/")) # type: ignore
'''
__inits__()
