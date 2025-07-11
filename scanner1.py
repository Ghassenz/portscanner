#!/usr/bin/env python3
import socket
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

def scan_ports():
    target = entry_target.get()
    port_range = entry_ports.get()

    try:
        start_port, end_port = map(int, port_range.split('-'))
    except:
        messagebox.showerror("Erreur", "Plage de ports invalide ! (ex: 1-100)")
        return

    total_ports = end_port - start_port + 1
    progress_bar["maximum"] = total_ports
    result_box.delete(1.0, tk.END)
    status_label.config(text="🔎 Scan en cours...")
    root.update()

    count = 0
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "inconnu"
            result_box.insert(tk.END, f"[+] Port {port} ({service}) ouvert\n")
        s.close()
        count += 1
        progress_bar["value"] = count
        root.update_idletasks()

    status_label.config(text="✅ Scan terminé.")
    root.update()

# 🎨 Thème sombre personnalisé
bg_color = "#87CEEB"  # Bleu ciel
fg_color = "#000000"  # Noir
button_color = "#1E88E5"
font_default = ("Consolas", 11)

root = tk.Tk()
root.title("Scanner de ports - Kali")
root.configure(bg=bg_color)

# Champs
tk.Label(root, text="Adresse IP :", bg=bg_color, fg=fg_color, font=font_default).grid(row=0, column=0, sticky="e")
entry_target = tk.Entry(root, width=30, font=font_default)
entry_target.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Plage de ports (ex: 1-100):", bg=bg_color, fg=fg_color, font=font_default).grid(row=1, column=0, sticky="e")
entry_ports = tk.Entry(root, width=30, font=font_default)
entry_ports.insert(0, "1-1024")
entry_ports.grid(row=1, column=1, padx=5, pady=5)

# Bouton
scan_button = tk.Button(root, text="🚀 Lancer le scan", command=scan_ports, bg=button_color, fg="white", font=("Arial", 11, "bold"))
scan_button.grid(row=2, columnspan=2, pady=10)

# Zone résultat
result_box = scrolledtext.ScrolledText(root, width=60, height=20, bg="#1E1E1E", fg="#00FF00", font=("Courier", 10))
result_box.grid(row=3, columnspan=2, padx=10, pady=10)

# Barre de progression
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=4, columnspan=2, pady=5)

# Statut
status_label = tk.Label(root, text="⏳ En attente...", bg=bg_color, fg="#AAAAAA", font=("Arial", 10, "italic"))
status_label.grid(row=5, columnspan=2, pady=5)

root.mainloop()
