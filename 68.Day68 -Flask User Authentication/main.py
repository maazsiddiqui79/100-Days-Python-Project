from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app= app)
# db.init_app(app)

# CREATE TABLE IN DB
login_manager = LoginManager()
login_manager.init_app(app=app)
# login_manager.login_view('login')



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
    # def check_password
    
    


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html",logged_in = current_user.is_authenticated)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name  = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        hashed_password = generate_password_hash(password=password,method='pbkdf2:sha256',salt_length=8)
        new_user = User(name=name,email=email,password=hashed_password)
        exist_user = User.query.filter_by(email=email).first()
        if exist_user:
            flash('User with this email exists','danger')
        else:
            try:
                    
                db.session.add(new_user)
                db.session.commit()
                login_user(user=new_user)
                return render_template('secrets.html',logged_in = current_user.is_authenticated)
            except Exception:
                db.session.rollback()
                flash('ERRORRRR','danger')
           
    return render_template("register.html",logged_in = current_user.is_authenticated)



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user :
            if check_password_hash(user.password,password):    
                login_user(user=user)
                return redirect(url_for('secrets'))
            else:
                flash('Invalid Password','warning')
            
        else:
            flash('User Doesn\'t exists','danger')
        
        
    
    return render_template("login.html",logged_in = current_user.is_authenticated)



@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",user_name=current_user.name,logged_in = current_user.is_authenticated)


@app.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
