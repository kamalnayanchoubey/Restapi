# app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400
    user = User(username=data['username'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/notes', methods=['GET', 'POST'])
@jwt_required()
def notes():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.json
        note = Note(user_id=user_id, content=data['content'])
        db.session.add(note)
        db.session.commit()
        return jsonify({"message": "Note added"}), 201

    notes = Note.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": note.id, "content": note.content} for note in notes]), 200

@app.route('/notes/<int:id>', methods=['PUT', 'DELETE'])
@jwt_required()
def update_delete_notes(id):
    user_id = get_jwt_identity()
    note = Note.query.filter_by(id=id, user_id=user_id).first()
    if not note:
        return jsonify({"message": "Note not found"}), 404

    if request.method == 'PUT':
        data = request.json
        note.content = data['content']
        db.session.commit()
        return jsonify({"message": "Note updated"}), 200

    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted"}), 200

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
