from flask import render_template

from app import app
from app.calculations import multiply_by_two


@app.route("/")
@app.route("/index")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def show_data():
    data = {"message": "Hello, World!"}
    return render_template("data.html", data=data)


@app.route('/result/<int:post_id>')
def show_result_page(post_id):
    if post_id > 10:
        return "<p> Zoveel resultaten zijn er niet!</p>"
    return render_template("result.html", result_page=post_id, double=multiply_by_two(post_id))
