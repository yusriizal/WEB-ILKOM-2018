import tkinter as tk
from PIL import ImageTk, Image

def priceBeautify(price):
    price = str(price)
    output = ""
    for i in range(len(price)-1, -1, -1):
        if(i != len(price)-1 and (len(price)-1 - i) % 3 == 0):
            output = "."+output
        output = price[i] + output
    return output

class BlankSpace(tk.Frame):
    def __init__(self, master, width=0, height=0, background=None):
        super().__init__(master, width=width, height=height)
        if background == None :
            self["background"] = master["background"]
        else :
            self["background"] = background

class Picture(tk.Label):
    def __init__(self, master, imgLoc, imgW, imgH, background):
        img = Image.open(imgLoc)
        img = img.resize((imgW, imgH), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        super().__init__(master, image=img, background=background)
        self.image = img

class Navbar(tk.Frame):
    def __init__(self, master, user, output, page):
        super().__init__(master, background="aquamarine", padx=20, pady=20, relief="solid", borderwidth=1)
        navBar = tk.Frame(self, background=self["background"])

        #logo
        logo = tk.Label(navBar, text="Siakad", fg="Black")
        logo["font"] = "courier 16 bold"
        logo["background"] = logo.master["background"]
        logo.pack(side="left")
        #logo end

        space = BlankSpace(navBar, width=30)
        space.pack(side="left")


        #profil-button

        def profileBtnClicked():
            output["action"] = "profile"
            output["data"] = user

            page.destroy()
            page.quit()

        profileBtn = tk.Button(navBar, text=user.getInfo()["username"], relief="groove", background="azure", fg="black", borderwidth=2,  cursor="hand2", command=profileBtnClicked, padx=5, pady=5)
        profileBtn["font"] = "courier 14"
        profileBtn.pack(side="right", fill="y")
        #profil-button end

        def Biodata():
            output["action"] = "Biodata"
            output["data"] = user

            page.destroy()
            page.quit()

        Biodata = tk.Button(navBar, text="Biodata", relief="groove", background="azure", fg="black",borderwidth=2, cursor="hand2", command=Biodata, padx=5, pady=5)
        Biodata["font"] = "courier 14"
        Biodata.pack(side="right", fill="y")
        #Biodata end

        #Krs
        def Krs():
            output["action"] = "Krs"
            output["data"] = user

            page.destroy()
            page.quit()

        Krs = tk.Button(navBar, text="Krs", relief="groove", background="azure", fg="black", borderwidth=2, cursor="hand2", command=Krs, padx=5, pady=5)
        Krs["font"] = "courier 14"
        Krs.pack(side="right", fill="y")
        #Krs end

        #Khs
        def Khs():
            output["action"] = "Khs"
            output["data"] = user

            page.destroy()
            page.quit()

        Khs = tk.Button(navBar, text="Khs", relief="groove", background="azure", fg="black", borderwidth=2, cursor="hand2", command=Khs, padx=5, pady=5)
        Khs["font"] = "courier 14"
        Khs.pack(side="right", fill="y")
        #Khs end
        navBar.pack(fill="x")
            
        
class PageBtns():
    def __init__(self):
        self.children = list()

    def append(self, newChild):
        self.children.append(newChild)

    def getChildren(self):
        return self.children

class PageBtn(tk.Button):
    def __init__(self, master, text, state, parent, page):
        if (state == "disabled"):
            super().__init__(master, text=text, state="disabled", relief="flat")
        else:
            super().__init__(master, text=text, cursor="hand2")
        self.parent = parent
        self.parent.append(self)
        self.page = page
        self["command"] = self.clicked
        if(state == "disabled"):
            self.disable()

    def disable(self):
        self["state"] = "disabled"
        self["cursor"] = ""
        self["relief"] = "flat"
        self.page.pack(expand=True, fill="both")

    def enable(self):
        self["state"] = "normal"
        self["cursor"] = "hand2"
        self["relief"] = "raised"
        self.page.pack_forget()

    def clicked(self):
        for i in self.parent.getChildren() :
            i.enable()
        self.disable()

class ProductCard(tk.Frame):
    def __init__(self, master, product, output, page):
        super().__init__(master, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        container = tk.Frame(self, background=self["background"])

        productImg = Picture(container, product.getInfo()["pic"], 150, 100, "white")
        productImg.pack(expand=True, fill="both")

        space = BlankSpace(container, height=5)
        space.pack(fill="x")

        productDesc = tk.Frame(container, background="white")

        productDescName = tk.Label(productDesc, text=product.getInfo()["name"], font="courier 10 bold", wraplength=250)
        productDescName["background"] = productDescName.master["background"]
        productDescName.pack(expand=True, fill="both")

        productDescPrice = tk.Label(productDesc, text="Rp"+priceBeautify(product.getInfo()["price"]), font="courier 14 bold", fg="blue")
        productDescPrice["background"] = productDescPrice.master["background"]
        productDescPrice.pack(expand=True, fill="both")

        detailBtn = tk.Button(productDesc, text="Detail", cursor="hand2", background="lightskyblue1", relief="flat", fg="white", font="courier 14 bold")
        def detailBtnClicked():
            output["action"] = "product-detail"
            output["data"] = product
            page.quit()
            page.destroy()

        detailBtn["command"] = detailBtnClicked
        detailBtn.pack(fill="x")

        productDesc.pack(fill="x")

        container.pack(expand=True, fill="both")