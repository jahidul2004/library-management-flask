# Flask, Jsonify & Request import
from flask import Flask, jsonify, request
# MongoClient import
from pymongo import MongoClient

# Create app
app = Flask(__name__)

#Local Mongodb Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.libraryDB

# Root Route
@app.route('/')
def home():
    return 'Library Management System is Running!'

# ------------------ All get Route --------------------

# Get all books
@app.route('/books',methods=['GET'])
def getBooks():
    books = []
    for book in db.books.find():
        book['_id'] = str(book['_id'])
        books.append(book)
    return jsonify(books)

# Get all Authors
@app.route('/authors', methods=['GET'])
def getAuthors():
    authors = []
    for author in db.authors.find():
        author['_id'] = str(author['_id'])
        authors.append(author)
    return jsonify(authors)

# Get all users
@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for user in db.users.find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)

# Get all borrowRecords
@app.route('/borrowRecords', methods=['GET'])
def getBorrowRecords():
    borrowRecords = []
    for borrowRecord in db.borrowRecords.find():
        borrowRecord['_id'] = str(borrowRecord['_id'])
        borrowRecords.append(borrowRecord)
    return jsonify(borrowRecords)

# ------------------ Get Route end --------------------

# Run the server
if __name__ == '__main__':
    app.run(debug = True)