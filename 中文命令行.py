import time
import os
import random

time.sleep(0.1)
print("中文命令行 [版本 1.0.0]")
print("(c) 编程猫怪盗 个人保留所有权利。")
print("输入 帮助 获取帮助\n")
os.system("title 中文命令行")
while True:
    cmd = input("中文命令行> ")
    if cmd == "帮助":
        print("─────────────────────────")
        print("可用命令：")
        print("  计算器")
        print("  清屏")
        print("  记事本")
        print("  骰子")
        print("  装黑客")
        print("  版本日志")
        print("  当前版本")
        print("  退出")
        print("─────────────────────────")
        print("\n")
    elif cmd == "":
        pass   
    elif cmd == "计算器":
        os.system("calc")
        print("计算器已启动")
    elif cmd == "清屏":
        os.system("cls")
    elif cmd == "记事本":
        os.system("start notepad")
    elif cmd == "骰子":
        print(f"🎲 {random.randint(1,6)}")
    elif cmd == "装黑客":
        os.system("cls")
        os.system("color 0A")
        os.system("dir D:\ /s /b")
        input("完成！按回车继续")
        os.system("cls")
        os.system("color 07")
    elif cmd == "版本日志":
        print("─────────────────────────")
        print("v1.0.0 加入骰子、版本日志、装黑客，第一个正式版本")
        print("─────────────────────────")
        print("\n")    
    elif cmd == "当前版本":
        print("─────────────────────────")
        print("当前版本：v1.0.0")
        print("作    者：编程猫怪盗")
        print("项目性质：个人自用原创")
        print("─────────────────────────")
        print("\n")
    elif cmd == "退出":
        os._exit(0)
    else:
        print(f'本程序无法理解“{cmd}”')
        
    
