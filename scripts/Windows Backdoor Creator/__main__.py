import tkinter as tk
from tkinter import ttk
import subprocess
import time
import sys

def frage_popup():
    root = tk.Tk()
    root.title("Einstellungen wählen")

    # Setzt die Größe des Fensters
    root.geometry("300x200")

    # Funktion zur Bestätigung der Auswahl
    def bestatige_auswahl():
        sprache_ausgewaehlt = sprache.get()
        os_ausgewaehlt = os.get()
        print(f"Sprache: {sprache_ausgewaehlt}")
        print(f"Betriebssystem: {os_ausgewaehlt}")
        root.quit()  # Schließt das Fenster nach der Auswahl

    # Schritt 1: Sprache auswählen
    label_sprache = tk.Label(root, text="Wählen Sie eine Sprache:")
    label_sprache.pack(pady=10)

    sprache = ttk.Combobox(root, values=["Deutsch", "English"], state="readonly")
    sprache.pack(pady=10)
    sprache.current(0)  # Standardmäßig "Deutsch" auswählen

    # Schritt 2: Betriebssystem auswählen
    label_os = tk.Label(root, text="Wählen Sie das Betriebssystem:")
    label_os.pack(pady=10)

    os = ttk.Combobox(root, values=["Linux","Windows"], state="readonly")
    os.pack(pady=10)
    os.current(0)  # Standardmäßig "Windows" auswählen

    # Bestätigungsbutton
    button = tk.Button(root, text="Bestätigen", command=bestatige_auswahl)
    button.pack(pady=10)

    # Startet das Tkinter-Fenster
    root.mainloop()

    return sprache.get(), os.get()

# Programmausführung
sprache, os = frage_popup()

def anderes_programm_ausfuehren():
    # Pfad zum anderen Python-Skript
    # Beispiel: 'python3' für Linux oder 'python' für Windows
    if os == "Linux":
        result = subprocess.run(['python3', f'code\main_Linux{sprache}.py'], capture_output=True, text=True)
    elif os == "Windows":
        result = subprocess.run(['python', f'code\main_Windows{sprache}.py'], capture_output=True, text=True)

    # Fehlerausgabe (falls vorhanden)
    if result.stderr:
        print("Error:")
        print(result.stderr)

# Programmausführung
anderes_programm_ausfuehren()

time.sleep(1)
sys.exit()
