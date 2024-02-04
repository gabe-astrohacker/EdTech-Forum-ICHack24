from flask import Flask, redirect, render_template, request
 
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/search-results-page.html', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
    return render_template('search-results-page.html')

@app.route('/login-page.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userEmail = request.form['email']
        userPassword = request.form['password']
        return redirect('/')
    return render_template('login-page.html')

@app.route('/register-page.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userEmail = request.form['email']
        userPassword = request.form['password']
        return redirect('/')
    return render_template('register-page.html')

app.run(host='localhost', port=5000)
