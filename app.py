from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    for value in request.headers:
        print(value)
    return render_template("index.html", headers=request.headers)


@app.route("/api")
def api():
    return jsonify(dict(request.headers))


if __name__ == "__main__":
    app.run(debug=True)
