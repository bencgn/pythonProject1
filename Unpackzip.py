import tkinter as tk
from tkinter import filedialog
import os
import zipfile

def select_folder():
    folder_path = filedialog.askdirectory()
    folder1_entry.delete(0, tk.END)
    folder1_entry.insert(0, folder_path)

def rename_and_export():
    folder_path = folder1_entry.get()
    if not folder_path:
        return

    for filename in os.listdir(folder_path):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(folder_path, filename)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                for member in zip_file.infolist():
                    if member.filename.endswith('.webp') or member.filename.endswith('.gltf'):
                        new_filename = os.path.splitext(filename)[0] + '.zip'
                        new_webp_filename = os.path.splitext(filename)[0] + '.webp'
                        new_gltf_filename = os.path.splitext(filename)[0] + '.gltf'
                        zip_file.extract(member.filename, folder_path)
                        if member.filename.endswith('.webp'):
                            os.rename(os.path.join(folder_path, member.filename), os.path.join(folder_path, new_webp_filename))
                        elif member.filename.endswith('.gltf'):
                            os.rename(os.path.join(folder_path, member.filename), os.path.join(folder_path, new_gltf_filename))

            with zipfile.ZipFile(os.path.join(folder_path, new_filename), 'w', zipfile.ZIP_DEFLATED) as new_zip_file:
                for file_to_zip in os.listdir(folder_path):
                    if file_to_zip.endswith('.webp') or file_to_zip.endswith('.gltf'):
                        new_zip_file.write(os.path.join(folder_path, file_to_zip), file_to_zip)

            # Remove the original .zip file
            os.remove(zip_file_path)

    folder1_entry.delete(0, tk.END)
    folder1_entry.insert(0, "Done!")



# Create the main window
root = tk.Tk()
root.title("Folder Zip File Processor")

# Create and configure a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Label and Entry for folder path
folder1_label = tk.Label(frame, text="Select Folder:")
folder1_label.pack()

folder1_entry = tk.Entry(frame)
folder1_entry.pack(fill=tk.X, padx=10, pady=5)

# Buttons for folder selection and processing
select_button = tk.Button(frame, text="Select Folder", command=select_folder)
select_button.pack()

process_button = tk.Button(frame, text="Rename and Export", command=rename_and_export)
process_button.pack()

# Run the main loop
root.mainloop()
