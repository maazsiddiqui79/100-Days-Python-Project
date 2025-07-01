from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)
URL = 'https://api.npoint.io/ab27cc324316fabb5f34'
response = requests.get(url=URL)
all_posts = response.json()
# for post in all_posts:
#     post["image_url"] = "https://via.placeholder.com/900x300"  # or any valid image URL


@app.route('/')
def main_server_page():
    return render_template('index.html',post=all_posts)


@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')
        
@app.route('/post/<int:num>')
def post_page(num):
    for i in all_posts:
        if num == i['id']:
            return render_template('post.html',number=num,post=i)




if __name__ == '__main__':
    app.run(debug=True)