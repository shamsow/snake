# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/game')
def game():
    return render_template('game.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)