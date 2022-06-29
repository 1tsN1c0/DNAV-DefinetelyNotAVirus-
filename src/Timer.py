# Documento creato il 27/06/2022
import time
import tkinter as tk

def Timer():
    timer = 3000

    while timer != 0:
        timer = timer - 1
        time.sleep(1)

    if timer == 0:
        window = tk.Tk()
        window.geometry("400x200")
        window.title("Attenzione!")
        window.resizable(False, False)
        window.configure(background="#d7d6d7")

        l = tk.Label(window, text="I tuoi file sono stati cryptati e non potranno \n più essere recuperati!", font=("Helvetica 14 bold"), bg="#d7d6d7")
        l.grid(column=0, row=0)

        l1 = tk.Label(window, text="- @1tsN1c0", font=("Helvetica 14 italic"), bg="#d7d6d7")
        l1.grid(column=0, row=1)

        if __name__ == "__main__":
            window.mainloop()
