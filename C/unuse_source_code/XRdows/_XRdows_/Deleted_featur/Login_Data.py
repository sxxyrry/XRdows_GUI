from consts import folder
import os

runnings = True

def L_D():
    if not os.path.exists(os.path.join(folder, './py_C_F/Login_Data/Login_Data.py')):
        with open(os.path.join(folder, './py_C_F/Login_Data/Login_Data.py'), 'w', encoding='UTF-8') as file:
            file.write("""Login_Data = False\nuser_name = ''""")
        L_D()
        return
    else:
        from py_C_F.Login_Data.Login_Data import Login_Data, user_name

        if Login_Data == False:
            print(' > Not logged in!')
            User_name = input(' > User name :')
            print(f' > Hi {User_name}')
            with open(os.path.join(folder, './py_C_F/Login_Data/Login_Data.py'), 'w', encoding='UTF-8') as file:
                file.write(f"""Login_Data = True\nuser_name = '{User_name}'""")
            return
        elif Login_Data == True:
            print(' > Logged in!')
            print(f' > Hi {user_name}')

if __name__ == '__main__':
    L_D()
