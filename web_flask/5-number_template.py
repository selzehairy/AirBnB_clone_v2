# File: web_flask/5-number_template.py
#!/usr/bin/python3
"""
5-number_template.py - A Flask web application with routes for '/', '/hbnb', '/c/<text>', '/python/(<text>)', '/number/<n>',
and '/number_template/<n>'.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
