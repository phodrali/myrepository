import psycopg2

class DB:
    lock = False
    def __init__(self,recordID=None):
        self.recordID = recordID
        self.cursor = None
        self.conn = None

    def convertIntoReadable(sefl,record):
        if len(record) < 3:
            return None
        new_record = {"id": record[0], "userId": record[1], "title": record[2], "completed": record[3] }
        return new_record

    def searchRecordInDB(self,recordID):
        try:
            query = "select * from myDB where id = "+str(recordID)
            self.cursor.execute(query)
            if self.cursor.rowcount == 0:
                return None
            record = self.convertIntoReadable(self.cursor.fetchone())
            return record

        except Exception as e:
            print("Error while searching for record in DB: {}".format(e))
            return None


    def connectDB(self):
        try:
            print("Connecting to db test")
            conn = psycopg2.connect(
                     database="test", user='test', password='test', host='127.0.0.1', port= '5432'
                   )
            self.cursor = conn.cursor()
            self.conn = conn
            return True
        except Exception as e:
            print("Error while trying to connect to DB {}".format(e))
            return False

    def addRecordInDB(self,record):
        DB.lock = True
        if record == None or record == "" or len(record) == 0:
            return False
        try:

            query = "INSERT INTO myDB (id,userid,title,completed) VALUES (" + str(record['id'])+","+ str(record['userId'])+",\'"+record["title"]+"\',"+str(record["completed"])+ ")"
            print(query)
            while DB.lock:
                self.cursor.execute(query)
                self.conn.commit()
                print( self.cursor.statusmessage)
                DB.lock = False
            return True
        except Exception as e:
            print("Error while updating DB: {}".format(e))
            DB.lock = False
            return False

    def deleteRecordInDB(self, recordID):
        DB.lock = True
        try:
            query: "DELETE FROM myDB where id = "+str(recordID)
            print(query)
            while DB.lock:
                self.cursor.execute(query)
                self.conn.commit()
                print( self.cursor.statusmessage)
                DB.lock = False
            return True
        except Exception as e:
            print("Error while deleting DB: {}".format(e))
            DB.lock = False
            return False

    def displayDBRecords(self):
        DB.lock = True
        try:
            query: "SELECT * FROM myDB "
            print(query)
            while DB.lock:
                self.cursor.execute(query)
                for i, record in enum(self.cursor):
                    print(self.convertIntoReadable(record))
                DB.lock = False
            return True
        except Exception as e:
            print("Error while displaying in DB: {}".format(e))
            DB.lock = False
            return False

    def disconnectDB(self):
        print("Disconnecting from db test")
        self.conn.close()
"""
db = DB()
record = {
    "userId": 2,
    "id": 5,
    "title": "This is a example title",
    "completed": False
  }
db = DB()
db.connectDB()
print(db.addRecordInDB(record))
print(db.searchRecordInDB(5))
db.disconnectDB()
"""

