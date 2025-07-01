from flask import Flask , render_template , request
import requests
import smtplib


app = Flask(__name__)
URL = 'https://api.npoint.io/ab27cc324316fabb5f34'
response = requests.get(url=URL)
all_posts = response.json()


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
        
        
@app.route('/login',methods = ['GET','POST'])
def login_page():
    name = request.form['username']
    email_id = request.form['email-id']
    phone_no = request.form['phoneno']
    message = request.form['message']
    sender_mail = "maaz.irshad.siddiqui@gmail.com"
    password ="tvud sggg rdle ywll"
    message = f"Subject: Assalamualaikum\n\nNew User Registered\nName:{name}\nEmail:{email_id}\nPhone no:{phone_no}\nMessage:{message}"
    
    with smtplib.SMTP_SSL("smtp.gmail.com",port=465) as connection:
            connection.login(user=sender_mail,password=password)
            connection.sendmail(
                from_addr=sender_mail,
                to_addrs='siddiqui.maaz79@gmail.com',
                msg=message
            )
    print("Mail Sent")
    
    
    return render_template('successful_form_delivered.html')




if __name__ == '__main__':
    app.run(debug=True)