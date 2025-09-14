import tkinter as tk

def przycisk_klik():
    print("Przycisk kliknięty!")

root = tk.Tk()
root.title("Przycisk z GIF")

# Ładujemy obraz GIF (tylko GIF/PPM/PGM działa bez Pillow)
photo = tk.PhotoImage(file="przycisk.gif")

# Tworzymy przycisk z obrazkiem
button = tk.Button(root, image=photo, command=przycisk_klik, borderwidth=0)
button.pack(pady=20)

# Trzymamy referencję do PhotoImage, inaczej obraz zniknie
button.image = photo

root.mainloop()
