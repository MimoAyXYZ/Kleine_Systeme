import tkinter as tk
from tkinter import ttk
import customtkinter
from CTkListbox import *
import random
import os
import sys


# Funktion zum Laden von Ressourcen (z. B. Dateien), auch wenn das Programm als .exe läuft
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Pfad im temporären Ordner, wenn als .exe ausgeführt
    except Exception:
        base_path = os.path.abspath(".")  # Pfad im normalen Entwicklungsmodus
    return os.path.join(base_path, relative_path)


# Erscheinungsbild der GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Datei 1 lesen
f = "Speicher_Datein/data.txt"
with open(resource_path(f), "a+", encoding="utf-8") as f:
    f.seek(0)
    daten = f.readlines()

# Datei 2 lesen
f2 = "Speicher_Datein/user_data.txt"
with open(resource_path(f2), "a+", encoding="utf-8") as f2:
    f2.seek(0)
    user_daten = f2.readlines()

liste_kleinebuchstaben: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'v', 'w', 'x', 'y', 'z']
liste_grossbuchstaben: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
liste_ziffern: list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
liste_sonderzeichen: list = ['~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                             '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

fehler_meldung_chb: bool = False
eingelogt: bool = False
passwort = ""





def pin_setzen(status):
    global root_pin_setzen, entry1_pin, entry2_pin, entry_var1_pin, entry_var2_pin, label1_pin_var, label2_pin_var, button_pin_var, status_global
    root_pin_setzen = customtkinter.CTkToplevel()
    root_pin_setzen.title("Pin setzen")
    root_pin_setzen.geometry("400x200")

    status_global = status

    entry_var1_pin = tk.StringVar()
    entry_var2_pin = tk.StringVar()

    label1_pin_var = tk.StringVar()
    label2_pin_var = tk.StringVar()

    button_pin_var = tk.StringVar()

    root_pin_setzen.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), weight=1, uniform="a")
    root_pin_setzen.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1, uniform="a")

    # Labels und Buttons ect erstellen
    label1_pin = customtkinter.CTkLabel(root_pin_setzen, textvariable=label1_pin_var)
    label2_pin = customtkinter.CTkLabel(root_pin_setzen, textvariable=label2_pin_var)

    button1 = customtkinter.CTkButton(root_pin_setzen, textvariable=button_pin_var, command=input_pin_auslesen)

    entry1_pin = customtkinter.CTkEntry(root_pin_setzen, textvariable=entry_var1_pin)
    entry2_pin = customtkinter.CTkEntry(root_pin_setzen, textvariable=entry_var2_pin)

    # Labels und Buttons ect anzeigen
    label1_pin.grid(row=1, column=1, columnspan=2, sticky="ew")
    label2_pin.grid(row=4, column=1, columnspan=2, sticky="ew")

    button1.grid(row=2, column=10, rowspan=2, columnspan=2, sticky="ew")

    entry1_pin.grid(row=2, rowspan=2, column=1, columnspan=5, sticky="ew")
    entry2_pin.grid(row=5, rowspan=2, column=1, columnspan=5, sticky="ew")
    if status == 1:
        label1_pin_var.set("Pin setzen:")
        label2_pin_var.set("Pin wiederholen:")
        button_pin_var.set("Pin setzen")
    elif status == 0:
        label1_pin_var.set("Pin:")
        label2_pin_var.set("Pin wiederholen:")
        button_pin_var.set("Einloggen")
    root_pin_setzen.mainloop()


