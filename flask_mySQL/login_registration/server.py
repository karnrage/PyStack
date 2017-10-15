from flask import Flask, render_template, redirect, request, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import datetime
import time
app = Flask(__name__)
app.secret_key= 'KeepItSecretKeepItSafe'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print mysql.query_db("SELECT * FROM email")

@app.route('/')
def index():
    # query = "select id, name, age, concat( monthname(created_at), ' ', Day(created_at)) as friend_date, year(created_at) as year_name FROM friends"
    email = mysql.query_db("SELECT * FROM email")
    return render_template('index.html', email = email)

@app.route('/process', methods=["POST"])
def create_email_():
    email = request.form ['email']
    if len(request.form['email']) < 1:
        flash("email cannot be empty!")
        return redirect('/')
    else:
        flash("The email address you entered{} is completely valid!!".format(request.form['email']))
        # flash("The email address you entered{} ".format(request.form['email']) )
    created_at = datetime.datetime.now()
    mysql.query_db("INSERT INTO email (email, created_at)VALUES('{}','{}')".format(email, created_at))
    return redirect('/update')

@app.route('/update')
def update():
    all_email = mysql.query_db("SELECT * FROM email")
    return render_template('/success.html', all_email=all_email)

app.run(debug=True)
