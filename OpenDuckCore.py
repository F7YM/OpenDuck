import http.server, socket, socketserver, os, json, getpass

port = None  # 端口号
command = None  # 命令
prompt = None  # 返回字符串

def loadConfig():
    try:
        with open(f'C:\\Users\\{getpass.getuser()}\openduck_config.json', 'r', encoding='UTF-8') as f:
            f = json.load(f)
            global port, command, prompt
            try:
                port = f['port']
                command = f['command']
                prompt = f['prompt']
            except KeyError:
                print('[Error] 配置错误。请检查openduck_config.json文件或删除openduck_config.json文件。')
                exit(1)
    except FileNotFoundError:
        with open(f'C:\\Users\\{getpass.getuser()}\openduck_config.json', 'w', encoding='UTF-8') as f:
            defaultConfig = {'port':1145, 'command':'Rundll32.exe user32.dll, LockWorkStation', 'prompt':'搞定了。'}
            f.write(str(json.dumps(defaultConfig, indent=4)))
        loadConfig()

loadConfig()

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            os.system(command)
        except Exception as e:
            print(f'[Error] 命令执行失败: {e}')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(prompt.encode('utf-8'))

with socketserver.TCPServer(('', port), RequestHandler) as httpd:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        print(f'[Info] 启动成功。请确保您已在系统防火墙放行端口 {port}。')
        print(f'[Info] 在局域网内访问 http://{s.getsockname()[0]}:{port} 以在本机执行命令 [{command}]。')
        print('[Info] 若想要远程使用OpenDuck（局域网外），请使用内网穿透工具。')
    httpd.serve_forever()