from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/home_page')
@app.route('/')
def hello_world():
    return 'Welcome to the main page!'

@app.route('/about')
def about_func():
    return redirect('/catalog')

@app.route('/catalog')
def catalog_func():
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)

