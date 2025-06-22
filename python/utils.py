import subprocess
import asyncio
import config
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPT_FOLDER = os.path.join(BASE_DIR, "../scripts/")

def restart_bot():
    subprocess.call(["sh", f"{SCRIPT_FOLDER}restartbot.sh"])

def restart_site():
    subprocess.call(["sh", f"{SCRIPT_FOLDER}restartsite.sh"])

def reboot_server():
    subprocess.call(["sh", f"{SCRIPT_FOLDER}reboot.sh"])

def shutdown_server():
    subprocess.call(["sh", f"{SCRIPT_FOLDER}poweroff.sh"])

def wakeonlan():
    subprocess.call(["sh", f"{SCRIPT_FOLDER}wakeonlan.sh"])
        
def get_local_ip():
    address = subprocess.run(["sh", f"{SCRIPT_FOLDER}get_local_ip.sh"], capture_output=True, text=True).stdout
    return address

def get_global_ip():
    address = subprocess.run(["sh", f"{SCRIPT_FOLDER}get_global_ip.sh"], capture_output=True, text=True).stdout
    return address
