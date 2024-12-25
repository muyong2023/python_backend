from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["zijin_db"]

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = list(db.projects.find({}, {"_id": 0}))
    return jsonify(projects)

@app.route('/contact', methods=['POST'])
def save_contact():
    data = request.json
    db.contacts.insert_one(data)
    return jsonify({"message": "Contact saved!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
