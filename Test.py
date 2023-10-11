import tkinter as tk
import subprocess
import shutil
from tkinter import messagebox
import os
import configparser


window = tk.Tk()
window.iconbitmap(r'D:\AppBuild\pythonProject1\icon.ico')
window.title("OpenBENPC")
window.geometry("350x1100")

config = configparser.ConfigParser()
config_path = "D:/config.ini"
folder1_default = "D:\d3-racing-legends2"
folder2_default = "D:\d3-racing-legends2"
folder3_default = "D:\d3-racing-legends2"

def load_config():
    if not os.path.exists(config_path):
        # Create the config.ini file if it doesn't exist
        config["Settings"] = {"folder1": folder1_default, "folder2": folder2_default, "folder3": folder3_default}
        with open(config_path, "w") as config_file:
            config.write(config_file)
    else:
        # Read the configuration from the existing file
        config.read(config_path)

def save_config():
    folder1 = folder1_entry.get()
    folder2 = folder2_entry.get()
    folder3 = folder3_entry.get()

    config.set("Settings", "folder1", folder1)
    config.set("Settings", "folder2", folder2)
    config.set("Settings", "folder3", folder3)

    with open(config_path, "w") as config_file:
        config.write(config_file)

def compare_folders():
    folder1 = folder1_entry.get()
    folder2 = folder2_entry.get()

    bcompare_path = r"C:\Program Files\Beyond Compare 4\BCompare.exe"
    subprocess.Popen([bcompare_path, folder1, folder2])

def download_files():
    folder1 = folder1_entry.get()
    folder2 = folder2_entry.get()

    # Prompt user to confirm file replacement
    confirmation = messagebox.askyesno("Xác Nhận", "Copy files?")

    if confirmation:
        # Copy files from folder2 to folder1, excluding files with ".ini" extension
        for root, _, files in os.walk(folder2):
            relative_path = os.path.relpath(root, folder2)
            target_path = os.path.join(folder1, relative_path)
            os.makedirs(target_path, exist_ok=True)

            for file in files:
                if not file.endswith(".ini"):  # Exclude files with ".ini" extension
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_path, file)

                    if os.path.exists(target_file):
                        os.remove(target_file)

                    shutil.copy(source_file, target_file)

        messagebox.showinfo("Xong", "Files have been copied.")
    else:
        messagebox.showinfo("Huỷ", "File copy has been cancelled.")

def git_pull():
    folder3 = folder3_entry.get()
    command = f"cd /d {folder3} && git pull"
    execute_command(command)

def git_reset_hard():
    folder3 = folder3_entry.get()
    command = f"cd /d {folder3} && git reset --hard"
    execute_command(command)

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        result_text.insert(tk.END, output.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        result_text.insert(tk.END, e.output.decode("utf-8"))

load_config()

folder1_label = tk.Label(window, text="My PC")
folder1_label.grid(row=0, column=0)

folder2_label = tk.Label(window, text="Ben PC")
folder2_label.grid(row=1, column=0)

folder3_label = tk.Label(window, text="Source Git")
folder3_label.grid(row=2, column=0 , padx=10, pady=10)

folder1_entry = tk.Entry(window)
folder1_entry.insert(0, config.get("Settings", "folder1", fallback=folder1_default))
folder1_entry.grid(row=0, column=1)

folder2_entry = tk.Entry(window)
folder2_entry.insert(0, config.get("Settings", "folder2", fallback=folder2_default))
folder2_entry.grid(row=1, column=1)

folder3_entry = tk.Entry(window)
folder3_entry.insert(0, config.get("Settings", "folder3", fallback=folder3_default))
folder3_entry.grid(row=2, column=1)

download_button = tk.Button(window, text="Tải Về", command=download_files)
download_button.grid(row=3, column=0, columnspan=2 , padx=10, pady=10)

compare_button = tk.Button(window, text="Compare", command=compare_folders)
compare_button.grid(row=4, column=0, columnspan=2)

save_button = tk.Button(window, text="Save Config", command=save_config)
save_button.grid(row=5, column=0, columnspan=2)


# Git Command Section
git_label = tk.Label(window, text="Git Commands")
git_label.grid(row=6, column=0, columnspan=2 ,padx=10, pady=10)


pull_button = tk.Button(window, text="1: Git Pull", command=git_pull)
pull_button.grid(row=7, column=0, columnspan=2)

reset_button = tk.Button(window, text="2: Git Reset (Revert))", command=git_reset_hard)
reset_button.grid(row=8, column=0, columnspan=2)

result_text = tk.Text(window, height=50, width=40)
result_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
