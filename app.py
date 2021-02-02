import os
from flask import Flask, render_template
from flask import request
from datetime import date
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URI = os.environ['DATABASE_URL']

start_date = date(2020, 12, 27)
today = date.today()
app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def corona_plot():
    from models import VaccinesByDate
    vaccines = VaccinesByDate.query.all()
    days_from_start = (today - start_date).days
    days = int(request.args.get('ld', default=0))
    add_days = days_from_start - days
    dataset = pd.read_csv('data.csv')
    labels = [x for x in dataset['date']][-days:]
    values = [x for x in dataset['vaccine_number']][-days:]
    return render_template('index.html', labels=labels, values=values, days_from_start=days_from_start,
                           add_days=add_days, vaccines=vaccines)


if __name__ == '__main__':
    app.run()
