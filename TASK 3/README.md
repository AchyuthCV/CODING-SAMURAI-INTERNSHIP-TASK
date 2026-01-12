# 📝 My Flask Blog

A simple yet elegant **Flask-based blogging website** with user authentication, post creation, and a clean UI.  
Built as part of the **CODING SAMURAI Internship Project**.

---

## 🚀 Features

- 👤 User Registration & Login (with password hashing)
- 🔐 Secure Authentication using Flask Sessions
- ✍️ Create Blog Posts
- 📃 View All Blog Posts
- 🗄️ SQLite Database
- 🎨 Modern UI with custom CSS
- 🖼️ Blog post images support (static files)
- 🚪 Logout functionality

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Security:** Werkzeug Password Hashing
- 

## 📁 Project Structure
---project_6_flask_blog/
-│
├── app.py
├── database.db
├── venv/
│
├── templates/
│ ├── home.html
│ ├── register.html
│ ├── login.html
│ ├── dashboard.html
│ ├── create_post.html
│ └── posts.html
│
├── static/
│ ├── style.css
│ └── images/
│ └── post.jpg
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/my-flask-blog.git
cd my-flask-blog

2️⃣ Create Virtual Environment
- python -m venv venv

3️⃣ Activate Virtual Environment

-Windows

-venv\Scripts\activate


-Mac/Linux

-source venv/bin/activate

4️⃣ Install Dependencies
-pip install flask werkzeug

5️⃣ Run the Application
-python app.py

