from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image

# Open a file dialog to select an image file
file_path = askopenfilename()
if not file_path:
    print("No file selected")
    exit()

# Open the selected image file
img = Image.open(file_path)
myheight, mywidth = img.size
format = img.format

# Resize the image using LANCZOS filter
img = img.resize((myheight, mywidth), Image.LANCZOS)

# Open a file dialog to save the compressed image
save_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
if not save_path:
    print("No save location selected")
    exit()

# Save the compressed image
img.save(save_path)
print(f"Image saved at {save_path}")
