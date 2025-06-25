# Flask, Jsonify & Request import
from flask import Flask, jsonify, request
# MongoClient import
from pymongo import MongoClient
# Object id import
from bson.objectid import ObjectId

# Create app
app = Flask(__name__)

#Local Mongodb Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.libraryDB

# Root Route
@app.route('/')
def home():
    return 'Library Management System is Running!'

# ------------------ All get Routes --------------------

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

# ------------------ All post routes ------------------

# Add a single book route
@app.route('/book', methods=['POST'])
def addABook():
    bookData = request.json
    result = db.books.insert_one(bookData)
    
    return jsonify({
        "message":"Book successfully inserted!",
        "inserted_id":str(result.inserted_id)
    }),201
    
# Add a single user route
@app.route('/user', methods=['POST'])
def addAUser():
    userData = request.json
    result = db.users.insert_one(userData)
    
    return jsonify({
        "message":"User successfully inserted!",
        "inserted_id":str(result.inserted_id)
    }),201
    
# Add a single author route
@app.route('/author', methods=['POST'])
def addAAuthor():
    authorData = request.json
    result = db.authors.insert_one(authorData)
    
    return jsonify({
        "message":"Author successfully inserted!",
        "inserted_id":str(result.inserted_id)
    }),201
    
# Ass a single borrow record
@app.route('/borrowRecord', methods=['POST'])
def addABorrowRecord():
    borrowRecordData = request.json
    result = db.borrowRecords.insert_one(borrowRecordData)
    
    return jsonify({
        "message":"Borrow Record successfully inserted!",
        "inserted_id":str(result.inserted_id)
    }),201
    
# ------------------ Post routes end ------------------

# ----------------- Get by id route -------------------

# Get user by id
@app.route('/user/<id>', methods=['GET'])
def getUserById(id):
    try:
        user = db.users.find_one({
            "_id" : ObjectId(id)
        })
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user)
        else:
            return jsonify({
                "error" : "User not found!"
            }), 404
    except:
        return jsonify({
            "error" : "Invalid User Id!"
        }), 400

# Get author by id
@app.route('/author/<id>', methods=['GET'])
def getAuthorById(id):
    try:
        author = db.authors.find_one({
            "_id" : ObjectId(id)
        })
        if author:
            author['_id'] = str(author['_id'])
            return jsonify(author)
        else:
            return jsonify({
                "error" : "Author not found!"
            }), 404
    except:
        return jsonify({
            "error" : "Invalid Author Id!"
        }), 400

# ---------------- Get by id route end -----------------

# Run the server
if __name__ == '__main__':
    app.run(debug = True)