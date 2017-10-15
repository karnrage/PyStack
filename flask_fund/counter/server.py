from flask import Flask, render_template, request, redirect, session
from pprint import pprint

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


# our index route will handle rendering our form
# @app.route('/')
# def index():
#     if session.get()
#     return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# @app.route('/users', methods=['POST'])
# def create_user():
#    print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
#    session['name'] = request.form['name']
#    session['email'] = request.form['email']
   # redirects back to the '/' route
#    return redirect('/show')
# print request.form
# my_data = request.form['POST']
# @app.route('/show')
# @app.route('/show')
# def show_user():
#    return render_template('user.html')

@app.route('/')  
def index():  
    # session["counter"] = 0
    # print session.has_key("counter")
    if not session.has_key('counter'):
        session['counter'] = 0
        # print str(session['counter'])
        print 'KEY created and reset'
        #, session['counter']
    else:
        session['counter'] += 1
        # print str(session['counter'])
        print 'KEY exists incremented'
        #, session['counter']
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def doublecount():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def doreset():
    session['counter'] = -1
    return redirect('/')

# @app.route('/login')
# def login():
#     session['logged_in'] = True
#     return redirect(url_for('index'))

# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.secret_key = 'ssssshhhhh'
#     app.run()

app.run(debug=True) # run our server
