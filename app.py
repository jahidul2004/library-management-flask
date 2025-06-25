# Flask, Jsonify & Request import
from flask import flash, jsonify, request

# Create app
app = flash(__name__)

# Root Route
@app.route('/')
def home():
    return 'Library Management System is Running!'

# Run the server
if __name__ == '__main__':
    app.run(debug = True)