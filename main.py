import tkinter as tk
import controller

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Siakad")

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(str(w)+"x"+str(h))

    while True :
        guest = controller.Guest(root)
        user = guest.login()
        user.showProfile()

    root.mainloop()