def konto():
    root_konto = customtkinter.CTkToplevel()
    root_konto.title("Konto")
    root_konto.geometry("200x250")

    def konto_loeschen():
        print("Gelöscht")
        if user_daten:
            user_daten.clear()
            daten.clear()
            f1 = "Speicher_Datein/data.txt"
            with open(resource_path(f1), "w", encoding="utf-8"):
                pass
            f1 = "Speicher_Datein/user_data.txt"
            with open(resource_path(f1), "w", encoding="utf-8"):
                pass
            text_var1.set(f"Gespeicherte Passwörter : {len(daten)}")
            if user_daten:
                text_var2.set("Konto vorhanden")
            else:
                text_var2.set("Kein Konto vorhanden")

    def checkbox_changed():
        if cb_var.get():
            button_reset.configure(state="normal")
        else:
            button_reset.configure(state="disabled")

    text_var1 = tk.StringVar()
    text_var1.set(f"Gespeicherte Passwörter : {len(daten)}")

    text_var2 = tk.StringVar()
    if user_daten:
        text_var2.set("Konto vorhanden")
    else:
        text_var2.set("Kein Konto vorhanden")

    cb_var = tk.BooleanVar()

    label = customtkinter.CTkLabel(root_konto, textvariable=text_var2)
    label.pack(pady=10)
    label02 = customtkinter.CTkLabel(root_konto, textvariable=text_var1)
    label02.pack(pady=10)

    button_reset = customtkinter.CTkButton(root_konto, text="Konto Löschen", corner_radius=100,
                                           state="disabled", command=konto_loeschen)
    button_reset.pack(pady=10)

    cb = customtkinter.CTkCheckBox(root_konto,
                                   text="Ich stimme zu, \ndass alle meine\nDaten unwiderruflich\ngelöscht werden",
                                   variable=cb_var, command=checkbox_changed)
    cb.pack(pady=10)

    root_konto.mainloop()


def gespeicherte_passwoerter():
    global user_daten, daten, eingelogt, f

    if not user_daten:
        pin_setzen(1)
        return
    else:
        if not eingelogt:
            pin_setzen(0)
        if eingelogt:
            root_gespeicherte_passwoerter = customtkinter.CTk()
            root_gespeicherte_passwoerter.title("Gespeicherte Passwörter")
            root_gespeicherte_passwoerter.geometry("300x400")

            # Container für die Listbox
            listbox_frame = customtkinter.CTkFrame(root_gespeicherte_passwoerter)
            listbox_frame.pack(pady=10, fill="both", expand=True)

            lb_container = []

            def lade_daten():
                global daten
                f = "Speicher_Datein/data.txt"
                os.makedirs(resource_path("Speicher_Datein"), exist_ok=True)
                try:

                    with open(resource_path(f), "r", encoding="utf-8") as f:
                        daten[:] = [zeile.strip().split("   ") for zeile in f if zeile.strip()]
                except Exception as e:
                    daten[:] = []

                # Alte Listbox entfernen, neue erstellen
                if lb_container:
                    lb_container[0].destroy()

                lb = CTkListbox(listbox_frame)
                lb.pack(fill="both", expand=True)
                lb_container.clear()
                lb_container.append(lb)

                for item in daten:
                    lb.insert("end", "   ".join(item))

            def delet_passwoert():
                if not lb_container:
                    return

                lb = lb_container[0]
                index_tuple = lb.curselection()

                if isinstance(index_tuple, (tuple, list)):
                    if not index_tuple:
                        return
                    index = index_tuple[0]
                else:
                    # Falls direkt ein int zurückkommt
                    index = index_tuple
                lb.delete(index)
                daten.pop(index)

                try:
                    datei_pfad = "Speicher_Datein/data.txt"
                    with open(resource_path(datei_pfad), "w", encoding="utf-8") as f_neu:
                        for zeile in daten:
                            f_neu.write("   ".join([str(x) for x in zeile]) + "\n")
                except Exception as e:
                    print("Fehler beim Schreiben der Datei:", e)

                lade_daten()

            # Buttons
            button_delet = customtkinter.CTkButton(root_gespeicherte_passwoerter, text="Löschen",
                                                   command=delet_passwoert)
            button_delet.pack(pady=5)

            # Initiales Laden
            lade_daten()

            root_gespeicherte_passwoerter.mainloop()


