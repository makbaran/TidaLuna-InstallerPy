import os
import platform
import zipfile

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

<<<<<<< HEAD
match operatingSystem:
    case "Linux":
        osDir: str = linuxFolder 
    case "Windows":
        osDir: str = windowsFolder
    case "Darwin":
        osDir: str = macOSFolder
    
def InstallLuna():
=======
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

    DownloadLuna()
    InstallLuna(targetDirectory)

def DownloadLuna():
    owner: str = "Inrixia"
    repo: str = "TidaLuna"
    release: str = "luna.zip"
>>>>>>> 65d5d0f (FIX: Deleted .git attr, fixed windows functionality and finding directory to download to, and finally added stable way to download github releases.)
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
<<<<<<< HEAD
        with zipfile.ZipFile("luna.zip", "w") as LunaZip:
            LunaZip.extractall(f"{osDir}/app")
            print(f"File {LunaZip} successfully extracted!")
=======
        with zipfile.ZipFile("luna.zip", "r") as LunaZip:
            LunaZip.extractall(f"{targetDirectory}app")
            print(f"File luna.zip successfully extracted!")
    except FileNotFoundError: 
        print("Zip file luna.zip does not exist.")
        print("Github release may not have been downloaded!")
>>>>>>> 65d5d0f (FIX: Deleted .git attr, fixed windows functionality and finding directory to download to, and finally added stable way to download github releases.)
    except Exception as e:
        print(f"Error {e} occurred when extracting luna.zip")

def CodeSignOSX():
    try:
        if platform.system() == "Darwin":
            os.system("codesign --force --deep --sign - /Applications/TIDAL.app")
            print("Code Signed Tidal Client for MacOS!")
    except Exception as e:
        print(f"Error {e} has occurred while attempting to Code Sign Tidal Client!")

<<<<<<< HEAD
check_and_download_updates(
    GitHubRepo(owner, repo)
)

InstallLuna()
CodeSignOSX()
=======
ChooseOS()
CodeSignOSX()

>>>>>>> 65d5d0f (FIX: Deleted .git attr, fixed windows functionality and finding directory to download to, and finally added stable way to download github releases.)
