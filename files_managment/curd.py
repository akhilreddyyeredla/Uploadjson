
import database_conn
class Mongo_opp():
    def __init__(self):
        pass
    def insert_data(self,data):
        try:
            json_data = []
            for i in data:
                json_data.append(data[i])
            database_conn.connection().insert_many(json_data)
            response = {"status": "success", "code": 200,
                        "message": "Data Updated Sucessfully",

                        }
            return response
        except Exception as e:
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while inserting to database"
                        }

            return response

    def get_data(self,symbol):
        try:
            res = database_conn.connection().find({"symbol":symbol})
            response_data = []
            for doc in res:
                response_data.append(doc)
            response = {"status": "success", "code": 200,
                        "message": "Data Fetched Sucessfully",
                        "data" : response_data
                        }
            return response
        except Exception as e:
            print(e)
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while Fetching from database"
                        }

            return response


    def update_data_db(self,symbol,data):
        try:
            filter = {"symbol":symbol}
            updata_values = data
            res = database_conn.connection().update_one(filter,updata_values)
            response = {"status": "success", "code": 200,
                        "message": "Data Fetched Sucessfully",
                        "data" : updata_values
                        }
            return response
        except Exception as e:
            print(e)
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while updating to database"
                        }

            return response
