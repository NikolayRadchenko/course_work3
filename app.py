import json
import logging
import werkzeug.exceptions

from flask import Flask, request, render_template

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

logging.basicConfig(filename="./logs/api.log", level=logging.INFO,
                    encoding='utf-8', format='%(asctime)s [%(levelname)s] %(message)s')


app = Flask(__name__)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return render_template("404.html"), 404


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return render_template("500.html"), 500


app.register_error_handler(404, handle_bad_request)
app.register_error_handler(500, handle_bad_request)


@app.route("/", methods=["GET"])
def load_main_page():
    posts_all = get_posts_all()
    return render_template("index.html", posts=posts_all)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def load_post(post_id):
    post = get_post_by_pk(post_id)
    comments_post = get_comments_by_post_id(post_id)
    return render_template("post.html", ava=post["poster_avatar"], user_name=post["poster_name"],
                           img_post=post["pic"], views=post["views_count"], post_id=post_id, post_text=post["content"],
                           comments_count=len(comments_post), comments=comments_post, poster_name=post["poster_name"])


@app.route("/search/", methods=["GET"])
def search_page():
    tag = request.args.get("tag")
    posts = search_for_posts(tag)
    return render_template("search.html", posts=posts, search_count=len(posts))


@app.route("/user/<user_name>", methods=["GET"])
def load_user(user_name):
    posts_by_user = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts_by_user, user_name=user_name)


@app.route("/api/posts/", methods=["GET"])
def list_posts_json():
    logging.info('Запрос /api/posts')
    with open("./data/posts.json", encoding="utf-8") as file:
        data = json.load(file)
        if type(data) == list:
            return json.dumps(data, ensure_ascii=False)
        else:
            return "Неудалось загрузить json файл"


@app.route("/api/posts/<int:post_id>", methods=["GET"])
def load_post_json(post_id):
    logging.info(f'Запрос /api/posts/{post_id}')
    with open("./data/posts.json", encoding="utf-8") as file:
        data = json.load(file)
        for _post in data:
            if type(_post) == dict:
                if _post["pk"] == post_id:
                    return json.dumps(_post, ensure_ascii=False)
            else:
                return "Не удалось загрузить json файл"


if __name__ == "__main__":
    app.run()
