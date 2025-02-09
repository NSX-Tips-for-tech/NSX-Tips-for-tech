import json
import os
import tkinter as tk
from tkinter import messagebox

def update_json():
    try:
        fps_value = entry.get()
        if not fps_value.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            return
        
        fps_value = int(fps_value)
        
        folder_path = r"C:\\Users\\nonoh\\AppData\\Local\\Roblox\\Versions\\ClientSettings"
        file_path = os.path.join(folder_path, "ClientAppSettings.json")
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        data = {"DFIntTaskSchedulerTargetFps": fps_value}
        
        if os.path.exists(file_path):
            os.remove(file_path)
        
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        messagebox.showinfo("Success", f"FPS updated to {fps_value}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("FPS Booster")
root.geometry("300x250")
root.configure(bg='black')  # Set background color to black

# Set the icon (make sure you have a 'hammer.ico' file)
root.iconbitmap('hammer.ico')

label = tk.Label(root, text="Enter FPS:", fg='lightgrey', bg='black')  # Light grey text
label.pack(pady=5)

entry = tk.Entry(root, fg='lightgrey', bg='black', insertbackground='lightgrey')  # Light grey text
entry.pack(pady=5)

button = tk.Button(root, text="Boost FPS", command=update_json, fg='lightgrey', bg='black', relief='solid')
button.pack(pady=10)

root.mainloop()
