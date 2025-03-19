from flask import Flask, render_template, request, jsonify
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

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.json 
        username = data.get('username')
        password = data.get('password')
        users = details.query.all()
        for user in users:
            if user.username == username and user.password == password:
                return jsonify({'message': 'Login Successful', 'status': 'success'})
        return jsonify({'message': 'Invalid credentials', 'status': 'error'})
 
        
    else:
        return render_template('login.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        data = request.json 
        username = data.get('username')
        password = data.get('password')
        confpassword = data.get('confpassword')
        users = details.query.all()
        if password != confpassword:
                return jsonify({'message': 'The passwords do not match!', 'status': 'error'})
        
        ids = []
        for user in users:
            if user.username == username:
                return jsonify({'message': 'This username already exists!', 'status': 'error'})
            ids.append(user.id)
        id = 1
        while id in ids:
            id += 1
        new_user = details(id=id, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Signed up successfully', 'status': 'success'}), 401
 
        
    else:
        return render_template('signup.html')
    


if __name__ == '__main__':
    app.run(debug=True)