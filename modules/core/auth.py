from __main__ import *
import db as DB
import hashlib
import uuid
import time

class AuthManager:
    
    def __init__(self, user, pwd, email=None, remember=False) -> None:
        self.username   = user
        self.password   = pwd
        self.email      = email
        self.rem        = remember
    
    def Authenticate(self):
        c = DB.AuthDB.cursor()
        c.execute("SELECT id FROM users WHERE user = %s AND pass = %s", (self.username, self.password))
        res = c.fetchone()
        
        if res == None:
            return False
        
        if self.rem:
            return res, uuid.uuid1()
        
        return res
    
    def Create(self):
        if self.email == None: return False
        
        c = DB.AuthDB.cursor()
        c.execute("INSERT INTO users (id, email, user, pass, date) VALUES (%s, %s, %s, %s, %s)", (str(uuid.uuid4(), self.email, self.username, hashlib.sha256(self.password).hexdigest(), str(time.time()))))
        DB.AuthDB.commit()
        return True
    
    def Delete(self, id):
        c = DB.AuthDB.cursor()
        c.execute("DELETE FROM users WHERE id = %s ANDuser = %s AND pass = %s", (id, self.username, self.password))
        DB.AuthDB.commit()
        return True

def URL():
    A = AuthManager(request.form["username"], request.form["password"], email=request.form["email"])
    if A.Authenticate():
        return redirect(url_for("Home", auth=A.Authenticate()))
    return redirect(url_for("Home"))
            
    