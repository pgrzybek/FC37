import tkinter as tk
from PIL import Image, ImageTk

def przycisk_klik():
    print("Przycisk kliknięty!")

root = tk.Tk()
root.title("Przycisk z obrazkiem")
#photo = tk.PhotoImage(file="przycisk.jpg")

# Wczytanie obrazu
#image = Image.open("przycisk.jpg")  # plik w katalogu głównym
#photo = ImageTk.PhotoImage(image)

# Tworzymy przycisk z obrazkiem
button = tk.Button(root, image=photo, command=przycisk_klik, borderwidth=0)
button.pack(pady=20)

# Konieczne, żeby Python nie usunął referencji do obrazka
button.image = photo

root.mainloop()
