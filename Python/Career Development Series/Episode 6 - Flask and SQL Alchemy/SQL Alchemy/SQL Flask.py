from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db' 

db = SQLAlchemy(app)

class details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))


@app.before_request
def create_tables():
    db.create_all()

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ids = []
        users = details.query.all()
        for user in users:
            if user.username == username:
                return "This username already exists!"
            ids.append(user.id)
        id = 1
        while id in ids:
            id += 1
        new_user = details(id=id, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return "You have signed up successfully!"
    return render_template('signUp.html')

@app.route('/details')
def get_details():
    users = details.query.all()
    return render_template('table.html', users=users)

@app.route('/deleteuser/<int:id>')
def delete_user(id):
    user = details.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted!'
    return 'User not found!'

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = details.query.all()
        for user in users:
            if user.username == username and user.password == password:
                return ("Welcome Back " + username) 
        return ("Incorrect Login Details")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
