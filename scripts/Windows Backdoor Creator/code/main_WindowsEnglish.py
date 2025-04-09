import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import sys


# Funktion für Fehlerfenster
def show_error(message):
    root = tk.Tk()
    root.withdraw()  # Verhindert das Öffnen eines leeren Fensters
    messagebox.showerror("Error", message)
    root.quit()

# Funktion für Bestätigungsfenster
def ask_continue():
    root = tk.Tk()
    root.withdraw()
    return messagebox.askyesno("Backup exists", "A backup file already exists. Do you want to continue and overwrite it?")

# Benutzereingabe für den Dateipfad
user_input = simpledialog.askstring("Eingabe", "Gib den Dateipfad für *: C:\\Windows\\System32 ein. Beispiel: C:\\Windows\\System32")

if not user_input:
    show_error("No input provided.")
    sys.exit()  # Beendet das Programm, wenn keine Eingabe erfolgt

# Zielordner und Quellpfad
ziel = user_input.strip()  # Entfernt führende und folgende Leerzeichen
skript_ordner = os.path.dirname(os.path.abspath(__file__))
dateipfad = os.path.join(skript_ordner, "osk.exe")
dateipfadsys = os.path.join(ziel, "osk.exe")
dateipfadsys_backup = os.path.join(ziel, "osk_backup.exe")

# Überprüfen, ob osk.exe existiert
if not os.path.exists(dateipfad):
    show_error("Error 404: Cracked osk.exe not found.")
    sys.exit()  # Programm beenden

# Überprüfen, ob osk_backup.exe schon existiert
if os.path.exists(dateipfadsys_backup):
    if ask_continue():
        try:
            os.remove(dateipfadsys_backup)  # Alte Backup-Datei löschen
            print("osk_backup.exe removed.")
        except Exception as e:
            show_error(f"Failed to remove backup file: {e}")
            sys.exit()  # Programm beenden
    else:
        print("Operation canceled by user.")
        sys.exit()  # Wenn der Benutzer nicht fortfahren möchte, das Programm beenden

# Wenn osk.exe im Zielordner existiert, umbenennen in osk_backup.exe
if os.path.exists(dateipfadsys):
    os.rename(dateipfadsys, dateipfadsys_backup)
    print("Backup of old file created.")

# Die neue osk.exe kopieren
try:
    shutil.copy(dateipfad, dateipfadsys)
    print("New file copied successfully.")
except Exception as e:
    show_error(f"Failed to copy new file: {e}")
    sys.exit()  # Programm beenden

# Erfolgs-Popup anzeigen
root = tk.Tk()
root.withdraw()  # Verhindert das Öffnen eines leeren Fensters
messagebox.showinfo("Done", "The operation was successful. For more information, check GitHub.")
root.quit()
