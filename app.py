from flask import Flask, request
from scrap import scrap_photo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/photos', methods=["POST"])
def get_photos():
    link = request.get_json()
    return scrap_photo(str(link))


if __name__ == '__main__':
    app.run(port=8080)
