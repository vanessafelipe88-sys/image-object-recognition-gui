import tkinter as tk
from tkinter import filedialog, messagebox
import os
import PIL.Image
import PIL.ImageTk

class ImageClassifier:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Classification GUI")

        self.label = tk.Label(self.master, text="Upload an image for classification:")
        self.label.pack(padx=20, pady=20)

        self.upload_button = tk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.image_label = tk.Label(self.master)
        self.image_label.pack(pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            self.display_image(file_path)
            # Here you can add your image classification logic
            messagebox.showinfo("Info", "Image uploaded successfully!")

    def display_image(self, file_path):
        img = PIL.Image.open(file_path)
        img.thumbnail((300, 300))  # Resize for display
        img = PIL.ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img  # Keep a reference to avoid garbage collection

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageClassifier(root)
    root.mainloop()