import tkinter as tk
import customGui
import math

class Guest:
    '''
        root:Tk
    '''
    def __init__(self, root):
        self.root = root

    def login(self, error):
        output = {
            "username" : "",
            "password" : "",
            "action" : ""
        }

        #GUI
        outerContainer = tk.Frame(self.root, background="snow")

        innerContainer = tk.Frame(outerContainer, background="aquamarine", padx=50, pady=50, relief="groove", borderwidth=2)

        loginLabel = tk.Label(innerContainer, text="Login Siakad", pady=10)
        loginLabel["background"] = loginLabel.master["background"]
        loginLabel["font"] = ("courier", 30)
        loginLabel.pack()

        usernameLabelContainer = tk.Frame(innerContainer)
        usernameLabelContainer["background"] = usernameLabelContainer.master["background"]
        usernameLabel = tk.Label(usernameLabelContainer, text="Username : ")
        usernameLabel["background"] = usernameLabel.master["background"]
        usernameLabel["font"] = ("courier", 16)
        usernameLabel.pack(side="left")
        usernameLabelContainer.pack(fill="x")

        usernameEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="groove", borderwidth=1)
        usernameEntry = tk.Entry(usernameEntryContainer, bd=0)
        usernameEntry["background"] = usernameEntry.master["background"]
        usernameEntry.pack(fill="x")
        usernameEntryContainer.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=20)
        space.pack(fill="x")

        passwordLabelContainer = tk.Frame(innerContainer)
        passwordLabelContainer["background"] = passwordLabelContainer.master["background"]
        passwordLabel = tk.Label(passwordLabelContainer, text="Password : ")
        passwordLabel["background"] = passwordLabel.master["background"]
        passwordLabel["font"] = ("courier", 16)
        passwordLabel.pack(side="left")
        passwordLabelContainer.pack(fill="x")

        passwordEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="groove", borderwidth=2)
        passwordEntry = tk.Entry(passwordEntryContainer, bd=0, show="*")
        passwordEntry["background"] = passwordEntry.master["background"]
        passwordEntry.pack(fill="x")
        passwordEntryContainer.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=5)
        space.pack(fill="x")

        errorLabel = tk.Label(innerContainer, text=error, fg="red")
        errorLabel["background"] = errorLabel.master["background"]
        errorLabel["font"] = ("courier", 12)
        errorLabel.pack()

        space = customGui.BlankSpace(innerContainer, height=5)
        space.pack(fill="x")

        loginBtn = tk.Button(innerContainer, background="azure", text="Login", relief="flat", fg="black", cursor="hand2")
        
        def loginBtnClicked():
            output["username"] = usernameEntry.get()
            output["password"] = passwordEntry.get()
            output["action"] = ""
            outerContainer.destroy()
            outerContainer.quit()

        loginBtn["command"] = loginBtnClicked

        loginBtn.pack(side="left")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        registerBtn = tk.Button(innerContainer, background="azure", text="Register", relief="flat", fg="black", cursor="hand2")
        
        def registerBtnClicked():
            output["username"] = ""
            output["password"] = ""
            output["action"] = "register"
            outerContainer.destroy()
            outerContainer.quit()

        registerBtn["command"] = registerBtnClicked
        
        registerBtn.pack(side="right")

        innerContainer.pack(expand=True)

        outerContainer.pack(expand=True, fill="both")
        outerContainer.mainloop()
        #GUI END

        return output

    def register(self, errorMsg):
        output = {
            "username" : "",
            "password" : "",
            "email" : "",
            "action" : ""
        }

        #GUI
        outerContainer = tk.Frame(self.root, background="snow")

        innerContainer = tk.Frame(outerContainer, background="aquamarine", padx=20, pady=20, relief="solid", borderwidth=1)

        container = tk.Frame(innerContainer)
        container["background"] = container.master["background"]
        
        def backBtnClicked():
            output["action"] = "login"
            outerContainer.destroy()
            outerContainer.quit()

        backBtn = tk.Button(container, text="<-Login", bd=1, command=backBtnClicked, background="gray", cursor="hand2")
        backBtn["background"] = backBtn.master["background"]
        backBtn.pack(side="left")
        
        container.pack(fill="x")

        registerLabel = tk.Label(innerContainer, text="Registrasi Siakad", pady=10)
        registerLabel["background"] = registerLabel.master["background"]
        registerLabel["font"] = ("courier", 30)
        registerLabel.pack()

        usernameLabelContainer = tk.Frame(innerContainer)
        usernameLabelContainer["background"] = usernameLabelContainer.master["background"]

        usernameLabel = tk.Label(usernameLabelContainer, text="Username : ")
        usernameLabel["background"] = usernameLabel.master["background"]
        usernameLabel["font"] = ("courier", 16)
        usernameLabel.pack(side="left")

        error = tk.Label(usernameLabelContainer, text=errorMsg["username"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")
        
        usernameLabelContainer.pack(fill="x")

        usernameEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        usernameEntry = tk.Entry(usernameEntryContainer, bd=0)
        usernameEntry["background"] = usernameEntry.master["background"]
        usernameEntry.pack(fill="x")
        usernameEntryContainer.pack(fill="x")

        passwordLabelContainer = tk.Frame(innerContainer)
        passwordLabelContainer["background"] = passwordLabelContainer.master["background"]

        passwordLabel = tk.Label(passwordLabelContainer, text="Password : ")
        passwordLabel["background"] = passwordLabel.master["background"]
        passwordLabel["font"] = ("courier", 16)
        passwordLabel.pack(side="left")

        error = tk.Label(passwordLabelContainer, text=errorMsg["password"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")

        passwordLabelContainer.pack(fill="x")

        passwordEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        passwordEntry = tk.Entry(passwordEntryContainer, bd=0, show="*")
        passwordEntry["background"] = passwordEntry.master["background"]
        passwordEntry.pack(fill="x")
        passwordEntryContainer.pack(fill="x")

        emailLabelContainer = tk.Frame(innerContainer)
        emailLabelContainer["background"] = emailLabelContainer.master["background"]

        emailLabel = tk.Label(emailLabelContainer, text="Email : ")
        emailLabel["background"] = emailLabel.master["background"]
        emailLabel["font"] = ("courier", 16)
        emailLabel.pack(side="left")

        error = tk.Label(emailLabelContainer, text=errorMsg["email"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")

        emailLabelContainer.pack(fill="x")

        emailEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        emailEntry = tk.Entry(emailEntryContainer, bd=0)
        emailEntry["background"] = emailEntry.master["background"]
        emailEntry.pack(fill="x")
        emailEntryContainer.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=20)
        space.pack(fill="x")

        registerBtn = tk.Button(innerContainer, background="azure", text="register", relief="flat", fg="black", cursor="hand2")
        
        def registerBtnClicked():
            output["username"] = usernameEntry.get()
            output["password"] = passwordEntry.get()
            output["email"] = emailEntry.get()
            outerContainer.destroy()
            outerContainer.quit()

        registerBtn["command"] = registerBtnClicked

        registerBtn.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        innerContainer.pack(expand=True)

        outerContainer.pack(expand=True, fill="both")
        outerContainer.mainloop()
        #GUI END

        return output
class User:
    def __init__(self, root):
        self.root = root

    def showProducts(self, data):
        output = {
            "action": None,
            "data": None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #must be edited 
        productLength = len(data["products"])
        pageNumbers = int(math.ceil(productLength / 10))
        #must be edited end

        #products list
        container = tk.Frame(body, padx=20, pady=5, background="white smoke")
        container["background"] = container.master["background"]

        pages = list()
        for h in range(pageNumbers):
            page = tk.Frame(container)
            page["background"] = page.master["background"]
            for i in range(10):
                if ( i % 5 == 0 ) :
                    row = tk.Frame(page)
                    row["background"] = row.master["background"]
                elif (i % 5 == 4 or i == 7):
                    row.pack(expand=True, fill="both")

                colBorder = tk.Frame(row, padx=5, pady=5)
                colBorder["background"] = colBorder.master["background"]

                if(10*h+i < productLength):
                    currentProductInfo = data["products"][10*h+i]

                    col = customGui.ProductCard(colBorder, currentProductInfo, output, body)
                    col.pack(expand=True, fill="both")
                
                colBorder.pack(side="left", fill="both", expand=True)

            pages.append(page)

        container.pack(expand=True, fill="both")
        #product list end

        #product list pages
        container = tk.Frame(body, pady=5)
        filler = tk.Frame(container)
        filler["background"] = filler.master["background"]
        filler.pack(side="left", expand=True)
        pageBtns = customGui.PageBtns()
        for i in range(pageNumbers):
            if(i == 0):
                pageBtn = customGui.PageBtn(container, str(i+1), "disabled", pageBtns, pages[i])
            else :
                pageBtn = customGui.PageBtn(container, str(i+1), "normal", pageBtns, pages[i])

            pageBtn.pack(side="left")

        filler = tk.Frame(container)
        filler["background"] = filler.master["background"]
        filler.pack(side="left", expand=True)
        container.pack(fill="x")
        #product list pages end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output

    def showProfile(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")


        editInfo = tk.Button(backBtn, text="User", font="courier 16 bold", fg="black", padx=20, pady=20, relief="flat", cursor="hand2")
        editInfo["background"] = editInfo.master["background"]
        editInfo.pack(side="right")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]

        #edit-information
        editInfoPage = tk.Frame(content)
        editInfoPage["background"] = editInfo.master["background"]

        #change-username
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeUsername = tk.Label(container, font="courier 16", text="Username : ", pady=10)
        labelChangeUsername["background"] = labelChangeUsername.master["background"]
        labelChangeUsername.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeUsernameError = tk.Label(container, font="courier 16", pady=10)
        labelChangeUsernameError["background"] = labelChangeUsernameError.master["background"]
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        changeUsernameEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        changeUsernameEntry.insert(0, data["user"].getInfo()["username"])
        changeUsernameEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-username end

        #change-email
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeEmail = tk.Label(container, font="courier 16", text="Email : ", pady=10)
        labelChangeEmail["background"] = labelChangeEmail.master["background"]
        labelChangeEmail.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeEmailError = tk.Label(container, font="courier 16", pady=10)
        labelChangeEmailError["background"] = labelChangeEmailError.master["background"]
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changeEmailEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        changeEmailEntry.insert(0, data["user"].getInfo()["email"])
        changeEmailEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-email end

        space = customGui.BlankSpace(editInfoPage, height=10)
        space.pack(fill="x")


        editInfoPage.pack(expand=True, fill="both")
        #edit-information end

        content.pack(side="left", expand=True, fill="both")

        mainPage.pack(expand=True, fill="both")

        border.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")
        #main-page end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output 

    def Biodata(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        editInfo = tk.Frame()
        editInfo["background"] = editInfo.master["background"]
        editInfo.pack(fill="x")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]

        #edit-information
        editInfoPage = tk.Frame(content)
        editInfoPage["background"] = editInfo.master["background"]

        #Biodata
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelBiodata = tk.Label(container, font="courier 16 bold", text="Biodata : ", pady=10)
        labelBiodata["background"] = labelBiodata.master["background"]
        labelBiodata.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelBiodata = tk.Label(container, font="courier 16", text="Nama : ", pady=5)
        labelBiodata["background"] = labelBiodata.master["background"]
        labelBiodata.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        BiodataEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        BiodataEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-username end

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelNoMahasiswa = tk.Label(container, font="courier 16", text="No Mahasiswa : ", pady=5)
        labelNoMahasiswa["background"] = labelNoMahasiswa.master["background"]
        labelNoMahasiswa.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        NoMahasiswaEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        NoMahasiswaEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelTTL = tk.Label(container, font="courier 16", text="TTL : ", pady=5)
        labelTTL["background"] = labelTTL.master["background"]
        labelTTL.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        TTLEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        TTLEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        #change-email
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelAlamat = tk.Label(container, font="courier 16", text="Alamat : ", pady=5)
        labelAlamat["background"] = labelAlamat.master["background"]
        labelAlamat.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        AlamatEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        AlamatEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-email end


        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelAgama = tk.Label(container, font="courier 16", text="Agama : ", pady=5)
        labelAgama["background"] = labelAgama.master["background"]
        labelAgama.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        AgamaEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        AgamaEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelNoHp = tk.Label(container, font="courier 16", text="No HP : ", pady=5)
        labelNoHp["background"] = labelNoHp.master["background"]
        labelNoHp.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        NoHpEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        NoHpEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        space = customGui.BlankSpace(editInfoPage, height=10)
        space.pack(fill="x")

        #save-change
        save = tk.Button(editInfoPage, font="courier 16 bold", background="azure", fg="black", text="Simpan", cursor="hand2")
        save.pack(side="right")
        #save-change end

        editInfoPage.pack(expand=True, fill="both")
        #edit-information end

        content.pack(side="left", expand=True, fill="both")

        mainPage.pack(expand=True, fill="both")

        border.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")
        #main-page end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output
        
    def Krs(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        Krs = tk.Label(backBtn, text="KRS", font="courier 16 bold", fg="black", padx=20, pady=5, relief="flat")
        Krs["background"] = Krs.master["background"]
        Krs.pack(side="right")
       
        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]
        
        container = tk.Frame(content)
        container["background"] = container.master["background"]
        
        lst = tk.Frame(container)
        lst["background"] = lst.master["background"]
        matakuliah=tk.Label(lst, relief="groove", font="courier 16", text="mata Kuliah", padx=10)
        matakuliah.pack(side="left", fill="both", expand=True)
        kodematakuliah=tk.Label(lst, relief="groove", font="courier 16", text="kode mata Kuliah", padx=10)
        kodematakuliah.pack(side="left", fill="both", expand=True)
        dosen=tk.Label(lst, relief="groove", font="courier 16", text="Dosen", padx=10)
        dosen.pack(side="left",fill="both", expand=True)
        Sks=tk.Label(lst, relief="groove", font="courier 16", text="SKS", padx=10)
        Sks.pack(side="left", fill="both", expand=True)
        lst.pack( fill="x")
        space = customGui.BlankSpace(container, height=10)
        space.pack(fill="y")
        tambah = tk.Button(container, font="courier 16 bold", background="Azure", fg="black", text="tambah", cursor="hand2")
        tambah.pack(fill="x", side="left")
        Simpan = tk.Button(container, font="courier 16 bold", background="Azure", fg="black", text="Simpan", cursor="hand2")
        Simpan.pack(fill="x", side="right")
        
        container.pack(expand=True, fill="both") 
        
        content.pack( expand=True, fill="both")
        
        mainPage.pack(expand=True, fill="both")
        
        border.pack(expand=True, fill="both")
        
        mainPageContainer.pack(expand=True, fill="both")

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output      

    def Khs(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        Khs = tk.Label(backBtn, text="KHS", font="courier 16 bold", fg="black", padx=20, pady=5, relief="flat")
        Khs["background"] = Khs.master["background"]
        Khs.pack(side="right")
       
        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]
        
        container = tk.Frame(content)
        container["background"] = container.master["background"]
        
        lst = tk.Frame(container)
        lst["background"] = lst.master["background"]
        matakuliah=tk.Label(lst, relief="groove", font="courier 16", text="mata Kuliah", padx=10)
        matakuliah.pack(side="left", fill="both", expand=True)
        kodematakuliah=tk.Label(lst, relief="groove", font="courier 16", text="kode mata Kuliah", padx=10)
        kodematakuliah.pack(side="left", fill="both", expand=True)
        dosen=tk.Label(lst, relief="groove", font="courier 16", text="Dosen", padx=10)
        dosen.pack(side="left",fill="both", expand=True)
        Sks=tk.Label(lst, relief="groove", font="courier 16", text="SKS", padx=10)
        Sks.pack(side="left", fill="both", expand=True)
        nilai=tk.Label(lst, relief="groove", font="courier 16", text="Nilai", padx=10)
        nilai.pack(side="left", fill="both", expand=True)
        lst.pack( fill="x")
        space = customGui.BlankSpace(container, height=10)
        space.pack(fill="y")
        
        container.pack(expand=True, fill="both") 
        
        content.pack( expand=True, fill="both")
        
        mainPage.pack(expand=True, fill="both")
        
        border.pack(expand=True, fill="both")
        
        mainPageContainer.pack(expand=True, fill="both")

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output
class Seller(User):
    def __init__(self, root):
        self.root = root

    def showProducts(self, data):
        output = {
            "action": None,
            "data": None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #must be edited 
        productLength = len(data["products"])
        pageNumbers = int(math.ceil(productLength / 10))
        #must be edited end

        #products list
        container = tk.Frame(body, padx=20, pady=5, background="white smoke")
        container["background"] = container.master["background"]

        pages = list()
        for h in range(pageNumbers):
            page = tk.Frame(container)
            page["background"] = page.master["background"]
            for i in range(10):
                if ( i % 5 == 0 ) :
                    row = tk.Frame(page)
                    row["background"] = row.master["background"]
                elif (i % 5 == 4 or i == 7):
                    row.pack(expand=True, fill="both")

                colBorder = tk.Frame(row, padx=5, pady=5)
                colBorder["background"] = colBorder.master["background"]

                if(10*h+i < productLength):
                    currentProductInfo = data["products"][10*h+i]

                    col = customGui.ProductCard(colBorder, currentProductInfo, output, body)
                    col.pack(expand=True, fill="both")
                
                colBorder.pack(side="left", fill="both", expand=True)

            pages.append(page)

        container.pack(expand=True, fill="both")
        #product list end

        #product list pages
        container = tk.Frame(body, pady=5)
        filler = tk.Frame(container)
        filler["background"] = filler.master["background"]
        filler.pack(side="left", expand=True)
        pageBtns = customGui.PageBtns()
        for i in range(pageNumbers):
            if(i == 0):
                pageBtn = customGui.PageBtn(container, str(i+1), "disabled", pageBtns, pages[i])
            else :
                pageBtn = customGui.PageBtn(container, str(i+1), "normal", pageBtns, pages[i])

            pageBtn.pack(side="left")

        filler = tk.Frame(container)
        filler["background"] = filler.master["background"]
        filler.pack(side="left", expand=True)
        container.pack(fill="x")
        #product list pages end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output

    def showProfile(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")


        editInfo = tk.Button(backBtn, text="User", font="courier 16 bold", fg="black", padx=20, pady=20, relief="flat", cursor="hand2")
        editInfo["background"] = editInfo.master["background"]
        editInfo.pack(side="right")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]

        #edit-information
        editInfoPage = tk.Frame(content)
        editInfoPage["background"] = editInfo.master["background"]

        #change-username
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeUsername = tk.Label(container, font="courier 16", text="Username : ", pady=10)
        labelChangeUsername["background"] = labelChangeUsername.master["background"]
        labelChangeUsername.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        changeUsernameEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        changeUsernameEntry.insert(0, data["user"].getInfo()["username"])
        changeUsernameEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-username end

        #change-email
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeEmail = tk.Label(container, font="courier 16", text="Email : ", pady=10)
        labelChangeEmail["background"] = labelChangeEmail.master["background"]
        labelChangeEmail.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changeEmailEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        changeEmailEntry.insert(0, data["user"].getInfo()["email"])
        changeEmailEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-email end

        space = customGui.BlankSpace(editInfoPage, height=10)
        space.pack(fill="x")


        editInfoPage.pack(expand=True, fill="both")
        #edit-information end

        content.pack(side="left", expand=True, fill="both")

        mainPage.pack(expand=True, fill="both")

        border.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")
        #main-page end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output 

    def Biodata(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        editInfo = tk.Frame()
        editInfo["background"] = editInfo.master["background"]
        editInfo.pack(fill="x")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]

        #edit-information
        editInfoPage = tk.Frame(content)
        editInfoPage["background"] = editInfo.master["background"]

        #Biodata
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelBiodata = tk.Label(container, font="courier 16 bold", text="Biodata : ", pady=10)
        labelBiodata["background"] = labelBiodata.master["background"]
        labelBiodata.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelBiodata = tk.Label(container, font="courier 16", text="Nama : ", pady=5)
        labelBiodata["background"] = labelBiodata.master["background"]
        labelBiodata.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        BiodataEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        BiodataEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-username end

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelNoMahasiswa = tk.Label(container, font="courier 16", text="No Mahasiswa : ", pady=5)
        labelNoMahasiswa["background"] = labelNoMahasiswa.master["background"]
        labelNoMahasiswa.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        NoMahasiswaEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        NoMahasiswaEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelTTL = tk.Label(container, font="courier 16", text="TTL : ", pady=5)
        labelTTL["background"] = labelTTL.master["background"]
        labelTTL.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        TTLEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        TTLEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        #change-email
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelAlamat = tk.Label(container, font="courier 16", text="Alamat : ", pady=5)
        labelAlamat["background"] = labelAlamat.master["background"]
        labelAlamat.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        AlamatEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        AlamatEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-email end


        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelAgama = tk.Label(container, font="courier 16", text="Agama : ", pady=5)
        labelAgama["background"] = labelAgama.master["background"]
        labelAgama.pack(side="left")
        container.pack(fill="x")

        

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        AgamaEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        AgamaEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelNoHp = tk.Label(container, font="courier 16", text="No HP : ", pady=5)
        labelNoHp["background"] = labelNoHp.master["background"]
        labelNoHp.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        NoHpEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        NoHpEntry.pack(fill="both", expand=True)
        container.pack(fill="x")

        space = customGui.BlankSpace(editInfoPage, height=10)
        space.pack(fill="x")

        editInfoPage.pack(expand=True, fill="both")
        #edit-information end

        content.pack(side="left", expand=True, fill="both")

        mainPage.pack(expand=True, fill="both")

        border.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")
        #main-page end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output
        
    def Krs(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        Krs = tk.Label(backBtn, text="KRS", font="courier 16 bold", fg="black", padx=20, pady=5, relief="flat")
        Krs["background"] = Krs.master["background"]
        Krs.pack(side="right")
       
        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]
        
        container = tk.Frame(content)
        container["background"] = container.master["background"]
        
        lst = tk.Frame(container)
        lst["background"] = lst.master["background"]
        matakuliah=tk.Label(lst, relief="groove", font="courier 16", text="mata Kuliah", padx=10)
        matakuliah.pack(side="left", fill="both", expand=True)
        kodematakuliah=tk.Label(lst, relief="groove", font="courier 16", text="kode mata Kuliah", padx=10)
        kodematakuliah.pack(side="left", fill="both", expand=True)
        dosen=tk.Label(lst, relief="groove", font="courier 16", text="Dosen", padx=10)
        dosen.pack(side="left",fill="both", expand=True)
        Sks=tk.Label(lst, relief="groove", font="courier 16", text="SKS", padx=10)
        Sks.pack(side="left", fill="both", expand=True)
        lst.pack( fill="x")
        space = customGui.BlankSpace(container, height=10)
        space.pack(fill="y")
        tambah = tk.Button(container, font="courier 16 bold", background="Azure", fg="black", text="input", cursor="hand2")
        tambah.pack(fill="x", side="left")
        Simpan = tk.Button(container, font="courier 16 bold", background="Azure", fg="black", text="Simpan", cursor="hand2")
        Simpan.pack(fill="x", side="right")
        
        container.pack(expand=True, fill="both") 
        
        content.pack( expand=True, fill="both")
        
        mainPage.pack(expand=True, fill="both")
        
        border.pack(expand=True, fill="both")
        
        mainPageContainer.pack(expand=True, fill="both")

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output      

    def Khs(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #Home-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Home", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #Home-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        Khs = tk.Label(backBtn, text="KHS", font="courier 16 bold", fg="black", padx=20, pady=5, relief="flat")
        Khs["background"] = Khs.master["background"]
        Khs.pack(side="right")
       
        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]
        
        container = tk.Frame(content)
        container["background"] = container.master["background"]
        
        lst = tk.Frame(container)
        lst["background"] = lst.master["background"]
        matakuliah=tk.Label(lst, relief="groove", font="courier 16", text="mata Kuliah", padx=10)
        matakuliah.pack(side="left", fill="both", expand=True)
        kodematakuliah=tk.Label(lst, relief="groove", font="courier 16", text="kode mata Kuliah", padx=10)
        kodematakuliah.pack(side="left", fill="both", expand=True)
        dosen=tk.Label(lst, relief="groove", font="courier 16", text="Dosen", padx=10)
        dosen.pack(side="left",fill="both", expand=True)
        Sks=tk.Label(lst, relief="groove", font="courier 16", text="SKS", padx=10)
        Sks.pack(side="left", fill="both", expand=True)
        nilai=tk.Label(lst, relief="groove", font="courier 16", text="Nilai", padx=10)
        nilai.pack(side="left", fill="both", expand=True)
        lst.pack( fill="x")
        space = customGui.BlankSpace(container, height=10)
        space.pack(fill="y")
        Input = tk.Button(container, font="courier 16 bold", background="Azure", fg="black", text="Input", cursor="hand2")
        Input.pack(fill="x", side="left")
        Simpan = tk.Button(container, font="courier 16 bold", background="Azure", fg="black", text="Simpan", cursor="hand2")
        Simpan.pack(fill="x", side="right")
        
        container.pack(expand=True, fill="both") 
        
        content.pack( expand=True, fill="both")
        
        mainPage.pack(expand=True, fill="both")
        
        border.pack(expand=True, fill="both")
        
        mainPageContainer.pack(expand=True, fill="both")

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output


class Mahasiswa(User):
    def __init__(self, root):
        super().__init__(root)

    def showProductDetail(self, data):
        output = {
            "action" : None,
            "data" : None
        }
    

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #product-detail

        #product-detail end

        body.pack(expand=True, fill="both")
        body.mainloop()
    
        #GUI END

        return output

class Admin(Seller):
    def __init__(self, root):
        super().__init__(root)

    def showProfile(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = tk.Button(backBtn, cursor="hand2", text="\u2190 Back", font="courier 16 bold")
        btn["background"] = btn.master["background"]

        def backBtnClicked():
            output["action"] = "search-back"
            body.quit()
            body.destroy()

        btn["command"] = backBtnClicked

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(body, padx=20, pady=5)
        border = tk.Frame(mainPageContainer, padx=1, pady=1, background="black")

        mainPage = tk.Frame(border, background="white")

        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        editInfo = tk.Button(lst, text="Edit Information", font="courier 16 bold", padx=20, pady=20, relief="flat", disabledforeground="black", anchor="w")
        editInfo["background"] = editInfo.master["background"]
        editInfo.pack(fill="x")

        changePassword = tk.Button(lst, text="Change Password", font="courier 16 bold", padx=20, pady=20, relief="flat",disabledforeground="black", anchor="w")
        changePassword["background"] = changePassword.master["background"]
        changePassword.pack(fill="x")

        logout = tk.Button(lst, text="Log Out", font="courier 16 bold", padx=20, pady=20, relief="flat", cursor="hand2", disabledforeground="black", fg="black", anchor="w")
        logout["background"] = logout.master["background"]
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        content = tk.Frame(mainPage, padx=20, pady=20)
        content["background"] = content.master["background"]

        #edit-information page
        editInfoPage = tk.Frame(content)
        editInfoPage["background"] = editInfo.master["background"]

        #change-username
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeUsername = tk.Label(container, font="courier 16", text="Username : ", pady=10)
        labelChangeUsername["background"] = labelChangeUsername.master["background"]
        labelChangeUsername.pack(side="left")

        labelChangeUsernameError = tk.Label(container, font="courier 16", pady=10, fg="red")
        labelChangeUsernameError["background"] = labelChangeUsernameError.master["background"]
        labelChangeUsernameError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        changeUsernameEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        changeUsernameEntry.insert(0, data["user"].getInfo()["username"])
        changeUsernameEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-username end

        #change-email
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeEmail = tk.Label(container, font="courier 16", text="Email : ", pady=10)
        labelChangeEmail["background"] = labelChangeEmail.master["background"]
        labelChangeEmail.pack(side="left")

        labelChangeEmailError = tk.Label(container, font="courier 16", pady=10, fg="red")
        labelChangeEmailError["background"] = labelChangeEmailError.master["background"]
        labelChangeEmailError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changeEmailEntry = tk.Entry(container, font="courier 16", background="white", bd=0)
        changeEmailEntry.insert(0, data["user"].getInfo()["email"])
        changeEmailEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-email end

        space = customGui.BlankSpace(editInfoPage, height=10)
        space.pack(fill="x")

        #save-change
        def saveInfoClicked():
            labelChangeUsernameError["text"] = data["user"].setUsername(changeUsernameEntry.get())
            labelChangeEmailError["text"] = data["user"].setEmail(changeEmailEntry.get())

        saveInfo = tk.Button(editInfoPage, font="courier 16 bold", background="lightskyblue1", fg="white", text="Save Edit", cursor="hand2", command=saveInfoClicked)
        saveInfo.pack(fill="x", side="bottom")
        #save-change end

        editInfoPage.pack(expand=True, fill="both")
        #edit-information page end

        #change-password page
        changePasswordPage = tk.Frame(content)
        changePasswordPage["background"] = changePasswordPage.master["background"]
        
        #old-password
        container = tk.Frame(changePasswordPage)
        container["background"] = container.master["background"]
        labelOldPassword = tk.Label(container, text="Old Password : ", pady=10, font="courier 16")
        labelOldPassword["background"] = labelOldPassword.master["background"]
        labelOldPassword.pack(side="left")

        labelOldPasswordError = tk.Label(container, fg="red", pady=10, font="courier 16")
        labelOldPasswordError["background"] = labelOldPasswordError.master["background"]
        labelOldPasswordError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(changePasswordPage, relief="solid", borderwidth=1, pady=5, padx=5, background="white")
        oldPasswordEntry = tk.Entry(container, bd=0, font="courier 16", show="*")
        oldPasswordEntry["background"] = oldPasswordEntry.master["background"]
        oldPasswordEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #old-password end

        #new-password
        container = tk.Frame(changePasswordPage)
        container["background"] = container.master["background"]
        labelNewPassword = tk.Label(container, text="New Password : ", pady=10, font="courier 16")
        labelNewPassword["background"] = labelNewPassword.master["background"]
        labelNewPassword.pack(side="left")

        labelNewPasswordError = tk.Label(container, fg="red", pady=10, font="courier 16")
        labelNewPasswordError["background"] = labelNewPasswordError.master["background"]
        labelNewPasswordError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(changePasswordPage, relief="solid", borderwidth=1, pady=5, padx=5, background="white")
        newPasswordEntry = tk.Entry(container, bd=0, font="courier 16", show="*")
        newPasswordEntry["background"] = newPasswordEntry.master["background"]
        newPasswordEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #new-password end

        #confirm-new-password
        container = tk.Frame(changePasswordPage)
        container["background"] = container.master["background"]
        labelConfirmNewPassword = tk.Label(container, text="Confirm New Password : ", pady=10, font="courier 16")
        labelConfirmNewPassword["background"] = labelConfirmNewPassword.master["background"]
        labelConfirmNewPassword.pack(side="left")

        labelConfirmNewPasswordError = tk.Label(container, fg="black", pady=10, font="courier 16")
        labelConfirmNewPasswordError["background"] = labelConfirmNewPasswordError.master["background"]
        labelConfirmNewPasswordError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(changePasswordPage, relief="solid", borderwidth=1, pady=5, padx=5, background="white")
        confirmNewPasswordEntry = tk.Entry(container, bd=0, font="courier 16", show="*")
        confirmNewPasswordEntry["background"] = confirmNewPasswordEntry.master["background"]
        confirmNewPasswordEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #confirm-new-password end

        #save-change
        def saveChangePasswordClicked():
            labelOldPasswordError["text"] = ""
            labelConfirmNewPasswordError["text"] = ""
            labelNewPasswordError["text"] = ""

            error = False
            if(oldPasswordEntry.get() != data["user"].getInfo()["password"]):
                labelOldPasswordError["text"] = "*Wrong Password"
                error = True
            if(newPasswordEntry.get() != confirmNewPasswordEntry.get()):
                labelConfirmNewPasswordError["text"] = "*Not Match"
                error = True

            if(not error):
                labelNewPasswordError["text"] = data["user"].setPassword(newPasswordEntry.get())

        saveChangePassword = tk.Button(changePasswordPage, font="courier 16 bold", background="lightskyblue1", fg="white", text="Save Edit", cursor="hand2", command=saveChangePasswordClicked)
        saveChangePassword.pack(fill="x", side="bottom")
        #save-change end
        #change-password page end 
        
        content.pack(side="left", expand=True, fill="both")

        mainPage.pack(expand=True, fill="both")

        border.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")
        #main-page end

        #state-management
        def editInfoClicked():
            changePasswordPage.pack_forget()

            editInfo["state"] = "disabled"
            editInfo["background"] = "white"
            editInfo["cursor"] = ""

            changePassword["state"] = "normal"
            changePassword["background"] = "white"
            changePassword["cursor"] = "hand2"

            editInfoPage.pack(fill="both", expand=True)

        def changePasswordClicked():
            editInfoPage.pack_forget()

            changePassword["state"] = "disabled"
            changePassword["background"] = "#f0f0f0"
            changePassword["cursor"] = ""
            editInfo["state"] = "normal"
            editInfo["background"] = "white"
            editInfo["cursor"] = "hand2"

            changePasswordPage.pack(fill="both", expand=True)


            changePassword["state"] = "normal"
            changePassword["background"] = "white"
            changePassword["cursor"] = "hand2"
            editInfo["state"] = "normal"
            editInfo["cursor"] = "hand2"
            editInfo["background"] = "white"

        def logoutClicked():
            body.quit()
            body.destroy()

        editInfo["command"] = editInfoClicked
        changePassword["command"] = changePasswordClicked
        logout["command"] = logoutClicked
        #state-management end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output
    