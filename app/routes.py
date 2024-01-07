from flask import render_template, request, url_for, redirect, session
from flask_paginate import get_page_parameter, Pagination

from app import app
from app.calculations import get_results


@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/index', methods=['POST'])
def search():
    search_text = request.form['search_text']
    session['search_text'] = search_text
    session['results'] = get_results(search_text)
    return redirect(url_for("show_result_page", post_id=0))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/result')
def show_result_page(results_per_page=5):
    search_text = session.get('search_text', None)
    results = session.get('results', None)

    if results is None:
        return redirect(url_for("index", post_id=0))

    # set up pagination
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(
        page=page, total=len(results), search=False, record_name='results', per_page=results_per_page
    )

    # get results for current page
    start = (page-1) * results_per_page
    end = min(start + results_per_page, len(results))
    page_results = results[start:end]

    return render_template("result.html", search_text=search_text, results=page_results, pagination=pagination)
