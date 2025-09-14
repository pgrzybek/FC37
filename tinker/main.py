import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uwaga", "Nie możesz dodać pustego zadania!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

root = tk.Tk()
root.title("Backlog")

# Pole do wpisywania
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Przycisk "Dodaj"
add_button = tk.Button(root, text="Dodaj zadanie", command=add_task)
add_button.pack(pady=5)

# Lista zadań
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

# Przycisk "Usuń"
delete_button = tk.Button(root, text="Usuń zaznaczone", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
