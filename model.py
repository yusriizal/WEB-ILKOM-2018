import redis

class User:
    '''
        username:string
        password:string
        email:string
        role:string
    '''
    def __init__(self, username, password, email, role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.col = redis.redis-cly()["Siakad"]["user"]

    def getInfo(self):
        return {
            "username": self.username, 
            "password" : self.password,
            "email": self.email, 
            "role": self.role
        }
    
    def setUsername(self, newUsername):
        if(len(newUsername) < 8 or len(newUsername) > 20):
            return "*Username Must 8 to 20 Characters Long"
        if(len(list(self.col.find({"username" : newUsername}))) == 1):
            return "*Username is Already Used"
        
        self.col.update_one({
            "username" : self.username
        }, {
            "$set" : {
                "username" : newUsername
            }
        })

        self.username = newUsername
        return ""

    def setPassword(self, newPassword):
        if(len(newPassword) < 8):
            return "Password Must More Than 8 Characters Long"

        self.col.update_one({
            "username" : self.username
        }, {
            "$set" : {
                "password" : newPassword
            }
        })

        return ""

    def setEmail(self, newEmail):
        if(len(list(self.col.find({"email" : newEmail}))) == 1):
            return "*Email is Already Used"

        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "email" : newEmail
            }
        })
        self.email = newEmail
        return ""

    def setRole(self, newRole):
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "role" : newRole
            }
        })
        self.role = newRole