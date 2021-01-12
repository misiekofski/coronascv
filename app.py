from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route('/')
def corona_plot():
    dataset = pd.read_csv('data.csv')
    labels = [str(x) for x in dataset['date']]
    values = [x for x in dataset['vaccine_number']]
    return render_template('index.html', labels=labels, values=values)


if __name__ == '__main__':
    app.run()
