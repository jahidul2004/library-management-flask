# 📚 Library Management System (Flask + MongoDB)

A simple Library Management System built with **Python Flask** and **MongoDB** that supports basic CRUD operations on books, authors, users, and borrow records. This project is designed for learning RESTful APIs and NoSQL integration using MongoDB Compass.

---

## 🚀 Features

-   📘 Add, update, delete, and retrieve book data
-   👤 Manage library users (add, update, delete, view)
-   ✍️ Store author information
-   🔄 Track borrow and return records
-   🌐 REST API tested using Postman
-   ⚙️ MongoDB used as the backend database (with Compass)

---

## 🧰 Tech Stack

| Technology         | Use              |
| ------------------ | ---------------- |
| 🐍 Python          | Backend language |
| ⚡ Flask           | Web framework    |
| 🍃 MongoDB         | NoSQL database   |
| 🧭 MongoDB Compass | GUI for MongoDB  |
| 🔥 Postman         | API testing      |

---

## 📂 Folder Structure

📁 your-project/
├── app.py # Main Flask server
└── README.md # This file

## 🔌 Example API Routes

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| GET    | `/books`              | Get all books        |
| POST   | `/books`              | Add a new book       |
| GET    | `/users/<id>`         | Get a user by ID     |
| PUT    | `/borrowRecords/<id>` | Update borrow record |
| POST   | `/authors`            | Add a new author     |

> 🧪 Test all APIs using **Postman**

---

## 💡 Future Improvements

-   🔐 JWT-based authentication
-   🖼️ Frontend with React or Vue
-   📊 Admin dashboard UI
-   ✅ Book availability check logic

---

## 🤝 Contributions

PRs are welcome!  
For major changes, please open an issue first to discuss what you would like to change.
