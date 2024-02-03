from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

 
@app.route('/search-results-page.html', methods=['GET', 'POST'])
def search():
    return render_template('results.html')

@app.route('/login-page.html', methods=['GET', 'POST'])
def login():
    return render_template('login-page.html')

@app.route('/register-page.html', methods=['GET', 'POST'])
def register():
    return render_template('register-page.html')

app.run(host='localhost', port=5000)
