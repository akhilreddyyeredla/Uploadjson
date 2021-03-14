from app import app
from files_managment import curd
from flask import request
from flask import json,jsonify


@app.route("/upload-json",methods=['POST'])
def upload_json():
    json_data = {}
    image_file = request.files['json_file']
    file_name = "curl.json"
    image_file.save('/tmp/'+str(file_name))
    file_path = '/tmp/'+str(file_name)
    with open(file_path) as f:
        data = json.load(f)
    mongo_obj = curd.Mongo_opp()
    response = mongo_obj.insert_data(data)
    return jsonify(response)


@app.route("/get-data",methods=['GET'])
def get_data():
    symbol = request.args.get('symbol')
    mongo_obj = curd.Mongo_opp()
    respose = mongo_obj.get_data(symbol)
    return respose

@app.route("/update-data",methods=['POST'])
def update():
    symbol = request.args.get('symbol')
    data = request.get_json(force = True)
    mongo_obj = curd.Mongo_opp()
    response = mongo_obj.update_data_db(symbol,data)
    return response

