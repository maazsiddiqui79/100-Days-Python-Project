
---


# 🔠 Text ↔ Morse Code Translator

A responsive web application built with **Flask** that allows users to easily convert English text to Morse code and Morse code back to English text. It features a clean UI, intuitive input/output fields, and copy-to-clipboard functionality.

---

## 📌 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Technology Stack](#technology-stack)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Usage Guidelines](#usage-guidelines)
- [Morse Code Format](#morse-code-format)
- [Developer](#developer)
- [License](#license)

---

## ✅ Features

- 🔁 **Two-way conversion** between text and Morse code
- 📤 Simple form submission using POST request
- 💡 Real-time output display after conversion
- 📋 Copy button for easy copying of results
- 🧩 Clean Bootstrap 5 UI with grid layout
- 📱 Fully responsive for mobile and desktop
- 🎨 Custom styling and light hover effects
- 🔒 No external API calls — runs entirely on Flask backend

---

## 🖼️ Screenshots

### Home Page
![Morse to Text](Screenshot%202025-07-30%20061715.png)
### Home Page
![Morse to Text](Screenshot%202025-07-30%20061942.png)


### Text to Morse Code
![Text to Morse](Screenshot%202025-07-30%20061904.png)


---

## 🛠️ Technology Stack

| Layer       | Technology          |
|-------------|---------------------|
| Frontend    | HTML, CSS, Bootstrap 5 |
| Backend     | Python, Flask       |
| Logic       | Custom Python Dictionaries |
| Styling     | Inline & Embedded CSS |
| Scripts     | JavaScript (Clipboard API) |

---

## 📁 Folder Structure

```

morse-translator/
│
├── static/
│   └── morse-code.png
│
├── templates/
│   ├── index.html             # Main form (Text → Morse)
│   └── morse\_to\_text.html     # Reverse translator (Morse → Text)
│
├── app.py                     # Flask application logic
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation

````

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/morse-translator.git
cd morse-translator
````

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

Then open in browser:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧪 Usage Guidelines

### ✅ Text to Morse

1. Go to the home page.
2. Enter your plain English sentence (e.g., `HELLO WORLD`)
3. Click "Convert"
4. Copy the output using the copy button.

### ✅ Morse to Text

1. Use the "Text ← Morse-code" button on the top navbar.

2. Enter Morse using:

   * Dot (`.`)
   * Dash (`-`)
   * Space between letters
   * Forward slash (`/`) between words
     Example: `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

3. Click "Convert" to decode.

---

## 📋 Morse Code Format

| Rule                    | Format  | Example                               |
| ----------------------- | ------- | ------------------------------------- |
| Letter separator        | 1 space | `.... . .-.. .-.. ---` (HELLO)        |
| Word separator          | `/`     | `.... .. / - .... . .-. .` (HI THERE) |
| Dot                     | `.`     | `A → .-`                              |
| Dash                    | `-`     | `B → -...`                            |
| No use of special chars | ❌       | No `@`, `#`, `!`, `*`, etc.           |
| Case sensitivity        | ❌       | All input treated as uppercase        |

---

## ✍️ Developer

**👨‍💻 Maaz Siddiqui**
🎓 Diploma in Computer Engineering
🔗 [LinkedIn](https://www.linkedin.com/in/siddiqui-maazzz/)
💻 [GitHub](https://github.com/maazsiddiqui79)
📧 Email: [siddiquimaaz79@gmail.com](mailto:siddiquimaaz79@gmail.com)
📞 Contact: +91 88502 81310
---
