# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# hello world
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

# logging in
@app.route('/login', methods=['POST'])
def data():
    data = request.json
    name = data.get("name")
    password = data.get("password")
    with open("acc.json", "r") as file:
      acc = json.load(file)
      if name in acc and acc[name] == password:
        return jsonify({"success": True, "message": "Successfully logged in"})
      else:
          return jsonify({"success": False, "message": "Failed to login"})

# registering
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get("name")
    password = data.get("password")
    with open("acc.json", "r") as file:
      acc = json.load(file)
      if name in acc:
        return jsonify({"success": False, "message": "Username already used"})
      else:
          acc[name] = password
          with open("acc.json", "w") as file:
              json.dump(acc, file)
          return jsonify({"success": True, "message": "Account created"})

# getting all accounts
@app.route('/acc', methods=['GET'])
def acc():
    with open("acc.json", "r") as file:
      return json.load(file)

# running the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