def erstellen():
    global passwort
    anzahl_zeichen: int = int(regler.get())
    grossbuchstaben: bool = var_chb1.get()
    kleinbuchstaben: bool = var_chb2.get()
    ziffern: bool = var_chb3.get()
    sonderzeichen: bool = var_chb4.get()

    if not (grossbuchstaben or kleinbuchstaben or ziffern or sonderzeichen):
        fehler_meldung = True
    else:
        fehler_meldung = False

        liste_variation_auswahl: list = []

        zusammenstellung: list = []
        anzahl_variation: int = 0

        if grossbuchstaben:
            anzahl_variation += 1
            liste_variation_auswahl.append(liste_grossbuchstaben)
        if kleinbuchstaben:
            anzahl_variation += 1
            liste_variation_auswahl.append(liste_kleinebuchstaben)
        if ziffern:
            anzahl_variation += 1
            liste_variation_auswahl.append(liste_ziffern)
        if sonderzeichen:
            anzahl_variation += 1
            liste_variation_auswahl.append(liste_sonderzeichen)

        anzahl_zeichen2: int = anzahl_zeichen

        while len(zusammenstellung) != anzahl_zeichen:
            anzahl_zeichen2 = anzahl_zeichen - len(zusammenstellung)
            if anzahl_variation > 1:
                idx: int = random.randint(0, len(liste_variation_auswahl) - 1)
            else:
                idx = 0
            platz_zum_hinzufuegen: int = anzahl_zeichen2 - len(liste_variation_auswahl) + 1
            if anzahl_variation == 1:
                anzahl_hinzuefuegen: int = anzahl_zeichen2
            else:
                anzahl_hinzuefuegen: int = random.randint(1, platz_zum_hinzufuegen)
            for j in range(anzahl_hinzuefuegen):
                idx2: int = random.randint(0, len(liste_variation_auswahl[idx]) - 1)
                zusammenstellung.append(liste_variation_auswahl[idx][idx2])
            if anzahl_variation > 1:
                liste_variation_auswahl.remove(liste_variation_auswahl[idx])
                anzahl_variation -= 1

        random.shuffle(zusammenstellung)
        passwort = "".join(zusammenstellung)
        entry_var1.set(passwort)
    if fehler_meldung:
        label4.grid(row=2, column=7, columnspan=2, sticky="ws")
    else:
        label4.grid_forget()


def input_pin_auslesen():
    global entry1_pin, entry2_pin, root_pin_setzen, entry_var1_pin, entry_var2_pin, user_daten, status_global, eingelogt
    input_pin1: str = entry1_pin.get()
    input_pin2: str = entry2_pin.get()
    if status_global == 1:
        if input_pin1 == input_pin2 and len(input_pin1) >= 8:
            root_pin_setzen.destroy()

            with open(resource_path("Speicher_Datein/user_data.txt"), "w", encoding="utf-8") as f2:
                f2.seek(0)
                f2.write(input_pin1)
                f2.flush()  # <-- ganz wichtig!
                f2.seek(0)
                user_daten.clear()

            with open(resource_path("Speicher_Datein/user_data.txt"), "r", encoding="utf-8") as f2:
                user_daten = f2.readline()
        else:
            entry_var1_pin.set("")
            entry_var2_pin.set("")
            # Errow Text wird angezeigt
            label_errow = customtkinter.CTkLabel(root_pin_setzen, text="Passwort mindest \nlänge 8 Zeichen.\n"
                                                                       "Überprüfen sie ihre\n Passwörter auf "
                                                                       "\nihre richtigkeit")
            label_errow.grid(row=4, column=10, rowspan=6, columnspan=2)
    elif status_global == 0:
        if input_pin1 == user_daten[0] == input_pin2:
            root_pin_setzen.destroy()
            eingelogt = True
        else:
            label_errow = customtkinter.CTkLabel(root_pin_setzen, text="Passwort nicht vorhanden!\n"
                                                                       "Überprüfen sie die Richtigkeit!")
            label_errow.grid(row=4, column=10, rowspan=6, columnspan=2)


