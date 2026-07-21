from semantic_version import SimpleSpec
from github_release_downloader import check_and_download_updates, GitHubRepo
from pathlib import Path
import os
import platform
import zipfile
import subprocess

owner: str = "Inrixia"
repo: str = "TidaLuna"
tidalVersion: str = ""

macOSFolder: str = "/Applications/TIDAL.app/Contents/Resources"
linuxFolder: str = "/opt/tidal-hifi/resources"
windowsFolder: str = f"%localappdata%\\TIDAL\\app-{tidalVersion}\\resources"
osDir: str 

operatingSystem = platform.system()

match operatingSystem:
    case "Linux":
        osDir: str = linuxFolder 
    case "Windows":
        osDir: str = windowsFolder
    case "Darwin":
        osDir: str = macOSFolder
    

def InstallLuna():
    try:
        os.rename(f"{osDir}/app.asar", f"{osDir}/original.asar")
        print(f"File renamed from app.asar to original.asar successfully!")
    except Exception as e:
        print(f"An error {e} occurred!")
        print(osDir)

    try:
        with zipfile.ZipFile("luna.zip", "r") as LunaZip:
            LunaZip.extractall(f"{osDir}/app")
            print(f"File {LunaZip} successfully extracted!")
    except Exception as e:
        print(f"Error {e} occurred when extracting {zipfile}")

def CodeSignOSX():
    try:
        if platform.system() == "Darwin":
            os.system("codesign --force --deep --sign - /Applications/TIDAL.app")
            print("Code Signed Tidal Client for MacOS!")
        else:
            pass
    except Exception as e:
        print(f"Error {e} has occurred while attempting to Code Sign Tidal Client!")


check_and_download_updates(
    GitHubRepo(owner, repo)
)

InstallLuna()
CodeSignOSX()