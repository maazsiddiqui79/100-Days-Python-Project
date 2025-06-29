from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

@app.context_processor
def inject_year():
    return {'current_year':datetime.datetime.now().year}

URL = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url=URL)
all_posts = response.json()
@app.route('/')
def home():
    return render_template("index.html",post=all_posts)

@app.route('/post/<int:num>')
def get_blog(num):
    for i in all_posts:
        if num == i['id']:
            return render_template('post.html',number=num,post=i)

if __name__ == "__main__":
    app.run(debug=True)
