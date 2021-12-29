from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
app = Flask(__name__)
app.secret_key = '123'
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
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html',product=product,size=size)
    return render_template('catalog.html')

@app.route('/assignment8')
def assighn_func():
    hobbies = ('sport', 'music', 'python', 'flask')
    return render_template('assignment8.html')

@app.route('/login', methods =['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('log-in.html')

    if request.method == 'POST':
        #DB
        username = request.form['username']
        password = request.form['password']
        found = True
        if found:
            session['username'] = username
        return redirect(url_for('home_page'))
    else:
        return render_template('log-in.html')

@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('index.html')

@app.route('/assignment9',methods=['GET','POST'])
def assignment9_func():
    users = {'user1': {'name': 'Michael:', 'email':'Michael@gmail.com'},
             'user2':{'name': 'Ido:', 'email':'Ido@gmail.com'},
             'user3': {'name': 'Roni:', 'email': 'Roni@gmail.com'},
             'user4': {'name': 'Omer:', 'email': 'Omer@gmail.com'},
             'user5': {'name': 'Gil:', 'email': 'Gil@gmail.com'}}
    if request.method == 'GET':
        if 'usersearch' in request.args:
            search_user = request.args['usersearch']
            return render_template('assignment9.html',users=users,search_user=search_user)
        return render_template('assignment9.html',users=users)
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        session['username']=username
        session['email']=email
        return render_template('assignment9.html')

if __name__ == '__main__':
    app.run(debug=True)

