import os
import subprocess
import tkinter as tk
from tkinter import filedialog


def install_software(directory):
    software_files = ['photoshop_setup.exe', '3dmax_setup.exe']  # Add more software files as needed
    for software_file in software_files:
        software_path = os.path.join(directory, software_file)
        if os.path.isfile(software_path):
            subprocess.call([software_path])  # Run the software installer


def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)


def install_from_usb():
    directory = directory_entry.get()
    if directory:
        install_software(directory)


# Create the main window
window = tk.Tk()
window.title("Software Installer")

# Create the directory selection label and entry
directory_label = tk.Label(window, text="Select USB Drive:")
directory_label.pack()

directory_entry = tk.Entry(window, width=50)
directory_entry.pack()

# Create the browse button
browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack()

# Create the install button
install_button = tk.Button(window, text="Install", command=install_from_usb)
install_button.pack()

# Start the main loop
window.mainloop()
