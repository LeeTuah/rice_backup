from pathlib import Path
import shutil

true = True
false = False

USERNAME = "leetuah"
HOMEPATH = Path(f"/home/{USERNAME}")

# config_path = f"{HOMEPATH}/.config/"
# wallpaper_path = f"{HOMEPATH}/Pictures/Wallpapers/"

# located in ~/.config
config_folders = [
	"alacritty", "fastfetch", "i3", "i3blocks", "polybar", "rofi", "wal", "picom",
	"dunst"
]

config_files = [
	"starship.toml"
]

# located in ~
base_file = [
	".zshrc"
]

def verify_config_folders(rice_backup: bool):
	base_path = Path()
	if rice_backup: base_path = HOMEPATH / "rice_backup" / ".config"
	else: base_path = HOMEPATH / ".config"

	base_path.mkdir(parents=True, exist_ok=True)
	all_folder = [f.name for f in base_path.iterdir() if f.is_dir()]
	all_files = [f.name for f in base_path.iterdir() if f.is_file()]

	missing_folders = set(config_folders) - set(all_folder)
	for folder in missing_folders:
		folder_path = base_path / folder
		folder_path.mkdir(exist_ok=True)

	missing_files = set(config_files) - set(all_files)
	for file in missing_files:
		file_path = base_path / file
		file_path.touch()

	base_path = Path()
	if rice_backup: base_path = HOMEPATH / "rice_backup"
	else: base_path = HOMEPATH

	all_files = [f.name for f in base_path.iterdir() if f.is_file()]
	missing_base_files = set(base_file) - set(all_files)

	for file in missing_base_files:
		file_path = base_path / file
		file_path.touch()


def verify_wallpapers_folders(rice_backup: bool):
	base_path = Path()
	if rice_backup: base_path = HOMEPATH / "rice_backup" / "Pictures" / "Wallpapers"
	else: base_path = HOMEPATH / "Pictures" / "Wallpapers"

	base_path.mkdir(parents=True, exist_ok=True)

def backup(run_backup: bool):
	# .config files backup
	source_path = HOMEPATH / ".config"
	backup_path = HOMEPATH / "rice_backup" / ".config"

	for folder in config_folders:
		source_folder = source_path / folder
		backup_folder = backup_path / folder

		if run_backup:
			if source_folder.exists():
				if backup_folder.exists():
					shutil.rmtree(backup_folder)

				shutil.copytree(source_folder, backup_folder, symlinks=true)
				print(f"[+] Backed up {folder}")

		else:
			if backup_folder.exists():
				if source_folder.exists():
					shutil.rmtree(source_folder)

				shutil.copytree(backup_folder, source_folder, symlinks=true)
				print(f"[*] Restored {folder}")

	for file in config_files:
		source_file = source_path / file
		backup_file = backup_path / file

		if run_backup:
			if source_file.exists():
				shutil.copy(source_file, backup_file)
				print(f"[+] Backed up {file}")

		else:
			if backup_file.exists():
				shutil.copy(backup_file, source_file)
				print(f"[+] Restored {file}")
	
	# base folder backup
	for file in base_file:
		source_file = HOMEPATH / file
		backup_file = HOMEPATH / "rice_backup" / file

		if run_backup:
			if source_file.exists():
				shutil.copy(source_file, backup_file)
				print(f"[+] Backed up {file}")

		else:
			if backup_file.exists():
				shutil.copy(backup_file, source_file)
				print(f"[+] Restored {file}")

	# wallpapers backup
	source_path = HOMEPATH / "Pictures" / "Wallpapers"
	backup_path = HOMEPATH / "rice_backup" / "Pictures" / "Wallpapers"

	if run_backup:
		if source_path.exists():
			shutil.copytree(source_path, backup_path, dirs_exist_ok=true)
			print("[-] Backed up wallpapers.")

	else:
		if backup_path.exists():
			shutil.copytree(backup_path, source_path, dirs_exist_ok=true)
			print("[-] Restored wallpapers.")

def main():
	print("1. Back up Rice\n2. Load last Backup\n3. Exit\n>> ", end="")
	choice = int(input())

	if choice == 1:
		verify_config_folders(true)
		verify_wallpapers_folders(true)

		backup(true)

	elif choice == 2:
		verify_config_folders(false)
		verify_wallpapers_folders(false)

		backup(false)

	elif choice == 3:
		return

if __name__ == "__main__":
	main()