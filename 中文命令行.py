import time
import os
import random

time.sleep(0.1)
print("中文命令行 [版本 1.2.0]")
print("(c) 编程猫怪盗 个人保留所有权利。")
print("输入 帮助 获取帮助\n")
os.system("title 中文命令行")

"""实用工具类"""
def 计算器():
    os.system("calc")
    print("计算器已启动")
def 记事本():
    os.system("start notepad")
    print("记事本已启动")
def 清理系统缓存():
    a = input("请您先关闭除了此程序外的所有程序，输入确定\n如果想取消，直接按回车> ")
    if a == "确定":    
        os.system("rd /s /q %temp%")
        os.system("md %temp%")
        os.system("cls")
        print("已清理")
def 文件资源管理器():
    os.system("start explorer")
    print("已打开文件资源管理器")

"""整活类"""
def 骰子():
    print(f"🎲 {random.randint(1,6)}")
def 装黑客():
    os.system("cls")
    os.system("color 0A")
    os.system("dir D:\ /s /b")
    input("完成！按回车继续")
    os.system("cls")
    os.system("color 07")

"""关于此项目"""
def 清屏():
    os.system("cls")
def 在github上查看此项目():
    try:
        os.system("start microsoft-edge:https://github.com/bcmgd/Chinese-CLI")
    except:
        os.system("start https://github.com/bcmgd/Chinese-CLI")
        print("您的电脑可能没有edge，已为您用默认浏览器打开")
def 版本日志():
    print("─────────────────────────")
    print("v1.0.0 加入骰子、版本日志、装黑客，第一个正式版本")
    print("v1.1.0 加入在github上查看此项目、文件资源管理器、清理系统缓存")
    print("v1.2.0 对代码进行函数重构，优化帮助界面")
    print("─────────────────────────")
    print("\n")
def 当前版本():
    print("─────────────────────────")
    print("当前版本：v1.2.0")
    print("作    者：编程猫怪盗")
    print("项目性质：个人自用原创")
    print("─────────────────────────")
    print("\n")
def 退出():
    os._exit(0)    
while True:
    cmd = input("中文命令行> ")
    if cmd == "帮助":
        print("─────────────────────────")
        print("可用命令：")
        print("-实用工具类")
        print("  计算器")
        print("  记事本")
        print("  清理系统缓存")
        print("  文件资源管理器")
        print("-整活类")
        print("  骰子")
        print("  装黑客")
        print("-关于此项目")
        print("  清屏")
        print("  在github上查看此项目")
        print("  版本日志")
        print("  当前版本")
        print("  退出")
        print("─────────────────────────")
        print("\n")
    elif cmd == "":
        pass
    elif cmd == "计算器":
        计算器()
    elif cmd == "清屏":
        清屏()
    elif cmd == "记事本":
        记事本()
    elif cmd == "骰子":
        骰子()
    elif cmd == "装黑客":
        装黑客()
    elif cmd == "在github上查看此项目":
        在github上查看此项目()
    elif cmd == "文件资源管理器":
       文件资源管理器()
    elif cmd == "清理系统缓存":
        清理系统缓存()
    elif cmd == "版本日志":
        版本日志()
    elif cmd == "当前版本":
        当前版本()
    elif cmd == "退出":
        退出()
    else:
        print(f'本程序无法理解“{cmd}”')
        a = input("您想使用原生终端执行您的命令吗?(想的话回车，不想就输入任意文本)> ")
        if a == "":
            os.system(cmd)
            
