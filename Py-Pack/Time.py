import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())  # Get current time
    time_label.config(text=current_time)  # Update label with the current time
    root.after(100, update_time)  # Schedule the function to run again in 100ms

# Create the main window
root = tk.Tk()
root.overrideredirect(True)  # Make the window borderless
root.geometry("200x50+100+100")  # Set size and position of the window
root.configure(bg="black")  # Set background color to black
root.attributes('-topmost', True)  # Keep the window on top

# Create a label to display the time
time_label = tk.Label(root, text="", font=("Arial", 24), fg="white", bg="black")
time_label.pack(expand=True)

# Start updating the time
update_time()

# Start the GUI event loop
root.mainloop()
