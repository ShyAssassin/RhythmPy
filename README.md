# Mania Bot
A simple bot that plays mania for you
im still working on this btw :p

## Supported Games
- Quaver
  - [x] 4K Mania
  - [ ] 7K Mania
- Osu
  - [x] 4K Mania
  - [ ] 7K Mania
  - [ ] Osu!
  

## Installation
**Mania Bot has been tested to work with python verisons 3.7 or lower.**  
<sup>In theory this project should work on Mac / Linux but i have not tested it yet</sup>

1. <a href="https://github.com/assassinsorrow/Mania-Bot/releases">Download the latest release</a> or Clone the Repo (`git clone https://github.com/assassinsorrow/Mania-Bot.git`)
2. run the `Setup.py` script to install needed dependencies or install manually with (`pip install -r requirements.txt`)
3. Run `Main.py` to start the program (`python Main.py`)

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

i will review the pull request as soon as i can

## Roadmap
- [x] Choosing game / gamemode without user input
- [x] Multi-threading
- [x] Json settings
- [ ] Automatic updates
- [ ] User interface 

## Building from source
if you want to compile this program yourself you can run the `Build.py` script **or**         
you can use pyinstaller                  
***i recommend using a virtual environment for this***
1. Download Pyinstaller `pip install pyinstaller`
2. CD into working directory `cd Mania Bot`
3. Create a Main.spec file `pyi-makespec Main.py`
4. Fill in needed information <a href="https://github.com/assassinsorrow/Mania-Bot/blob/master/Mania%20Bot/Main.spec">click here for example</a> **you will need to define where the ui elements can be found**
5. Once done with the spec file run `pyinstaller --onedir Main.spec Main.py` and wait for it to complete
- After pyinstaller is done there should be two folders `build` and `dist` if they do not appear please install <a href="https://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads">Visual C++ Redistributable</a>
6. Open the exe found in `dist/Main` to run the program 
*if you want to create a installer please use nsis*

## Disclaimer 
*By downloading this program you agree that you and you alone will be held responsible for any banned accounts that may or may not occur. It is completely up to you if you use any of the following* **Tools** or any other **Third-Party Application** *that in any way is breaking the* **EULA** or **TOS** *of the game.*       
<a href="https://github.com/assassinsorrow/Mania-Bot/blob/master/DISCLAIMER.md"><sub><sup>Full Disclaimer</sup></sub></a>

