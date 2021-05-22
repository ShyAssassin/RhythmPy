.DEFAULT_GOAL := default
Pyinstaller = poetry run pyinstaller --onedir --noconfirm
# windows
ifdef OS
	ifeq ($(shell uname -o), Msys) #MINGW on windows
		RM = rm -rf
		CP = cp
		mkdir = mkdir -p
		run = ./RhythmPyDev
		CopyDevBuild = cp "RhythmPy/Updater/Build/Updater.exe" "dist/RhythmPyDev"
		CopyBuild = cp "RhythmPy/Updater/Build/Updater.exe" "dist/RhythmPy"
	else #Normal windows
		RM = rmdir /S /Q
		CP = copy
		mkdir = mkdir 
		run = RhythmPyDev.exe
		CopyDevBuild = copy RhythmPy\Updater\Build\Updater.exe dist/RhythmPyDev
		CopyBuild = copy RhythmPy\Updater\Build\Updater.exe dist\RhythmPy
	endif
else #Linux
	ifeq ($(shell uname), Linux)
		RM = rm -rf
		CP = cp
		mkdir = mkdir -p
		run = ./RhythmPyDev
		CopyDevBuild = cp "RhythmPy/Updater/Build/Updater.exe" "dist/RhythmPyDev"
		CopyBuild = cp "RhythmPy/Updater/Build/Updater.exe" "dist/RhythmPy"
	endif
endif


default:
	$(Pyinstaller) RhythmPy/RhythmPy.spec RhythmPy/__main__.py
	cmake -B RhythmPy/Updater/Build -S RhythmPy/Updater -G "Unix Makefiles"
	cmake --build RhythmPy/Updater/Build
	$(CopyBuild)
dev:
	$(Pyinstaller) RhythmPy/RhythmPyDev.spec RhythmPy/__main__.py
	cmake -B RhythmPy/Updater/Build -S RhythmPy/Updater -G "Unix Makefiles"
	cmake --build RhythmPy/Updater/Build
	$(CopyDevBuild)
python:
	cd RhythmPy && poetry run python __main__.py
run:
	make dev
	cd dist/RhythmPyDev && $(run)
Updater:
	$(mkdir) "RhythmPy/Updater/Build"
	cmake -B RhythmPy/Updater/Build -S RhythmPy/Updater -G "Unix Makefiles"
	cmake --build RhythmPy/Updater/Build
RhythmPyDev:
	$(Pyinstaller) RhythmPy/RhythmPyDev.spec RhythmPy/__main__.py
clean:
	$(RM) "build/"
	$(RM) "dist/"