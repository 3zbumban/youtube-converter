from os import getcwd, system
from pathlib import Path
import subprocess


YOUTUBE_DL = Path(getcwd() + "\\bin\\youtube-dl.exe")
CMD_BASE = [YOUTUBE_DL, "--extract-audio", "--audio-format", "mp3"]

def checklinks(LINKS):
    if len(LINKS) < 1:
        raise Exception("[error] 'links.txt' ist leer!\n[lösung] erst links in 'links.txt' speichern!")

try:
    LINKS_FILE = open(Path(getcwd() + "\\links.txt"), "r")
    LINKS = LINKS_FILE.readlines()
    checklinks(LINKS)
    BEFEHL = CMD_BASE + LINKS
    print(f"[execute] {BEFEHL}")
    subprocess.call(BEFEHL)
    print("FERTIG!")
    CODE = 0
except FileNotFoundError:
    print(f"[error!]  'links.txt' wurde nicht gefunden!\n[lösung] 'links.txt' erstellen, erstelle 'links.txt'!\n")
    open("links.txt", "w").close()
    CODE = -1
except KeyboardInterrupt:
    print("[achtung!] DOWNLOAD MANUELL VOM BENUTZER ABGEBROCHEN!")
    CODE = -1
except Exception as e:
    print(e)
    CODE = -1
finally:
    exit(CODE)
    system("PAUSE")
