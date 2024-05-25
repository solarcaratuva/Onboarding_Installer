# Solar Car Onboarding Script

## Description
This program was made by and for the Solar Car Team at UVA as a tool to onboard new members. This program downloads, installs, and configures the necessary software stack to develop, compile, and upload our embedded code to the car. This program can be run multiple times, as any step where the requirement is already met will just be skipped.

## Windows Users
**Prerequisites:**
1. Install Python ([Link](https://www.python.org/downloads/))
2. Install and configure Windows Subsystem for Linux 2 (WSL) ([Guide](https://learn.microsoft.com/en-us/windows/wsl/install))
    - Note that whatever Linux user and distro you set as the default will be what this program uses
3. Download the code as a `.zip` file and unzip it. Alternatively, if you have Git installed then clone it

**Execution:**
To run the program, enter the following commands in a terminal prompt *with administrator privileges*:
`cd path\where\the\script\was\downloaded\to`
`py .\main.py password`
- Replace `password` with your WSL sudo password (not your normal windows password)
- Note that you may need to use `python` or `python3` instead of `py`

If any step *failed*, then you will need to manually complete the step. Debug data is saved to `log.txt`

## Mac Users
**Prerequisites:**
1. Install Python ([Link](https://www.python.org/downloads/))
2. Install Homebrew ([Link](https://brew.sh/))
3. Download the code as a `.zip` file and unzip it. Alternatively, if you have Git installed then clone it

**Execution:**
To run the program, enter the following commands in a terminal prompt:
`cd path/where/the/script/was/downloaded/to`
`sudo python3 ./main.py path`
- Replace `path` with the absolute path to the folder where you want Solar Car code saved; the folder must already exist
- Note that you may need to use `python` or `py` instead of `python3`

If any step *failed*, then you will need to manually complete the step. Debug data is saved to `log.txt`

## Common Issues
- A step involving Docker containers failed -> Docker Desktop must be running for these commands to work.
- All steps involving WSL failed -> WSL was probably not completely setup then.
- Failures can cascade. Often later steps rely on earlier steps working.
