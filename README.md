# Solar Car Onboarding Script

## Description
This program was made by and for the Solar Car Team at UVA as a tool to onboard new members. This program downloads, installs, and configures the necessary software stack to develop, compile, and upload our embedded code to the car. This program can be run multiple times, as any step where the requirement is already met will just be skipped.

## Windows Users
**Prerequisites:**
1. Install Python ([Link](https://www.python.org/downloads/))
2. Install and configure Windows Subsystem for Linux 2 (WSL) ([Guide](https://learn.microsoft.com/en-us/windows/wsl/install))
    - Note that whatever Linux user and distro you set as the default will be what this program uses

**Execution:**
To run the program, enter the following commands in a terminal prompt *with administrator privileges*
`cd path/where/the/script/was/downloaded/to`
`py ./main.py password`
- replace `password` with your WSL sudo password (not your normal windows password)
- Note that you may need to use `python` or `python3` instead of `py`

If any step *failed*, then you will need to manually complete the step. Debug data is saved to `log.txt`

## Mac Users
Coming eventually...

## Common Issues
- A step involving Docker containers failed -> Docker Desktop must be running for these commands to work.
- All steps involving WSL failed -> WSL was probably not completely setup then.
- Failures can cascade. Often later steps rely on earlier steps working.
