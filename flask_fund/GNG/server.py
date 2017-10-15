from flask import Flask, render_template, request, redirect, session
from pprint import pprint
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')    
def index():
    if not session.has_key('answer'):
        session['answer'] = random.randrange(0, 101)
        print session['answer'] #KEY CREATED AND RANDOMIZED
    else:
        session.pop('answer')
        session['answer'] = random.randrange(0, 101)
        print session['answer'] #'KEY ERASED, CREATED AND RANDOMIZED'
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def attempt():
    guess = request.form['guess']
    sesh = session['answer']
    print guess
    if (int(guess) >= sesh):
        print "FAIL: Too high, TRY AGAIN!"
        return redirect('/2high')
        
    elif (int(guess) <= sesh):
        print "FAIL: Too low, TRY AGAIN!"
        return redirect('/2low')
    else:
        pass    
        #make winner page  
        
   
    return render_template('/')

#make winner page app.route('/process', methods=['POST'])


app.run(debug=True) # run our server
