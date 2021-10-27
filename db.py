
class DB:
    FakeDB = {"myDB": [
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  }
]
}
    lock = False
    def __init__(self,recordID=None):
        self.recordID = recordID

    def searchRecordInDB(self,recordID):
        try:
            for record in DB.FakeDB["myDB"]:
                if record["id"] == recordID:
                    return record
            return None
        except Exception as e:
            print("Error while searching for record in DB: {}".format(e))
            return None


    def connectDB(self):
        pass

    def addRecordInDB(self,record):
        lock = True
        if record == None or record == "" or len(record) == 0:
            return False
        try:
            while lock:
                DB.FakeDB["myDB"].append(record)
                lock = False
            return True
        except Exception as e:
            print("Error while updating DB: {}".format(e))
            locak = False
            return False

    def deleteRecordInDB(self):
        pass

    def displayDBRecords(self):
        print("Entire record :")
        for record in DB.FakeDB["myDB"]:
            print(record)
"""
db = DB()
print(db.searchRecordInDB(1))
db.displayDBRecords()
record = {
    "userId": 1,
    "id": 4,
    "title": "This is a example title",
    "completed": False
  }
db.addRecordInDB(record)
db.displayDBRecords()
"""
