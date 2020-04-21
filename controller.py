import redis
import model
import view

class Guest:
    def __init__(self, root):
        self.view = view.Guest(root)
        self.col = redis.redis-cly()["Siakad"]["user"]
        self.root = root

    def login(self):
        error = ""

        while(True):
            data = self.view.login(error)
            error = ""
            if(data["action"] == "register"):
                self.register()
                continue
                
            result = list(self.col.find({"username":data["username"], "password":data["password"]}))

            if(len(result) > 0):
                if result[0]["role"] == "Admin":
                    return Admin(result[0]["username"], result[0]["password"], result[0]["email"], self.root)
                    
                return Admin(result[0]["username"], result[0]["password"], result[0]["email"], self.root)
            
            error = "*Username or Password is Invalid"

    def register(self):
        errorMsg = {
                "username":"",
                "password":"",
                "email": ""
            }
        while(True):
            error = False
            data = self.view.register(errorMsg)
            errorMsg = {
                "username":"",
                "password":"",
                "email": ""
            }

            if(data["action"] == "login"):
                return
            
            if(len(list(self.col.find({"username":data["username"]}))) > 0):
                errorMsg["username"] = "*Username is Already Used"
                error = True
            elif(len(data["username"]) < 8 or len(data["username"]) > 20):
                errorMsg["username"] = "*Username Length Only 8-20 Characters"
                error = True

            if(len(data["password"]) < 8 or len(data["password"]) > 20):
                errorMsg["password"] = "*Password Length Only 8-20 Characters"
                error = True

            if(len(list(self.col.find({"email":data["email"]}))) > 0):
                errorMsg["email"] = "*Email is Already Used"
                error = True
            elif(len(data["email"]) == 0):
                errorMsg["email"] = "*Email Cannot be Empty"
                error = True

            if(not error):
                self.col.insert_one({
                    "username" : data["username"],
                    "password" : data["password"],
                    "email" : data["email"],
                    "role" : "Mahasiswa"
                })
                self.login()
                return

class User:
    def __init__(self, view, model, root):
        self.client = redis.redis-cly()["Siakad"]
        self.view = view
        self.model = model
        self.root = root
        self.recentSearch = ""

    def executeResult(self, result):
        if(result["action"] == "profile"):
            self.showProfile()
        elif(result["action"] == "Biodata"):
            self.Biodata()
        elif(result["action"] == "Krs"):
            self.Krs()
        elif(result["action"] == "Khs"):
            self.Khs()

 
    def showProfile(self):
        data = {"user" : self.model}
        result = self.view.showProfile(data)
        self.executeResult(result)
        
    def Biodata(self):
        data = {"user" : self.model}
        result = self.view.Biodata(data)
        self.executeResult(result)
    def Krs(self):
        data = {"user" : self.model}
        result = self.view.Krs(data)
        self.executeResult(result)
    def Khs(self):
        data = {"user" : self.model}
        result = self.view.Khs(data)
        self.executeResult(result)

class Seller(User):
    def __init__(self, view, model, root):
        super().__init__(view, model, root)

class Admin(Seller):
    def __init__(self, username, password, email, root):
        super().__init__(view.Admin(root), model.User(username, password, email, "Admin"), root)

class Mahasiswa(User):
    def __init__(self, username, password, email, root):
        super().__init__(view.Mahasiswa(root), model.User(username, password, email, "Mahasiswa"), root)

