from flask import Flask, render_template
from flask import request
from datetime import date
import pandas as pd

start_date = date(2020,12,27)
today = date.today()
app = Flask(__name__)


@app.route('/')
def corona_plot():
    days = int(request.args.get('ld', default=0))
    days_from_start = (today-start_date).days
    dataset = pd.read_csv('data.csv')
    labels = [x for x in dataset['date']][-days:]
    values = [x for x in dataset['vaccine_number']][-days:]
    return render_template('index.html', labels=labels, values=values, days_from_start=days_from_start)


if __name__ == '__main__':
    app.run()
