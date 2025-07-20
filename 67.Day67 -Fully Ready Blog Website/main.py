from flask import Flask, render_template, redirect, url_for ,request
# from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os
from datetime import date
import smtplib


app = Flask(__name__, instance_relative_config=True)
ckeditor = CKEditor(app)
os.makedirs(app.instance_path, exist_ok=True)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap5(app)


# Create a Flask Form 
class ADD_NEW_POST_FORM(FlaskForm):
    title = StringField("Blog post title",validators=[DataRequired()])
    subtitle = StringField("Subtitle",validators=[DataRequired()])
    author_name = StringField("Author Name",validators=[DataRequired()])
    img_url = StringField("Image For BG",default='data:image/jpeg;base64,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')
    # body = CKEditorField('Content')
    body = TextAreaField("Content")
    done_btn = SubmitField("Post")
    


# CREATE DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.instance_path + '/posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CKEDITOR_WIDTH'] = 400
app.config['CKEDITOR_HEIGHT'] = 400
db = SQLAlchemy(app)
# db.init_app(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(250),nullable=False)
    subtitle= db.Column(db.String(250), nullable=False)
    date= db.Column(db.String(250), nullable=False)
    body= db.Column(db.Text, nullable=False)
    author= db.Column(db.String(250), nullable=False)
    img_url= db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/admin-maaz')
def admin_panel():
    # Query the database for all the posts. Convert the data to a python list.
    result = BlogPost.query.all()
    edit_btn_condition = 'True'
    print(result)
    return render_template("index.html", all_posts=result,ebc=edit_btn_condition)



@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    result = BlogPost.query.all()
    edit_btn_condition = 'False'
    print(result)
    return render_template("index.html", all_posts=result,ebc=edit_btn_condition)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>/<ebc>')
def show_post(post_id,ebc):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    
    requested_post = BlogPost.query.filter_by(id=post_id).first()
    return render_template("post.html", post=requested_post,ebc=ebc)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post',methods=['GET','POST'])
def add_new_post():
    form  =ADD_NEW_POST_FORM()
    if form.validate_on_submit():
        print('hello')
        title= form.title.data
        subtitle= form.subtitle.data
        a_name= form.author_name.data
        img= form.img_url.data
        content= form.body.data
        new_post = BlogPost(title=title,
                            subtitle=subtitle,
                            date=date.today().strftime("%B %d, %Y"),
                            body=content,
                            author=a_name,
                            img_url=img)
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
        
    return render_template('make-post.html',form=form,t= 'New Post')

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>',methods=['GET','POST'])
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    fform = ADD_NEW_POST_FORM(obj=post)
    if post:
        if fform.validate_on_submit():
            print('hello')
            title= fform.title.data
            subtitle= fform.subtitle.data
            a_name= fform.author_name.data
            img= fform.img_url.data
            content= fform.body.data
            post.title = title
            post.subtitle = subtitle
            post.author = a_name
            post.img_url = img
            post.body = content
            
            db.session.commit()
            # return redirect(url_for('show_post', post_id=post.id, ref='edit'))
            return redirect(url_for('get_all_posts'))
    
    return render_template('make-post.html',form=fform,t= 'Edit Post')
    

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete-post/<post_id>',methods=['GET','POST'])
def delete_post(post_id):
    data = BlogPost.query.get_or_404(post_id)
    print(data)
    db.session.delete(data)
    db.session.commit()
    
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method =='POST':
        print("ON CONTACT PAGE")
        
        name = request.form['name']
        email_id = request.form['email']
        phone_no = request.form['phone']
        message = request.form['message']
        sender_mail = "maaz.irshad.siddiqui@gmail.com"
        password ="tvud sggg rdle ywll"
        message = f"""Subject: Assalamualaikum

    You’ve received a new message from your website contact form.

    New User Registered
    Name: {name}
    Email: {email_id}
    Phone No: {phone_no}

    Message:
    {message}

    ---

    This message was sent via the contact form on your portfolio/blog site.
    Please respond at your earliest convenience.
    """

        
        with smtplib.SMTP_SSL("smtp.gmail.com",port=465) as connection:
                
                connection.login(user=sender_mail,password=password)
                connection.sendmail(
                    from_addr=sender_mail,
                    to_addrs='siddiqui.maaz79@gmail.com',
                    msg=message.encode("utf-8")
                )
        print("Mail Sent")
        return render_template('successful_form_delivered.html')
    
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
