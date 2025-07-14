from flask import Flask , redirect , url_for , render_template  , request
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import String , Float 
from flask_wtf import FlaskForm 
from wtforms import StringField , SubmitField
from wtforms.validators import DataRequired

class myform(FlaskForm):
    book_name_ip = StringField('Book Name:',validators=[DataRequired()])
    book_author_ip = StringField('Book Author:',validators=[DataRequired()])
    book_rating_ip = StringField('Book Author:',validators=[DataRequired()])
    submit_btn = SubmitField('submit')




app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'My-Very-Very-Top-Ultra-Secrect-Key'

my_sql = SQLAlchemy(app=app)

class MY_DATA(my_sql.Model):
   
    id = my_sql.Column(my_sql.Integer,primary_key=True)
    book_name = my_sql.Column(my_sql.String,nullable=False)
    book_author = my_sql.Column(my_sql.String,nullable=False)
    book_rating= my_sql.Column(my_sql.String,nullable=False)
    
    
    def __repr__(self):
         return (f"<MY_DATA id={self.id} "
                f"name='{self.book_name}' "
                f"author='{self.book_author}' "
                f"rating={self.book_rating}>")
    
    
    
    
@app.route('/')
def home():
    all_books = MY_DATA.query.all()
    return render_template('home.html',all_books=all_books)


@app.route('/add_new_book',methods=['GET','POST'])
def add_new_book():
    form = myform()
    
    if form.validate_on_submit():
        name = form.book_name_ip.data
        author = form.book_author_ip.data
        rating = form.book_rating_ip.data
        
        
        add_new_entry = MY_DATA(book_name=name,book_author=author,book_rating=rating)
        my_sql.session.add(add_new_entry)
        my_sql.session.commit()
        return redirect(url_for('home'))
    
    return render_template('add.html',form=form)

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    user_del = my_sql.session.query(MY_DATA).filter_by(id=id).first()
    
    if user_del:
        my_sql.session.delete(user_del)
        my_sql.session.commit()
    
    return redirect('/')
    
   
    
@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    user_edit = my_sql.session.query(MY_DATA).filter_by(id=id).first()
    user_choice_book = user_edit.book_name
    user_choice_author = user_edit.book_author
    
    
       
    if request.method == 'POST':
        new_rating = request.form['rating']
        user_edit.book_rating = new_rating
        my_sql.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html',u_book=user_choice_book,u_author=user_choice_author,id=id) 
    
    
with app.app_context():
    my_sql.create_all()
    


if __name__ =='__main__':
    app.run(debug=True)