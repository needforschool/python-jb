from flask import Flask, render_template
from system_info import SystemInfo

system_info = SystemInfo()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', system_info=system_info)