import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def set_volume(value):
    """Set system volume using pactl"""
    volume = int(value)
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])
    volume_label.configure(text=f"Volume: {volume}%")

def increase_volume():
    """Increase volume by 10%"""
    current_volume = get_current_volume()
    new_volume = min(current_volume + 10, 200)  
    set_volume(new_volume)
    volume_slider.set(new_volume)

def decrease_volume():
    """Decrease volume by 10%"""
    current_volume = get_current_volume()
    new_volume = max(current_volume - 10, 0)
    set_volume(new_volume)
    volume_slider.set(new_volume)

def get_current_volume():
    """Get the current system volume"""
    try:
        result = subprocess.run(["pactl", "get-sink-volume", "@DEFAULT_SINK@"], capture_output=True, text=True)
        volume = int(result.stdout.split('/')[1].strip().replace('%', ''))
        return volume
    except Exception:
        return 100  
root = ctk.CTk()
root.title("Volume Booster")
root.geometry("300x200")

volume_label = ctk.CTkLabel(root, text="Volume: 100%", font=("Arial", 14))
volume_label.pack(pady=10)

volume_slider = ctk.CTkSlider(root, from_=0, to=200, command=lambda value: set_volume(value))
volume_slider.set(100)
volume_slider.pack()

ctk.CTkButton(root, text="Increase", command=increase_volume).pack(pady=5)
ctk.CTkButton(root, text="Decrease", command=decrease_volume).pack(pady=5)

root.mainloop()
