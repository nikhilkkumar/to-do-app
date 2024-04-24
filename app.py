from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

# MongoDB connection setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_database"
mongo = PyMongo(app)

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    task = {
        "title": request.json['title'],
        "description": request.json['description'],
        "due_date": datetime.strptime(request.json['due_date'], '%Y-%m-%d'),
        "priority": request.json['priority'],
        "tags": request.json['tags'],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    mongo.db.tasks.insert_one(task)
    return jsonify(task), 201

# Route to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = mongo.db.tasks.find()
    return jsonify([task for task in tasks]), 200

# Route to retrieve a single task by ID
@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    if task:
        return jsonify(task), 200
    else:
        return jsonify({"error": "Task not found"}), 404

# Route to update a task by ID
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    update_result = mongo.db.tasks.update_one(
        {'_id': ObjectId(task_id)},
        {'$set': request.json}
    )
    if update_result.modified_count > 0:
        return jsonify({"msg": "Task updated"}), 200
    else:
        return jsonify({"error": "No changes made"}), 400

# Route to delete a task by ID
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    delete_result = mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})
    if delete_result.deleted_count > 0:
        return jsonify({"msg": "Task deleted"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
