import tkinter as tk
import random
import time

i = 1

def Idiot():
    
    def disable_event():
        pass

    time.sleep(5)
    window = tk.Tk()
    window.geometry("425x200")
    window.title("Sei un idiota?")
    window.resizable(False, False)
    window.configure(background="Black")

    def Close():
        window.destroy()

    l = tk.Label(window, text="Sei un idiota", font="Helvetica 24 bold", bg="Black", fg="White", padx="90px")
    l.grid(column=0, row=0)

    b = tk.Button(window, text="SI", command=Close, bg="Black", font="Helvetica 13 bold", fg="white", pady="5px", padx="5px")
    b.grid(column=0, row=1)

    b1 = tk.Button(window, text="NO", command=Close, bg="Black", font="Helvetica 13 bold", fg="white", pady="5px")
    b1.grid(column=0, row=2)

    if __name__ == "__main__":
        window.mainloop()

    time.sleep(45)
    
    for i in range(1,21):
        n = random.randint(1,2)

        # Versione con Sfondo Nero
        if n == 1:
            window = tk.Tk()
            window.geometry("425x200")
            window.title("Sei un idiota?")
            window.resizable(False, False)
            window.configure(background="Black")

            l = tk.Label(window, text="Sei un idiota", font="Helvetica 24 bold", bg="Black", fg="White", padx="90px")
            l.grid(column=0, row=0)

            b = tk.Button(window, text="SI", bg="Black", font="Helvetica 13 bold", fg="white", pady="5px")
            b.grid(column=0, row=1)

            b1 = tk.Button(window, text="SI", bg="Black", font="Helvetica 13 bold", fg="white", pady="5px")
            b1.grid(column=0, row=2)

            window.protocol("WM_DELETE_WINDOW", disable_event)

            if __name__ == "__main__":
                window.mainloop()

            time.sleep(60)

        # Versione Sfondo Bianco
        elif n == 2:
            window = tk.Tk()
            window.geometry("425x200")
            window.title("Sei un idiota?")
            window.resizable(False, False)
            window.configure(background="White")

            l = tk.Label(window, text="Sei un idiota", font="Helvetica 24 bold", bg="White", fg="Black", padx="90px")
            l.grid(column=0, row=0)

            b = tk.Button(window, text="SI", bg="White", font="Helvetica 13 bold", fg="Black", pady="5px")
            b.grid(column=0, row=1)

            b1 = tk.Button(window, text="SI", bg="White", font="Helvetica 13 bold", fg="Black", pady="5px")
            b1.grid(column=0, row=2)

            window.protocol("WM_DELETE_WINDOW", disable_event)

            if __name__ == "__main__":
                window.mainloop()

            time.sleep(60)

            i = i + 1
