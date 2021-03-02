# RhythmPy
<p align="center">
<img alt="GitHub" src="https://img.shields.io/github/license/assassinsorrow/RhythmPy?style=flat">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/assassinsorrow/RhythmPy/actions?query=workflow%3ABuild"><img src="https://github.com/assassinsorrow/RhythmPy/workflows/Build/badge.svg"></a>
<a href="https://github.com/assassinsorrow/RhythmPy/actions?query=workflow%3ALinting"><img src="https://github.com/assassinsorrow/RhythmPy/workflows/Lint/badge.svg"></a>
</p>
A not so simple bot that plays rhythm games for you
im still working on this btw :p       
<a href="https://trello.com/b/IkrtUXl8/rhythmpy">Click here for the roadmap and planned features</a>

## Supported Games
- Quaver
  - [x] 4K Mania
  - [ ] 7K Mania
- Osu
  - [x] 4K Mania
  - [ ] 7K Mania
  - [ ] Osu!
  

## Installation
**RhythmPy has been tested to work with python versions 3.7 or lower.**  
<sup>In theory this project should work on Mac / Linux but i have not tested it yet</sup>       

**Method 1: Using the official release installers**           
* <a href="https://github.com/assassinsorrow/RhythmPy/releases">Download the latest release</a> it is faster and includes a installer for RhythmPy with an optional standalone executable                         
                           
**Method 2: Using python**        
1. Clone the Repo `git clone https://github.com/assassinsorrow/RhythmPy.git`
2. CD into the project folder `cd RhythmPy` <sup>The folder that has README.md in it</sup>
3. Install <a href="https://github.com/python-poetry/poetry">Poetry</a>      
  Windows Powershell: `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -`      
  Linux/Mac: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`     
  <a href="https://python-poetry.org/docs/"><sup>Poetry's documentation<sup></sup></sup></a>
4. Create a virtual environment for RhythmPy with <a href="https://github.com/python-poetry/poetry">Poetry</a> `poetry install --no-dev`
5. CD into working directory `cd RhythmPy` <sup>The folder that has the scripts</sup>
6. Start RhythmPy `poetry run python __main__.py`

**Method 3: The Development Builds**       
*the Development builds will contain bugs and features that may not work, it is for testing and may not be a stable.*     
*it contains two seperate builds that do not include system installers and are not compressed (hence the large file size)*             
***You have been warned!***        
* You can get a development build by downloading the file listed under `Artifacts` <a href="https://github.com/assassinsorrow/RhythmPy/actions?query=workflow%3ABuild">Here</a>    (pick the topmost successful build).        
* You must be logged into GitHub to download a development build.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch `git checkout -b feature/AmazingFeature`
3. Commit your Changes `git commit -m 'Add some AmazingFeature'`
4. Push to the Branch `git push origin feature/AmazingFeature`
5. Open a Pull Request

i will review the pull request as soon as i can

## Building from source

1. [Follow installation guide to step 3](#installation)
2. install Dev version of RhythmPy `poetry install`    

 **Method 1 Using premade script:**         
 * 3᎐ Run `poetry run python Build.py` and follow in terminal instructions   
  
**Method 2: Using pyinstaller**    
 * 3.1 ***OPTIONAL*** Create your own .spec file `poetry run pyi-makespec RhythmPy/__main__.py` and Fill in needed information    <a         href="https://github.com/assassinsorrow/RhythmPy/blob/master/RhythmPy/RhythmPy.spec">click here for example</a>.  
 * 3.2 Run `poetry run pyinstaller --onedir RhythmPy/RhythmPy.spec RhythmPy/__main__.py` to create the .exe  
 you will need to define where the ui elements can be found
     
4. Open the executable found in `dist/RhythmPy` to run the program         

**After building is done there should be two folders `build` and `dist` if they do not appear or if the generated executable does not work please install <a href="https://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads">Visual C++ Redistributable</a>      
if that does not work recompile with `--debug=all` as an option and then check the logs in `build/Main`**                  
**if you want to create a installer use nsis, i am not going to cover how to do it here due to it being rather simple**

## Disclaimer 
*By downloading this program you agree that you and you alone will be held responsible for any banned accounts that may or may not occur. It is completely up to you if you use any of the following* **Tools** or any other **Third-Party Application** *that in any way is breaking the* **EULA** or **TOS** *of the game.*       
<a href="https://github.com/assassinsorrow/RhythmPy/blob/master/DISCLAIMER.md"><sub><sup>Full Disclaimer</sup></sub></a>

