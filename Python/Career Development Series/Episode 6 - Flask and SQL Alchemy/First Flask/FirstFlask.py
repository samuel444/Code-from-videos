from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask!'

@app.route('/welcome')
def welcome():
    return 'This is the welcome page on the welcome route'

@app.route('/about')
def about():
    return render_template('aboutPage.html')

names = ['Henry', 'Charlie', 'John', 'Emily', 'Erin']
@app.route('/names')
def namesList():
    return render_template('names.html',
                           names=names)


if __name__ == '__main__':
    app.run(debug=True)