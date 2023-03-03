import db as DB

class DocDatabase:
    
    def __init__(self, coll) -> None:
        self.database   = DB.DocDB
        self.collection = coll
    
    def Insert(self, data, single=True):
        if single:
            res = self.database[self.collection].insert_one(data)
        else:
            res = self.database[self.collection].insert_many(data)
        return res.acknowledged
    
    def Find(self, query, single=False):
        if single:
            res = self.database[self.collection].find_one(query)
        else:
            res = self.database[self.collection].find(query)
        return res
    
    def Update(self, query, data, req=False):
        if req:
            res = self.database[self.collection].update_many(data, query)
        else:
            res = self.database[self.collection].update_one(data, query)
        return res.modified_count
    
    def Delete(self, query, req=False):
        if req:
            res = self.database[self.collection].delete_many(query)
        else:
            res = self.database[self.collection].delete_one(query)