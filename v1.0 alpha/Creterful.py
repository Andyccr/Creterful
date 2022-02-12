'''
By Andy Chen
V1.0 Alpha
2022.2.12
'''
#python -m http.server 80
#pip install qrcode tkinter Image numpy random copy matplotlib.pyplot  -i https://mirrors.aliyun.com/pypi/simple/

import os
from os import startfile
import tkinter
from qrcode import make
import socket


print('''
  ______                        __                           ______             __ 
 /      \                      |  \                         /      \           |  \ 
|  $$$$$$\  ______    ______  _| $$_     ______    ______  |  $$$$$$\ __    __ | $$
| $$   \$$ /      \  /      \|   $$ \   /      \  /      \ | $$_  \$$|  \  |  \| $$
| $$      |  $$$$$$\|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$\| $$ \    | $$  | $$| $$
| $$   __ | $$   \$$| $$    $$ | $$ __ | $$    $$| $$   \$$| $$$$    | $$  | $$| $$
| $$__/  \| $$      | $$$$$$$$ | $$|  \| $$$$$$$$| $$      | $$      | $$__/ $$| $$
 \$$    $$| $$       \$$     \  \$$  $$ \$$     \| $$      | $$       \$$    $$| $$
  \$$$$$$  \$$        \$$$$$$$   \$$$$   \$$$$$$$ \$$       \$$        \$$$$$$  \$$
                                                                                   
                                                                                   
''')

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

#if __name__ == '__main__':
print(get_host_ip())

fn=r'h.jpg'#二维码储存地址
pff='http://'+get_host_ip()+':80'
print(pff)
img=make(pff)
img.save(fn)
startfile(fn)#直接将图片打开
os.system("python -m http.server 80")

