from os import getcwd, system
from pathlib import Path
import subprocess


YOUTUBE_DL = Path(getcwd() + "\\bin\\youtube-dl.exe")
CMD_BASE = [YOUTUBE_DL, "--extract-audio", "--audio-format", "mp3"]

try:
    LINKS_FILE = open(Path(getcwd() + "\\links.txt"), "r")
    LINKS = LINKS_FILE.readlines()
    BEFEHL = CMD_BASE + LINKS
    print(f"[execute] {BEFEHL}")
    subprocess.call(BEFEHL)
    print("FERTIG!")
    system("PAUSE")
except FileNotFoundError:
    print(f"[error]  'links.txt' wurde nicht gefunden!\n[lösung] 'links.txt' erstellen, erstelle 'links.txt'!\n")
    open("links.txt", "w").close()
    system("PAUSE")
    exit(-1)
except KeyboardInterrupt:
    print("DOWNLOAD ABGEBROCHEN!")
    system("PAUSE")
    exit(-1)
system("PAUSE")
