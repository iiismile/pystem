#!/usr/bin/env python3
#基于Python3构件
#Copyright (C) 2019 Jiatong
#版权所有 (C) 二〇一九 Jiatong
#主程序（启动器）
import hashlib
import math
#import alien_invasion
import sys
import time
import os
###############
import calculator
import md5
###############
os= os.name
###############
def main(): #主页
    print("\n \n 应用：\n1.外星人入侵\n2.计算器\n3.MD5加密\n[输入 256 关闭]")
    n = input(">")
    if n=='1':
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
        #alien_invasion.run_game()
        print("暂不可用，先留个位子先")
        return main()
    if n=='2':
        calculator.ca()
        return main()
    if n=='3':
        md5.md5()
        return main()
    if n=='root':
        print("你以为这是Linux吗？")
        return main()
    if n=='256': #lower 可以将所有字符串作为小写，从而达到不区分大小写。
        return exit()
    if n=='鸡你太美':
        print("鸡你实在是太美。")
        return main()
    else:
        print('[无法识别指令，请检查"',n,'"这个指令是否存在，或者检查您是否对这个指令拥有使用权。]')
        return main()

def main_posix(): #Linux主页
    print("\n \n 应用：\n\n1.计算器\n2.MD5加密\n[输入 256 关闭]")
    n = input(">")
    if n=='1':
        calculator.ca()
        return main_posix()
    if n=='2':
        md5.md5()
        return main_posix()
    if n=='256': #lower 可以将所有字符串作为小写，从而达到不区分大小写。
        return exit()
    else:
        print('[无法识别指令，请检查"',n,'"这个指令是否存在，或者检查您是否对这个指令拥有使用权。]')
        return main_posix()
def exit():
    print("EXIT")
    input('iSmile Python System 以停止服务，按下回车键关闭。\n>')
    sys.exit()

def start(): #启动时
    print ("Hello,world!")
    print ("iSmile Python System")
    pi = math.pi
    print ('pi',pi)
    if os == 'nt':
        print('Windows')
        time.sleep(0.5)
        main()
    if os == 'posix':
        print('Linux or OS X')
        time.sleep(0.5)
        main_posix()
    else:
        print('什么鬼系统')
        input('iSmile Python System 以停止服务，按下回车键关闭。\n>')

start() #启动
