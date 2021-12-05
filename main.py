from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("http://localhost:5000/user/redirect-test")


# @app.route("/")
# def index():
#     response = make_response("<h1>This document carries a cookie!</h1>")
#     response.set_cookie("answer", "42")
#     return response


# @app.route("/")
# def index():
#     user_agent = request.headers.get("User-Agent")
#     return "<p>Your browser is %s</p>" % user_agent


# @app.route("/")
# def index():
#     return "<h1>Hello World!</h1>"


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, %s!</h1>" % name


if __name__ == "__main__":
    app.run(debug=True)
