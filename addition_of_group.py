from flask import Flask, jsonify
from flask import request
from pymongo import MongoClient
from flask import json
from flask import abort
from flask import make_response
#from pymongo import Connection

app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.policy
collection = db.groups

def add_group(table, request):
    post_id = table.insert_one(request).inserted_id
    g = table.find_one({"_id": post_id})
    out = {'status': 'added', 'name' : g['name'], 'filter' : g['filter']}
    return out

def find_group(table, group_name):
    g = table.find_one({"name" : group_name})
    #print g
    if not g:
        return None
    out = {'name' : g['name'], 'filter' : g['filter']}
    #print out
    return out

@app.route('/abc', methods=['POST'])
def create_config_group_by_name():
    if not request.get_json(force=True) or not 'name' in request.get_json(force=True):
           abort(400)
    #check if group with given name alredy exists
    #print request.json['name']
    g = find_group(collection.groups, request.json['name'])
    if g:
    	print "Group already exists!"
    	return make_response("Group already exists in the db!\n", 409)
        #abort(409)
    #add to db
    groups = add_group(collection.groups, request.json)
    return jsonify({'groups': groups}), 201




if __name__ == '__main__':
	app.run(debug=True)