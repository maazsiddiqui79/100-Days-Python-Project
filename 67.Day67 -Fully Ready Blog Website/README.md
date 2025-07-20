
---

# 📝 Blog Website

A clean and minimal **Blog Web Application** built using **Flask (Python)**, deployed on **Vercel**, with blog data stored securely in a **PostgreSQL** database hosted on **Render**.

<!-- ---

## 🌐 Live Demo

👉 [Visit the Blog Website]() -->

---

## 🚀 Features

* 📰 Public blog reading access for users
* 🛡️ Admin-only blog creation and deletion (with login authentication)
* 📅 Timestamped blog posts
* 🧾 Blog content stored securely in a database
* ✍️ Simple and responsive blog interface
* ⚙️ Backend validation for form data

---

## 🛠️ Tech Stack

| Layer              | Technology          |
| ------------------ | ------------------- |
| Backend            | Flask (Python)      |
| Forms & Validation | Flask-WTF, WTForms  |
| Database           | PostgreSQL (Render) |
| ORM                | SQLAlchemy          |
| Hosting            | Vercel              |
| Deployment (DB)    | Render              |
| Templating         | Jinja2 (HTML)       |
| Styling            | CSS                 |

---

## 🧱 Project Structure

```
blog-website/
│
├── templates/
│   ├── index.html
│   ├── create.html
│   ├── login.html
│   └── blog_detail.html
│
├── static/
│   └── (optional CSS/JS files)
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (Local Development)

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/blog-website.git
   cd blog-website
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. **Run the application**

   ```bash
   flask run
   ```

6. **Visit**:
   `http://127.0.0.1:5000`

---

<!-- ## 📦 Deployment

### 🌍 Vercel (Frontend)

* Flask app deployed using Vercel’s Python template or custom configuration.

### 🗄️ Render (Database)

* PostgreSQL database hosted on [Render.com](https://render.com).
* Use the following format for your database URI:

  ```bash
  postgresql+psycopg2://username:password@host:port/database_name
  ```

--- -->

## 📑 Sample Usage

### 👀 Read Blogs

* All visitors can see published blog posts on the homepage.

### 🔐 Admin Login

* Admins can log in with secure credentials.
* Admin panel allows:

  * 📝 Creating new blog entries
  * ❌ Deleting existing blog posts

---

## 📬 Contact Me

* ✅ **To-Do App**: [Visit My To-Do App](https://go-todo-task.vercel.app/)
* 🔗 **URL Shortener**: [Check My URL Shortener](#)
* 💼 **LinkedIn**: [linkedin.com/in/siddiqui-maazzz](https://www.linkedin.com/in/siddiqui-maazzz/)
* 🛠️ **GitHub**: [github.com/maazsiddiqui79](https://github.com/maazsiddiqui79)

---

### ✍️ Author

**Maaz Siddiqui**
*Diploma in Computer Engineering | Passionate about Web Development and AI*

---
