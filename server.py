from flask import Flask, send_from_directory, request, jsonify, render_template
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/linkshortener"
mongo = PyMongo(app)


@app.route('/', methods=["GET"])
def index():
    return 'This should be the homepage'


@app.route('/shorten', methods=["GET"])
def shorten():
    return render_template('form.html')


@app.route('/api/shorten', methods=["POST"])
def shorten_url():
    print('**** shortening link *****')
    print(request.form)
    _form = request.form
    _link = _form["url"]
    _count = 0
    _id = uuid.uuid4()
    id = mongo.db.urls.insert({'link': _link, 'url': _id, 'count': _count})
    resp = jsonify('Id successfully inserted!')
    resp.status_code = 200
    return resp


@app.route('/s', methods=["GET"])
def redirect():
    return 'The link where the URL will be redirect to its original. The access counter for it will also be incremented'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
