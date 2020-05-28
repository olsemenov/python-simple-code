import socket
import os
from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue","pink"])
MY_PORT = os.environ.get('PORT') or 8080

@app.route("/")
def main():
    print(color)
    f1 = open("test.txt", "a+")
    f1.write("now " + str(color) + "\n")
    f1.close()
    return render_template('index.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    f1 = open("test.txt", "a+")
    f1.write("now " + str(new_color) + "\n")
    f1.close()
    return render_template('index.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f1 = open("test.txt")
    contents = f1.read()
    return render_template('index.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(MY_PORT))