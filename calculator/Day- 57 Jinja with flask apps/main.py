from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

BLOG_API_URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def home():
    response = requests.get(BLOG_API_URL)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    response = requests.get(BLOG_API_URL)
    posts = response.json()

    # find the post with matching id
    requested_post = None
    for post in posts:
        if post["id"] == blog_id:
            requested_post = post
            break

    if requested_post is None:
        abort(404)

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
