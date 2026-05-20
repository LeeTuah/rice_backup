from pathlib import Path
import random
import subprocess
import time

USERNAME = "leetuah"
SLIDESHOW_TIME_IN_SEC = 600

wallpaper_folder_path = "/home/{USERNAME}/Pictures/Wallpapers/"
wallpaper_folder = Path(wallpaper_folder_path)
all_walls = [f.name for f in wallpaper_folder.iterdir() if f.is_file()]

while (True):
	random_wall = random.choice(all_walls)
	if random_wall in ["script.py", "script_slideshow.py"]: continue

	feh_run_process = subprocess.run(["feh", "--bg-fill", f"{wallpaper_folder_path}{random_wall}"], capture_output=True, text=True)

	print("Output:", feh_run_process.stdout)
	print("Error:", feh_run_process.stderr)
	print("Status code", feh_run_process.returncode, "\n")

	if feh_run_process.returncode == 0:
		subprocess.run(["wal", "-q", "-n", "-i", f"{wallpaper_folder_path}{random_wall}"])
		subprocess.run(["ln", "-sf", f"/home/{USERNAME}/.cache/wal/colors-discord.css", f"/home/{USERNAME}/.config/vesktop/themes/pywal.theme.css"])
		subprocess.run(["i3-msg", "reload"])
		subprocess.run(["polybar-msg", "cmd", "restart"])

	time.sleep(SLIDESHOW_TIME_IN_SEC)
