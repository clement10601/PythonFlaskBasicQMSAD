from server import app
from flask import render_template

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/css/default.css')
def bundle():
    return app.send_static_file('css/default.css')

@app.route('/js/bundle.js')
def default():
    return app.send_static_file('js/bundle.js')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
