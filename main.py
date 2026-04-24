import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import PIL.Image
import PIL.ImageTk

from muscle_therapy_agent import MuscleTherapyAgent


class MuscleTherapyWindow:
    """Floating window that hosts the Muscle Therapy Consultant chat interface."""

    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Muscle Therapy Consultant")
        self.window.resizable(True, True)

        self.agent = MuscleTherapyAgent()

        # Title label
        title = tk.Label(
            self.window,
            text="💪 Muscle Therapy Consultant",
            font=("Helvetica", 14, "bold"),
        )
        title.pack(padx=10, pady=(10, 4))

        subtitle = tk.Label(
            self.window,
            text="Ask me about soreness, stretching, injuries, recovery, and more.",
            font=("Helvetica", 9),
            fg="gray",
        )
        subtitle.pack(padx=10, pady=(0, 8))

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            state=tk.DISABLED,
            width=60,
            height=20,
            font=("Helvetica", 10),
        )
        self.chat_display.pack(padx=10, pady=4, fill=tk.BOTH, expand=True)

        # Input frame
        input_frame = tk.Frame(self.window)
        input_frame.pack(padx=10, pady=8, fill=tk.X)

        self.user_input = tk.Entry(input_frame, font=("Helvetica", 10))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        self.user_input.bind("<Return>", lambda event: self.send_message())

        send_btn = tk.Button(input_frame, text="Send", command=self.send_message)
        send_btn.pack(side=tk.RIGHT)

        # Display the welcome message
        self._append_message("Consultant", self.agent.consult(""))

    def send_message(self):
        text = self.user_input.get().strip()
        if not text:
            return
        self._append_message("You", text)
        self.user_input.delete(0, tk.END)
        response = self.agent.consult(text)
        self._append_message("Consultant", response)

    def _append_message(self, sender: str, message: str):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}:\n{message}\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)


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

        self.consultant_button = tk.Button(
            self.master,
            text="💪 Open Muscle Therapy Consultant",
            command=self.open_consultant,
        )
        self.consultant_button.pack(pady=10)

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

    def open_consultant(self):
        MuscleTherapyWindow(self.master)


if __name__ == '__main__':
    root = tk.Tk()
    app = ImageClassifier(root)
    root.mainloop()