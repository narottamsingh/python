#!/usr/bin/python
from flask import Flask, request, jsonify
from flask_cors import CORS
import dbconnection
import logconfig

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(dbconnection.get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    logger.info("get particular user",user_id) 
    return jsonify(dbconnection.get_user_by_id(user_id))

@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(dbconnection.insert_user(user))

@app.route('/api/users/update',  methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(dbconnection.update_user(user))

@app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(dbconnection.delete_user(user_id))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    logger= logconfig.logconfig()
    logger.info("Server starting") 
    app.run()
    logger.info("Server started")