from flask import Flask, render_template, redirect, url_for, request , session

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,FloatField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class edit_form(FlaskForm):
    rating = FloatField('Your Rating out of 10 eg:7.5',validators=[DataRequired()])
    review = StringField('Your Review',validators=[DataRequired()])
    done_btn = SubmitField('Done')


class add_form(FlaskForm):
    movie_name = StringField('Movie',validators=[DataRequired()])
    add_btn = SubmitField('Add Movie')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


# CREATE DB


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MY_MOVIE_DATABASE.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)

# CREATE TABLE
class MOVIE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String,nullable=False)
    rating = db.Column(db.Integer,nullable=False)
    ranking = db.Column(db.Integer,nullable=False)
    review = db.Column(db.String,nullable=False)
    img_url = db.Column(db.String,nullable=False)
    
    def __repr__(self):
        return f"<Movie {self.id} - {self.title} ({self.year}) | Rating: {self.rating} | Review: {self.review}>"

    
    
    
    
@app.route("/")
def home():
    movies = MOVIE.query.order_by(MOVIE.rating.desc()).all()
    all_movie = MOVIE.query.all()
    
    
    return render_template("index.html",all_movie=movies)




# data = {}
title_lst = []
@app.route("/add" , methods=['GET','POST'])
def add():
    add_new_movie_form = add_form()
    if add_new_movie_form.validate_on_submit():
        api_key = '581eed00793c64dcb3ffb6d5c0c08c06'
        url = "https://api.themoviedb.org/3/search/movie"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ODFlZWQwMDc5M2M2NGRjYjNmZmI2ZDVjMGMwOGMwNiIsIm5iZiI6MTc1MjYxOTYwMy40NDEsInN1YiI6IjY4NzZkYTUzZDgyODhlMGRmNjJlOGNiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.roCLsNRG787hD8fZWec-TSQxSdoShSzPMieaEzX4NC8"
        }

        params={
            'api_key':api_key,
            'query': add_new_movie_form.movie_name.data
        }
        

        response = requests.get(url, headers=headers,params=params)
        print(response)
        data =response.json()
        
        
        
        title_lst.clear()
        for i in range(len(data['results'])):
            title_lst.append({'id':data['results'][i]['id'],
                              'title':data['results'][i]['title'],
                              'img_url':data['results'][i]['poster_path'],
                              'year':data['results'][i]['release_date'],
                              'desc':data['results'][i]['overview'],
                              })

        
        
    
    return render_template('add.html',movie_form=add_new_movie_form,movie_title=title_lst)


@app.route("/add_new_movie/<int:id>", methods=['GET', 'POST'])
def add_new_movie(id):
    for i in title_lst:
        if id == i['id']:
            

            # Safe extraction with fallback values
            title = i['title']
            img_path = i['img_url']
            img_url = f"https://image.tmdb.org/t/p/original/{img_path}" if img_path else "https://via.placeholder.com/300x450?text=No+Image"
            release_date = i['year']
            year = release_date.split('-')[0] if release_date else 0
            desc = i['desc']


            # For Testing Purpose
            # Debug log
            # print(f"\n[DEBUG] Adding movie:")
            # print(f"Title     : {title}")
            # print(f"Image URL : {img_url}")
            # print(f"Year      : {year}")
            # print(f"Overview  : {desc}\n")

            new_movie = MOVIE(
                title=title,
                year=int(year),
                description=desc,
                rating=0.0,
                ranking=0,  # Should be integer
                review="None",
                img_url=img_url
            )
            db.session.add(new_movie)
            db.session.commit()
            
            current_movie_id = MOVIE.query.filter_by(title=title).first()

            return redirect(url_for('edit',id=current_movie_id.id))
    return redirect(url_for('home'))




@app.route("/delete/<int:id>" , methods=['GET','POST'])
def delete(id):
    movie = MOVIE.query.get_or_404(id)

    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))    

@app.route("/edit/<int:id>" , methods=['GET','POST'])
def edit(id):
    movie = MOVIE.query.get_or_404(id)
    form = edit_form()  # Populate form with existing data
    # form = edit_form(obj=movie)  # Populate form with existing data

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home")) 
    bg = movie.img_url   
    
    return render_template('edit.html',form=form,movie=movie,bg=bg)

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
