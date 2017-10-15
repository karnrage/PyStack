from flask import Flask, render_template, request, redirect, session, flash
import re
import md5
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')

print mysql.query_db("SELECT * FROM users")

app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    errors = []
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # password = md5.new(request.form['password']).hexdigest()
    password = request.form['password']


    existingEmails = mysql.query_db("SELECT * FROM users WHERE email = '{}' ".format(email) ) 

    if len(request.form['email']) < 1:
        errors.append("Email cannot be empty!")

    if len(existingEmails) > 0:
        flash("Email Already Exists! Try logging in!")
        return redirect('/login')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")

    # ----------------------------------------------
    if len(request.form['first_name']) < 1:
        errors.append("First Name cannot be empty!")

    if not NAME_REGEX.match(first_name):
        errors.append("First Name Cannot Contain Any Numbers!")

    # ---------------------------------------
    if len(request.form['last_name']) < 1:
        errors.append("Last Name cannot be empty!")

    if not NAME_REGEX.match(last_name):
        errors.append("Last Name Cannot Contain Any Numbers!")

    # ---------------------------------------
    if len(request.form['password']) < 1:
        errors.append("password cannot be empty!")

    if request.form['password'] < 3:
        errors.append("Password has to be more than 3 characters!")

    # ----------------------------------------
    if request.form['confirm_password'] == request.form['password']:
        print ('match')
    else:
        errors.append("Password do not match!")
    # ----------------------------------------
    if len(errors) > 0:
        flash(errors)

    else:
        mysql.query_db ("INSERT INTO users (email, first_name, last_name, password) VALUES ('{}','{}','{}','{}')".format(email,first_name,last_name,password))
        flash ('You have been successfully registered! Now, log in.')
        return redirect('/')

    return redirect('/')

@app.route('/login', methods=['GET'])
def login():
    #Get to retrieve the page 
    return render_template('login.html')

@app.route('/signIn', methods=['POST'])
def SignIn():
    email = request.form['email']
    password = request.form['password']

    users = mysql.query_db("SELECT * FROM users WHERE email = '{}' ".format(email) ) 
    if len(users) > 0:
        user = users[0]

        if user['password'] == password:
            print "success"
            session['first_name'] = user['first_name']
            flash('Yay, you are logged in')
            return redirect('/alreadyin')
        #Needed two else statements?
        else:
            print "Password Invalid"
            flash('Password Invalid')
    else:
        print "no such user"
        flash('No Such User!')

    return redirect('/login')

@app.route('/alreadyin')
def alreadylogged():
    
    return render_template('alreadysignedin.html')

@app.route('/logout')
def logout():

    return render_template('alreadysignedin.html')
    

app.run(debug=True)