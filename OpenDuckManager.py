import easygui, subprocess, psutil, os, signal, winshell, getpass

startupPath = fr'C:\Users\{getpass.getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\OpenDuckCore.lnk'

while True:
    openDuckStatus = False

    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == 'OpenDuckCore.exe':
            openDuckStatus = True
    menuMsg = f'OpenDuckManager\n*OpenDuck配置文件:C:\\Users\\{getpass.getuser()}\openduck_config.json\n*OpenDuck状态：{openDuckStatus}'
    menuChoices = ['开启OpenDuck', '关闭OpenDuck', '设置开机自启', '关闭开机自启', '编辑配置文件']
    menu = easygui.choicebox(menuMsg, 'OpenDuckManager', menuChoices)
    if menu == '开启OpenDuck':
        if openDuckStatus is True:
            easygui.msgbox('OpenDuck已在运行。', 'OpenDuckManager')
            continue
        try:
            subprocess.Popen('OpenDuckCore.exe')
            easygui.msgbox('成功启动OpenDuck。', 'OpenDuckManager')
        except FileNotFoundError:
            easygui.msgbox('未找到同目录下的OpenDuckCore.exe。请检查是否有缺失文件！', 'OpenDuckManager')
    elif menu == '关闭OpenDuck':
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'] == 'OpenDuckCore.exe':
                os.kill(proc.info['pid'], signal.SIGTERM)
                easygui.msgbox('成功关闭OpenDuck。', 'OpenDuckManager')
    elif menu == '设置开机自启':
        try:
            winshell.CreateShortcut(startupPath, os.path.abspath('OpenDuckCore.exe'), Description= 'OpenDuck开机自启')
            easygui.msgbox('成功设置开机自启。\n请您务必在防火墙中放行程序OpenDuckCore.exe。', 'OpenDuckManager')
        except Exception as e:
            easygui.msgbox(f'设置开机自启失败。\n原因:{e}', 'OpenDuckManager')
    elif menu == '关闭开机自启':
        try:
            os.remove(startupPath)
            easygui.msgbox('成功关闭开机自启。', 'OpenDuckManager')
        except Exception as e:
            easygui.msgbox(f'关闭开机自启失败。\n原因:{e}', 'OpenDuckManager')
    elif menu == '编辑配置文件':
        os.system(rf'notepad C:\Users\{getpass.getuser()}\openduck_config.json')
    elif menu is None:
        exit()
