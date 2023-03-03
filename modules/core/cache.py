import db as DB
import hashlib
import base64
import time
import os

class CacheManager:
    
    def __init__(self) -> None:
        self.cache_dir  = "./cache/"
        self.hashing    = "sha1"
        self.max_age    = 60 #seconds
    
    def preserve(self, owner, data, type="string"):
        owner = eval("hashlib.{0}('{1}').hexdigest()".format(self.hashing, owner))
        stamp = time.time()
        try:
            open(self.cache_dir + owner + "/" + hashlib.md5(type).hexdigest(), "a").write(f"{stamp}::{base64.urlsafe_b64encode(data)}")
        except Exception:
            os.mkdir(self.cache_dir + owner)
        finally:
            open(self.cache_dir + owner + "/" + hashlib.md5(type).hexdigest(), "a").write(f"||{stamp}::{base64.urlsafe_b64encode(data)}")
        
        return True, stamp
            
    def terminate(self, owner, data, type):
        try:
            res = open(self.cache_dir + owner + "/" + hashlib.md5(type).hexdigest(), "r").read().split("||")
            stamp = [ x.split("::")[0] for x in res]
            res = [ x.split("::")[1] for x in res]
            loc = res.index(base64.urlsafe_b64encode(data))
            res.pop(loc)
            stamp.pop(loc)
            open(self.cache_dir + owner + "/" + hashlib.md5(type).hexdigest(), "w").write("")
            cache = open(self.cache_dir + owner + "/" + hashlib.md5(type).hexdigest(), "a")
            for x in range(len(res)):
                cache.write(f"||{stamp[x]}::{res[x]}")
        except ValueError or Exception:
            return False
        return True
    
    def grab(self, owner, data, type):
        try:
            res = open(self.cache_dir + owner + "/" + hashlib.md5(type).hexdigest(), "r").read().split("||")
            stamp = [ x.split("::")[0] for x in res]
            res = [ x.split("::")[1] for x in res]
            loc = res.index(base64.urlsafe_b64encode(data))
        except ValueError or Exception:
            return False
        return [base64.urlsafe_b64decode(res[loc]), stamp[loc]]