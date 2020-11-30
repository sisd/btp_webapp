import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods = ['GET'])
def main():
    return render_template('index.html')

@app.route('/station')
def hello():
    return 'Dropdown shit'

@app.route('/station1', methods=['GET', 'POST'])
def dropdown():
    states = ['s1', 's2', 's3', 's4']
    stations = ['st1', 'st2', 'st3']
    return render_template('test.html', states=states, stations=stations)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
