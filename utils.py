import json

COMMENTS = "./data/comments.json"
POSTS = "./data/posts.json"


def get_posts_all():
    with open(POSTS, encoding='utf-8') as file:
        posts_all = json.load(file)
        tag = []
        for post in posts_all:
            for word_content in post["content"]:
                if "#" in word_content:
                    tag.append(word_content)
        return posts_all


def get_posts_by_user(user_name):
    post_by_user = []
    posts_all = get_posts_all()
    for post in posts_all:
        if user_name.lower() == post["poster_name"].lower():
            post_by_user.append(post)
    return post_by_user


def get_comments_by_post_id(post_id):
    with open(COMMENTS, encoding='utf-8') as file:
        comments = json.load(file)
        comments_by_id = []
        for comments_post in comments:
            if post_id == comments_post["post_id"]:
                comments_by_id.append(comments_post)
        return comments_by_id


def search_for_posts(tag):
    posts_by_tag = []
    for post in get_posts_all():
        if tag.lower() in post["content"].lower():
            posts_by_tag.append(post)
    return posts_by_tag


def get_post_by_pk(pk):
    posts_all = get_posts_all()
    for post in posts_all:
        if post["pk"] == pk:
            return post
