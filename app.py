from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise request/<user_name>')
def test_sample(user_name):
    return user_name

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')

@app.route('/answer')
def answer_html():
    result = request.args.get("my_name")
    return render_template('answer.html',name=result)


