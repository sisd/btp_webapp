import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "This is where you write backchodi"

@app.route('/station')
def hello():
    return 'Dropdown shit'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)