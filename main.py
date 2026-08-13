import os
import platform
import zipfile
from pathlib import Path

def ModdedClientCheck(targetDirectory):
    isModded: bool
    targetPath = Path(f"{targetDirectory}app")
    targetFile = Path(f"{targetDirectory}original.asar")

    if targetPath.exists() and targetFile.exists():
        isModded = True
    else:
        isModded = False

    return isModded

def WinTidalVersion():
    tidalVersion: str
    winUser: str = os.getlogin()

    winTidalDir: str = f"C:/Users/{winUser}/AppData/Local/TIDAL/"
    tidalVersionList: list[str] = []

    for directory in os.scandir(winTidalDir):
        if directory.is_dir():
            if directory.name.startswith("app-"):
                appDirectory: str = directory.name 
                index = appDirectory.find("app-")
                if index != -1:
                    index = appDirectory[:index] + appDirectory[index + len("app-"):]
                    tidalVersionList.append(index)

    # Assuming found directories are in order pick the last one in list
    tidalVersion = tidalVersionList[-1]
    return winUser, tidalVersion

def ChooseOS():
    operatingSystem = platform.system()
    targetDirectory: str = ""
    macOSFolder: str = "/Applications/TIDAL.app/Contents/Resources/"
    linuxFolder: str = "/opt/tidal-hifi/resources/"

    match operatingSystem:
        case "Linux":
            targetDirectory = linuxFolder 
        case "Windows":
            winUser, tidalVersion = WinTidalVersion()
            windowsFolder: str = f"C:/Users/{winUser}/AppData/Local/TIDAL/app-{tidalVersion}/resources/"
            targetDirectory = windowsFolder
        case "Darwin":
            targetDirectory = macOSFolder

    if ModdedClientCheck(targetDirectory) == True:
        print("Client is already modded!")
    ModdedClientCheck(targetDirectory)
    DownloadLuna()
    InstallLuna(targetDirectory)

def DownloadLuna():
    owner: str = "Inrixia"
    repo: str = "TidaLuna"
    release: str = "luna.zip"
    try:
        os.system(f"curl -L -O https://github.com/{owner}/{repo}/releases/latest/download/{release}")
    except Exception as e:
        print(f"{e} error!")
        print("First option failed, trying second option...")
        try:
            os.system(f"curl-LO https://github.com/{owner}/{repo}/releases/latest/download/{release}")
        except Exception as e2:
            print(f"{e2} error!")
            print("Second option failed!")

def InstallLuna(targetDirectory):
    try:
        os.rename(f"{targetDirectory}app.asar", f"{targetDirectory}original.asar")
        print(f"File renamed from app.asar to original.asar successfully!")
    except Exception as e:
        print(f"An error {e} occurred!")
        print(targetDirectory)

    try:
        with zipfile.ZipFile("luna.zip", "r") as LunaZip:
            LunaZip.extractall(f"{targetDirectory}app")
            print(f"File luna.zip successfully extracted!")
    except FileNotFoundError: 
        print("Zip file luna.zip does not exist.")
        print("Github release may not have been downloaded!")
    except Exception as e:
        print(f"Error {e} occurred when extracting luna.zip")

def CodeSignOSX():
    try:
        if platform.system() == "Darwin":
            os.system("codesign --force --deep --sign - /Applications/TIDAL.app")
            print("Code Signed Tidal Client for MacOS!")
    except Exception as e:
        print(f"Error {e} has occurred while attempting to Code Sign Tidal Client!")

ChooseOS()
CodeSignOSX()

