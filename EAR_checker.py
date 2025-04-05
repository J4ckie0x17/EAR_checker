#!/usr/bin/env python3

import requests
import argparse

# ===== Banner =====
print("\033[95m" + r"""
  ______          _____    _____ _    _ ______ _____ _  ________ _____  
 |  ____|   /\   |  __ \  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
 | |__     /  \  | |__) || |    | |__| | |__ | |    | ' /| |__  | |__) |
 |  __|   / /\ \ |  _  / | |    |  __  |  __|| |    |  < |  __| |  _  / 
 | |____ / ____ \| | \ \ | |____| |  | | |___| |____| . \| |____| | \ \ 
 |______/_/    \_\_|  \_\ \_____|_|  |_|______\_____|_|\_\______|_|  \_\
                      ______                                            
                     |______| 
Made by Jackie0x17
Version: 1.0
""" + "\033[0m")

parser = argparse.ArgumentParser(description="EAR Vulnerability Checker")
parser.add_argument("-u", "--url", required=True, help="URL base, ej: http://10.10.10.10")
parser.add_argument("-d", "--directory", required=True, help="Directorio a probar, ej: /admin")
args = parser.parse_args()

URL = args.url
DIRECTORY = args.directory
CODE_STATE = [301, 302, 303, 307, 308]

full_url = URL + DIRECTORY
r = requests.get(full_url, allow_redirects=False, stream=True)

def get_http_version(version_number):
    if version_number == 10:
        return "HTTP/1.0"
    elif version_number == 11:
        return "HTTP/1.1"
    elif version_number == 20:
        return "HTTP/2"
    else:
        return "HTTP/?.?"

def EAR_check(response):
    print(f"[*] Status Code: {response.status_code}")
    for status in CODE_STATE:
        if response.status_code == status and response.text.strip():
            print(f"[*] {status} Redirection with body content detected.")
            print("[*] Treating as 200 OK for EAR check...")

            http_version = get_http_version(response.raw.version)

            original_status_line = f"{http_version} {status} FOUND"
            modified_status_line = f"{http_version} 200 FOUND"

            print(f"\n[!] Vulnerabilidad detectada en: {response.url}")
            print("\n🔁 Usa esto en BurpSuite → Match and Replace:")
            print(f"Match:   {original_status_line}")
            print(f"Replace: {modified_status_line}")

            print("\n✅ EAR vulnerability detected")
            break
    else:
        print("[*] No EAR vulnerability detected.")

EAR_check(r)
