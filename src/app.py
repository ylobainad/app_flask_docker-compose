from crypt import methods
from flask import Flask, jsonify
from users import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "hello world"})

@app.route('/users')
def users_handler():
    return jsonify({"users":users})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)