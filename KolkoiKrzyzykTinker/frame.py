import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Tworzymy ramkę
frame = tk.Frame(root, bg="lightblue", bd=3, relief="solid")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Dodajemy przycisk do ramki
button = tk.Button(frame, text="Kliknij mnie", bg="lightblue", bd=3, relief="solid")
button.pack(pady=10)

root.mainloop()
