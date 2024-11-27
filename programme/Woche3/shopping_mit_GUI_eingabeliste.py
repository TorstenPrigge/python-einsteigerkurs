import os
import pandas as pd
from tkinter import Tk, Label, Button, Listbox, Scrollbar, MULTIPLE, END

def lese_datei(dateiname):
    try:
        df = pd.read_excel(dateiname)
        inhalte = df.iloc[:, 0].tolist()
        return inhalte
    except FileNotFoundError:
        print(f"Die Datei {dateiname} wurde nicht gefunden.")
        return []
    except IOError:
        print(f"Ein Fehler ist beim Lesen der Datei {dateiname} aufgetreten.")
        return []

def speichere_einkaufsliste(items, dateiname):
    """
    Speichert die ausgewählten Artikel in eine Excel-Datei.
    """
    try:
        df = pd.DataFrame(items, columns=["Einkaufsliste"])
        df.to_excel(dateiname, index=False)
        print(f"Einkaufsliste in {dateiname} gespeichert.")
    except IOError:
        print(f"Fehler beim Speichern der Datei {dateiname}.")

def gui_shopping_list(input_filename, source_filename):
    def add_selected_items():
        selected_indices = listbox_source.curselection()
        selected_items = [listbox_source.get(i) for i in selected_indices]
        for item in selected_items:
            if item not in shopping_list:  # Duplikate vermeiden
                shopping_list.append(item)
                listbox_shopping.insert(END, item)

    def save_and_exit():
        speichere_einkaufsliste(shopping_list, input_filename)
        root.destroy()

    # GUI erstellen
    root = Tk()
    root.title("Einkaufsliste erstellen")

    # Werkzeugquelle anzeigen
    Label(root, text="Verfügbare Artikel (Quelle):").grid(row=0, column=0, padx=10, pady=5)
    listbox_source = Listbox(root, selectmode=MULTIPLE, width=50, height=15)
    scrollbar_source = Scrollbar(root, command=listbox_source.yview)
    listbox_source.config(yscrollcommand=scrollbar_source.set)
    listbox_source.grid(row=1, column=0, padx=10, pady=5)
    scrollbar_source.grid(row=1, column=1, sticky="ns", pady=5)

    # Artikel aus der Quelle laden
    for item in lese_datei(source_filename):
        listbox_source.insert(END, item)

    # Einkaufsliste anzeigen
    Label(root, text="Einkaufsliste:").grid(row=0, column=2, padx=10, pady=5)
    listbox_shopping = Listbox(root, width=50, height=15)
    scrollbar_shopping = Scrollbar(root, command=listbox_shopping.yview)
    listbox_shopping.config(yscrollcommand=scrollbar_shopping.set)
    listbox_shopping.grid(row=1, column=2, padx=10, pady=5)
    scrollbar_shopping.grid(row=1, column=3, sticky="ns", pady=5)

    # Buttons
    Button(root, text="Auswahl hinzufügen", command=add_selected_items).grid(row=2, column=0, columnspan=2, pady=10)
    Button(root, text="Speichern und Beenden", command=save_and_exit).grid(row=2, column=2, columnspan=2, pady=10)

    # Einkaufsliste initialisieren
    shopping_list = []

    root.mainloop()

# Verzeichnis und Dateinamen für die Eingabe- und Quell-Dateien
verzeichnis = "./programme/Woche3/"
dateiname_eingabe = os.path.join(verzeichnis, "raw_shopping_list.xlsx")
dateiname_quelle = os.path.join(verzeichnis, "Werkzeugquelle.xlsx")

# GUI zur Bearbeitung der Einkaufsliste anzeigen
gui_shopping_list(dateiname_eingabe, dateiname_quelle)


