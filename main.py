import subprocess
import json
import os
import sys
import atexit
import platform

log = open("log.txt", "w")
atexit.register(lambda: log.close)

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
    log.write(f"COMMAND: \n{cmd}\nOUTPUT:\n")
    try:
        process = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        log.write(process.stdout)
        log.write(process.stderr)
        log.write(f"EXIT CODE: {process.returncode}\n")
        return process.returncode == 0
    except Exception as e:
        log.write(f"ERROR: {e}\n")
        return False
    
def import_requests() -> None:
    cmdlets = ["", "py -m", "python3 -m", "python -m"]
    for cmdlet in cmdlets:
        if run_cmd(f"{cmdlet} pip install requests"):
            return
    print("FATAL ERROR: Failed to install \'requests\' module")
    exit(1)

def pause(text: str) -> None:
    print(f"{text} \nEnter \"continue\" to continue")
    while input().strip().lower() != "continue":
        print("Enter \"continue\" to continue")
    

# MAIN
if len(sys.argv) != 2:
    print("1 command line argument is expected. See the Readme for more information")
    exit(1)
inp = sys.argv[1]

import_requests()
import requests

user_path = os.path.expanduser("~")

match platform.system():
    case "Windows":
        config = "windows.json"
    case "Darwin":
        config = "mac.json"
    case _:
        print("Unsupported OS: Only Windows and MacOS are supported")
        exit(1)
with open(config, "r") as file:
    instructions = json.load(file)

for instruction in instructions:
    iterations = instruction["iterations"] if "iterations" in instruction else ["1 iteration only"]
    for iter in iterations:
        text = instruction["text"].replace("%ITER%", iter).replace("%IN%", inp)+":"
        print(text)
        log.write(f"\n\n{text}\n")

        if "path" in instruction and os.path.exists(instruction["path"].replace("~~~", user_path)):
            print("\tRequirement already fulfilled, \033[33mskipping\033[0m")
            continue

        if "skip_cmd" in instruction and run_cmd(instruction["skip_cmd"].replace("%ITER%", iter).replace("%IN%", inp)):
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

        cmd = instruction["cmd"].replace("%ITER%", iter).replace("%IN%", inp).replace("~~~", user_path)
        result = run_cmd(cmd)
        if result:
            print("\tCommand executed \033[32msuccessfully\033[0m")
        else:
            print("\tCommand execution \033[31mfailed\033[0m")
            continue

        if "pause" in instruction:
            pause(instruction["pause"])

print("DONE! Check \"log.txt\" for debug information")
    