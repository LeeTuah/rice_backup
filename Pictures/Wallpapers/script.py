from pathlib import Path
import random
import subprocess

wallpaper_folder_path = "/home/leetuah/Pictures/Wallpapers/"
wallpaper_folder = Path(wallpaper_folder_path)
all_walls = [f.name for f in wallpaper_folder.iterdir() if f.is_file()]
status_code = 999

while (status_code != 0):
	random_wall = random.choice(all_walls)
	if random_wall == "script.py": continue

	feh_run_process = subprocess.run(["feh", "--bg-fill", f"{wallpaper_folder_path}{random_wall}"], capture_output=True, text=True)

	print("Output:", feh_run_process.stdout)
	print("Error:", feh_run_process.stderr)
	print("Status code", feh_run_process.returncode, "\n")

	status_code = feh_run_process.returncode

	if status_code == 0:
		subprocess.run(["wal", "-i", f"{wallpaper_folder_path}{random_wall}"])
		subprocess.run(["i3-msg", "reload"])
		subprocess.run(["polybar-msg", "cmd", "restart"])
