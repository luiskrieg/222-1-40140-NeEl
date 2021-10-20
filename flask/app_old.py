from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Runnig Flask server http://127.0.0.1:5000/"

if __name__ == "__main__":
    app.run(debug=True)