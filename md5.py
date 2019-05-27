#MD5加密应用

import hashlib #模块导入
def md5():
    s = input('请输入要加密的字符串\n>')
    
    m = hashlib.md5(s.encode())
    print(m.hexdigest())