import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.iconbitmap(r'D:\AppBuild\pythonProject1\icon.ico')
        self.title("Converter va 512 - bendemo v0.1")
        self.geometry("350x300")
        self.folder_path = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        folder_label = tk.Label(self, text="Chon Thu Muc:")
        folder_label.pack(pady=10)

        folder_entry = tk.Entry(self, textvariable=self.folder_path, width=40)
        folder_entry.pack(pady=5)

        folder_button = tk.Button(self, text="Browse", command=self.choose_folder)
        folder_button.pack(pady=5)

        convert_button = tk.Button(self, text="to JPG", command=self.convert_to_jpg)
        convert_button.pack(pady=10)

        convert_button = tk.Button(self, text="to PNG (Interlaced)", command=self.convert_to_png)
        convert_button.pack(pady=10)

        resize_button = tk.Button(self, text="resize 512x512", command=self.resize_images)
        resize_button.pack(pady=5)

    def choose_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def convert_to_jpg(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            self.show_message("Deo Thay thu muc")
            return

        output_folder = os.path.join(folder_path, "converted")
        os.makedirs(output_folder, exist_ok=True)

        images = self.get_supported_images(folder_path)
        if not images:
            self.show_message("Deo Thay hinh")
            return

        for image_path in images:
            img = Image.open(image_path)
            img = img.convert("RGB")
            output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + ".jpg")
            img.save(output_path, "JPEG")

        self.show_message("OK Cu")

    def convert_to_png(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            self.show_message("No folder selected")
            return

        output_folder = os.path.join(folder_path, "convertedpng")
        os.makedirs(output_folder, exist_ok=True)

        images = self.get_supported_images(folder_path)
        if not images:
            self.show_message("No images found")
            return

        for image_path in images:
            img = Image.open(image_path)
            output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + ".png")
            img.save(output_path, "PNG", interlace=True)

        self.show_message("Conversion to PNG (Interlaced) complete")
    def resize_images(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            self.show_message("Chua chon thu muc")
            return

        output_folder = os.path.join(folder_path, "resized")
        os.makedirs(output_folder, exist_ok=True)

        images = self.get_supported_images(folder_path)
        if not images:
            self.show_message("Deo Thay")
            return

        for image_path in images:
            img = Image.open(image_path)
            img = img.resize((512, 512))
            output_path = os.path.join(output_folder, os.path.basename(image_path))
            img.save(output_path)

        self.show_message("OK Cu")

    def get_supported_images(self, folder_path):
        supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".tga", ".webp")
        images = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(supported_formats):
                    images.append(os.path.join(root, file))
        return images

    def show_message(self, message):
        messagebox.showinfo("Message", message)


if __name__ == "__main__":
    app = ImageConverterGUI()
    app.mainloop()
