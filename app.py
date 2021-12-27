from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)
@app.route('/Home')
@app.route('/')
def home_page():
    found = True
    if found:
        return render_template('index.html', name = 'Michael')
    else:
        return render_template('index.html')

@app.route('/about')
def about_func():
    return render_template('about.html', profile = {'name':'Michael', 'second_name':'Alfasy'}, university = 'BGU',
                          degrees = ['BSc','MSc'],
                           hobbies = ('sport' , 'music', 'python', 'flask'))

@app.route('/catalog')
def catalog_func():
    return render_template('catalog.html')

@app.route('/assignment8')
def assighn_func():
    hobbies = ('sport', 'music', 'python', 'flask')
    return render_template('assignment8.html')





if __name__ == '__main__':
    app.run(debug=True)

