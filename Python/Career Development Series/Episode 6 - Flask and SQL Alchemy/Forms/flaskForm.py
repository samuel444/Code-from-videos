from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return ("Form Submitted Thank You " + username + '!')
    
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

