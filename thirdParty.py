import requests
import json

class ThirdParty:

    def getTodos(self,recordID):
        url = "https://jsonplaceholder.typicode.com/todos/"+str(recordID)
        print(url)
        response = requests.get(url)
        if response.status_code != 200:
            print("Could not fetch details from the third party")
            return [False, ""]
        record = response.content
        if type(record) == bytes:
            record = record.decode('utf-8')
        res = json.loads(record)
        return [True,res]
"""
tp = ThirdParty()
tp.getTodos(7)
"""

