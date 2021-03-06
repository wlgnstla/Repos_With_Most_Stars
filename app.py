"""
A Simple Flask Web Application interface
For viewing popular GitHub Repos sorted by stars using the
GitHub Search API.

To run:
$ FLASK_APP=app.py FLASK_ENV=development flask run
"""
from flask import Flask, render_template, request

from repos.api import repos_with_most_stars
from repos.exceptions import GitHubApiException

app = Flask(__name__)

available_languages = ["Javascript", "HTML", "CSS", "SQL", "Python","TypeScript", "Java", "Shell","C#","C++","PHP","C","Go","Rust","Kotlin",
"Dart","Ruby","Assembly","Swift","R"]


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # Use the list of all languages
        selected_languages = available_languages
    elif request.method == 'POST':
        # Use the languages we selected in the request form
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results)


@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)


