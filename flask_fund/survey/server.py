from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('entry_form.html')

@app.route('/process', methods=['POST'])
def create_user():
   print request.form['name']   
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   return redirect('/submitted/' + name + '/'+ location + '/' + language + '/' + comment)

@app.route('/submitted/<name>/<location>/<language>/<comment>')
def submitSuccess(name, location, language, comment):
   print name
   print location
   print language
   print comment
   return render_template('submitted.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)