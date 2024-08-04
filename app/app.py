
from flask import Flask, jsonify, request
# import database
import database


app = Flask(__name__)

@app.route('/')
def index():
    return "Index!"

@app.route('/user')
def get_users():
    users = database.get_all_users()
    return jsonify(users)

@app.route('/user/<int:uid>')
def get_user(uid):
    user = database.get_user(uid)
    return jsonify(user)

@app.route('/user/new', methods=['POST'])
def create_user():
    req = request.get_json()
    name = req['name']
    age = req['age']
    
    result = database.create_user(name, age)
    return jsonify(result)

@app.route('/user/<int:uid>', methods=['PUT'])
def update_user(uid):
    req = request.get_json()
    name = req['name']
    age = req['age']
    
    result = database.update_user(uid, name, age)
    return jsonify(result)

@app.route('/user/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    result = database.delete_user(uid)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
