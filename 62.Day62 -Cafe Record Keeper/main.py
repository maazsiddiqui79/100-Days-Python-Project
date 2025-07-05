from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,SelectField
from wtforms.validators import DataRequired,ValidationError
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap = Bootstrap5(app)

def map_link(form, field):
    if 'https://' not in field.data or '/maps' not in field.data:
        raise ValidationError('Invalid Email Address')

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name:', validators=[DataRequired()])
    location = StringField('Location: ', validators=[DataRequired(),map_link])
    open = StringField('Open: ', validators=[DataRequired()])
    close = StringField('Close: ', validators=[DataRequired()])
    coffee = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField("WiFi", choices=["❌", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField("Power", choices=["❌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')
    

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        loc = form.location.data
        open_time = form.open.data
        close_time = form.close.data
        coffee_ = form.coffee.data
        wifi_ = form.wifi.data
        power_ = form.power.data
        
        with open('cafe-data.csv','a', encoding='utf-8') as f:
            f.write(f'\n{cafe_name},{loc},{open_time},{close_time},{coffee_},{wifi_},{power_}')
        
            
        with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in data:
                list_of_rows.append(row)
        return render_template('cafes.html', cafes=list_of_rows)
        
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
