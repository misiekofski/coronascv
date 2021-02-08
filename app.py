from flask import Flask, render_template
from flask import request
from datetime import date
import pandas as pd
from urllib.request import Request, urlopen

start_date = date(2020, 12, 27)
today = date.today()
app = Flask(__name__)


@app.route('/')
def corona_plot():
    days_from_start = (today - start_date).days
    days = int(request.args.get('ld', default=0))
    add_days = days_from_start - days

    req = Request('http://scvconsultants.com/data.csv')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
    content = urlopen(req)

    dataset = pd.read_csv(content)
    labels = [x for x in dataset['date']][-days:]
    values = [x for x in dataset['vaccine_number']][-days:]
    return render_template('index.html', labels=labels, values=values, days_from_start=days_from_start,
                           add_days=add_days)


if __name__ == '__main__':
    app.run()
