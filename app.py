from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def load_main_page():
    return render_template("index.html")


# @app.route("/feed", method=["GET"])
# def load_feed_page():
#     pass


# @app.route("/post", method=["GET", "POST"])
# def load_post():
#     pass


# @app.route("/search/?s=<key_search>", method=["GET"])
# def search_page():
#     pass


# @app.route("users/<user_name>", method=["GET"])
# def load_user():
#     pass

app.run()