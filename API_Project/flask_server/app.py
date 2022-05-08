from flask import Flask, render_template
import json
app = Flask(__name__)

with open("가천대_naver_news.json", "r") as json_file:
    data = json.load(json_file)

@app.route("/")
def hello():
    return render_template("index.html", news_dict_list=data[0:11])

