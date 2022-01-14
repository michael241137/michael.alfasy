import json
import requests
import random
from flask import Flask, redirect, url_for, request, Blueprint, jsonify
from flask import render_template, session
from mysqlx.protobuf.mysqlx_resultset_pb2 import JSON
import asyncio
import aiohttp
from pages.assignment10.assignment10 import assignment10
from interact_with_DB import interact_db
app = Flask(__name__)
app.register_blueprint(assignment10)
app.secret_key = '123'
from flask import jsonify
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


@app.route('/assignment11/outer_source')
def assignment11_def():
    return render_template('assignment11.html')




@app.route('/assignment11/outer_source/json')
def assignment11_def_json():
    number = request.args['number']
    res = requests.get("https://reqres.in/api/users/{}".format(number))
    response = jsonify(res.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/assignment11/users')
def assignment11_users_def():
        query = 'select  id,name,email from users;'
        users = interact_db(query=query, query_type='fetch')
        response = []
        for user in users:
            response.append({
                "id": user[0],
                "name": user[1],
                "email": user[2]
            })
        return jsonify(users)
        #return render_template('users.html', users=json.dumps(response))

if __name__ == '__main__':
    app.run(debug=True)

