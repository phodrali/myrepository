from db import DB
from thirdParty import ThirdParty

class Todo:
    def __init__(self,recordID):
        self.recordID = recordID

    def getRecordFromDB(self):
        db = DB()
        record = db.searchRecordInDB(self.recordID)
        return record

    def getRecordFromThirdParty(self):
        tp = ThirdParty()
        record = tp.getTodos(self.recordID)
        if not record[0]:
            print("Failed to get record from thrid party api")
            return [False, {}]
        if len(record[1]) == 0:
            print("Record is not found in the third party")
            return [False, {}]
        db = DB()
        res = db.addRecordInDB(record[1])
        if not res:
            print("Failed to add the record in DB but record is available from third party")
        print("Successfully added record in DB")
        return [True,record[1]]


    def getTodo(self):
        print("Getting todos from the DB for id {}".format(self.recordID))
        record = self.getRecordFromDB()
        if record == None:
            print("Could not find the todos for id {} from DB".format(self.recordID))
            print("Getting todos for id {} from thirdparty ".format(self.recordID))
            record = self.getRecordFromThirdParty()
            if not record[0]:
                print("Could not find the todos from the thirdparty for id: {}".format(self.recordID))
                return {"statue": 404, "content": {}}
            record = record[1]
        return {"status": 200, "content": record }
