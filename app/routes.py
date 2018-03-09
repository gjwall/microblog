from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'graham'}
    posts = [
        {'author': {'username': 'sam'},
         'body': 'this is sam''s body'},
        {'author': {'username': 'gemma'},
         'body': 'this is gemma''s body'}
    ]
    return render_template('index.html', title='Home', user = user, posts = posts)
