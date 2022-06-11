from flask import Flask
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
