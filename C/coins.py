import os

from C.API import get_API

API = get_API()()

folder = API.get_folder_API()

def encrypt(coins: int):
    with open(os.path.join(folder, './XRdows/coins/coins.coins'), 'w') as f:
        text = str(coins)
        text_ = ''
        for texts in text:
            text_ += bin((ord(texts))) + ' '

        f.write('coins : ' + text_)

def decrypt():
    with open(os.path.join(folder, './XRdows/coins/coins.coins'), 'r') as f:
        coins_list = f.read().split('coins : ')
        for text in coins_list:
            if text != '':
                text_ = ''
                for texts in text.split(' '):
                    if texts == '':
                        continue
                    text_ += chr(int(texts, base=2))
                coins = text_
                return coins
