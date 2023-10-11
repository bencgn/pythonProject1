import os
import tkinter as tk
from tkinter import filedialog

class FolderStructureCreator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.iconbitmap(r'D:\AppBuild\pythonProject1\icon.ico')
        self.title("FolderStructureCreator- bendemo v0.1")
        self.geometry("350x300")

        self.folder_path = tk.StringVar()

        self.create_widgets()

    def create_structure(self):
        selected_directory = filedialog.askdirectory(title="Select a Directory")
        if selected_directory:
            subfolders = ['Prefabs', 'Models', 'Textures', 'Materials']
            for subfolder in subfolders:
                folder_path = os.path.join(selected_directory, subfolder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
            self.status_label.config(text="Folders created successfully.")
        else:
            self.status_label.config(text="No directory selected.")

    def create_widgets(self):
        directory_label = tk.Label(self, text="Selected Directory:")
        create_button = tk.Button(self, text="Create Folder Structure", command=self.create_structure)
        self.status_label = tk.Label(self, text="")

        directory_label.pack()
        create_button.pack()
        self.status_label.pack()

if __name__ == "__main__":
    app = FolderStructureCreator()
    app.mainloop()