def speichern():
    global passwort
    zweck: str = entry2_zweck.get()
    if passwort:
        label6.grid_forget()
        if not user_daten:
            pin_setzen(1)
        elif not zweck:
            label5.grid(row=10, column=5, columnspan=4, sticky="new")
        else:
            label5.grid_forget()
            label6.grid_forget()
            entry_var2.set("")
            f = "Speicher_Datein/data.txt"

            with open(resource_path(f), "a", encoding="utf-8") as f:
                f.write(f"{zweck}   {passwort}\n")
            daten.append(f"{zweck}   {passwort}\n")
    else:
        label6.grid(row=10, column=5, columnspan=4, sticky="new")


def slider_aktualisieren(wert):
    label1.configure(text=f"Passwortlänge: {int(wert)}")


def on_close():
    global eingelogt
    eingelogt = False
    root.destroy()


root = customtkinter.CTk()
root.title("KeyForge-Passwort Generierer")
root.geometry("400x400")

root.protocol("WM_DELETE_WINDOW", on_close)

entry_var1 = tk.StringVar()
entry_var2 = tk.StringVar()

root.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1, uniform="a")
root.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1, uniform="a")

# Benutzerflaeche erstellen
label2 = customtkinter.CTkLabel(root, text="Zeichenarten wählen:")
label3 = customtkinter.CTkLabel(root, text="Zweck des Passwortes:")
label4 = customtkinter.CTkLabel(root, text="Eine Kategorie wählen!")
label5 = customtkinter.CTkLabel(root, text="Kein Zweck vorhanden!")
label6 = customtkinter.CTkLabel(root, text="Kein Passwort vorhanden!")
var_chb1 = tk.BooleanVar()
var_chb2 = tk.BooleanVar()
var_chb3 = tk.BooleanVar()
var_chb4 = tk.BooleanVar()
chb1 = customtkinter.CTkCheckBox(root, text="Großbuchstaben", variable=var_chb1)
chb2 = customtkinter.CTkCheckBox(root, text="Kleinbuchstaben", variable=var_chb2)
chb3 = customtkinter.CTkCheckBox(root, text="Ziffern", variable=var_chb3)
chb4 = customtkinter.CTkCheckBox(root, text="Sonderzeichen", variable=var_chb4)

entry1_ausgabe = customtkinter.CTkEntry(root, textvariable=entry_var1)
entry2_zweck = customtkinter.CTkEntry(root, textvariable=entry_var2)

button1_erstellen = customtkinter.CTkButton(root, text="Passwort Generieren", command=erstellen)
button2_speichern = customtkinter.CTkButton(root, text="Passwort Speichern", command=speichern)
button3_gespeichertes = customtkinter.CTkButton(root, text="Gespeicherte \nPasswörter",
                                                command=gespeicherte_passwoerter)
button4_konto = customtkinter.CTkButton(root, text="Konto", command=konto)

regler = customtkinter.CTkSlider(root, from_=8, to=50, orientation=tk.HORIZONTAL, command=slider_aktualisieren)
regler.set(8)

label1 = customtkinter.CTkLabel(root, text="Passwortlänge: 8")
label1.grid(row=0, column=1, columnspan=4, sticky="esw")

# Grit
label2.grid(row=2, column=1, columnspan=4, sticky="esw")
label3.grid(row=8, column=5, columnspan=4, sticky="s")
chb1.grid(row=3, column=2, columnspan=5, sticky="w")
chb2.grid(row=4, column=2, columnspan=5, sticky="w")
chb3.grid(row=6, column=2, columnspan=3, sticky="w")
chb4.grid(row=5, column=2, columnspan=5, sticky="w")
button1_erstellen.grid(row=7, column=1, columnspan=4, sticky="nesw")
button2_speichern.grid(row=9, column=1, columnspan=4, sticky="nesw")
button3_gespeichertes.grid(row=0, column=8, columnspan=2, sticky="nesw")
button4_konto.grid(row=1, column=8, columnspan=2, sticky="nesw")
entry1_ausgabe.grid(row=7, column=5, columnspan=4, sticky="")
entry2_zweck.grid(row=9, column=5, columnspan=4, sticky="")
regler.grid(row=1, column=1, columnspan=6, sticky="new")

chb1.select()
chb2.select()
chb3.select()
chb4.select()
root.mainloop()
