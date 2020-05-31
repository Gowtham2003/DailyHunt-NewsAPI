
# Coded By Gowtham on 30/05/2020
# Coded Using Vim Text Editor
from flask import Flask, request, jsonify
from DailyHunt import getNews
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "I_am_Marvelous (^_^)"
CORS(app)


@app.route('/')
def home():
    return 'News API is UP!<br><br>A part of <a href="https://t.me/alphaprojects">Alpha Projects</a>'


@app.route('/news')
def news():
    if request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
