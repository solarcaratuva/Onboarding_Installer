import subprocess
import json
import os
import sys

def download_file(url: str, save_path: str) -> bool:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False
    except Exception:
        return False

def run_cmd(cmd: str) -> bool:
    try:
        process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.returncode == 0
    except Exception:
        return False
    
def import_requests() -> None:
    if not run_cmd("pip install requests"):
        print("FATAL ERROR: Failed to install \'requests\' module")
        exit(1)
    

# MAIN
if len(sys.argv) != 2:
    print("1 command line argument is expected. See the Readme for more information")
    exit(1)
input = sys.argv[1]

import_requests()
import requests

user_path = os.path.expanduser("~")

with open("windows.json", "r") as file:
    instructions = json.load(file)

for instruction in instructions:
    iterations = instruction["iterations"] if "iterations" in instruction else ["1 iteration only"]
    for iter in iterations:
        print(instruction["text"].replace("%ITER%", iter).replace("%IN%", input)+":")

        if "path" in instruction and os.path.exists(instruction["path"].replace("~", user_path)):
            print("\tRequirement already fulfilled, \033[33mskipping\033[0m")
            continue

        if "skip_cmd" in instruction and run_cmd(instruction["skip_cmd"].replace("%ITER%", iter).replace("%IN%", input)):
            print("\tRequirement already fulfilled, \033[33mskipping\033[0m")
            continue

        if "download_URL" in instruction:
            url = instruction["download_URL"][0]
            save_path = instruction["download_URL"][1]
            result = download_file(url, save_path)
            if result:
                print("\tDownloaded \033[32msuccessfully\033[0m")
            else:
                print("\tDownload \033[31mfailed\033[0m")
                continue

        cmd = instruction["cmd"].replace("%ITER%", iter).replace("%IN%", input).replace("~", user_path)
        result = run_cmd(cmd)
        if result:
            print("\tCommand executed \033[32msuccessfully\033[0m")
        else:
            print("\tCommand execution \033[31mfailed\033[0m")
            continue

print("DONE!")
    