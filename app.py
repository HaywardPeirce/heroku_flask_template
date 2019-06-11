# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/method", methods=['GET', 'POST'])
def index():
    
    # do something if the method was GET
    if request.method == 'GET':
        if 'param' in request.args:
            return 'The value of `param` was: ' + request.args['param']

    # do something if the request method was POST
    elif request.method == 'POST':
        
        return 'There was POST data!'


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    # return """
    # <h1>Hello heroku</h1>
    # <p>It is currently {time}.</p>
    # """.format(time=the_time)

    return render_template('index.html', the_time = the_time )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

