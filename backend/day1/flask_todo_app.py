"""
Flask Todo CRUD API
A simple REST API for managing Todo items using Flask.
"""

from flask import Flask, request, jsonify
from typing import List, Dict, Optional

app = Flask(__name__)

# In-memory data store for todos
todos: List[Dict] = []
next_id = 1


@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todo items."""
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo item."""
    global next_id
    
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    todo = {
        'id': next_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': data.get('completed', False)
    }
    
    todos.append(todo)
    next_id += 1
    
    return jsonify(todo), 201


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id: int):
    """Get a specific todo item by ID."""
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify(todo), 200


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id: int):
    """Update a specific todo item by ID."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    # Update fields if provided
    if 'title' in data:
        todo['title'] = data['title']
    if 'description' in data:
        todo['description'] = data['description']
    if 'completed' in data:
        todo['completed'] = data['completed']
    
    return jsonify(todo), 200


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    """Delete a specific todo item by ID."""
    global todos
    
    todo_index = next((i for i, todo in enumerate(todos) if todo['id'] == todo_id), None)
    
    if todo_index is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    deleted_todo = todos.pop(todo_index)
    return jsonify(deleted_todo), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'Todo API is running'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)