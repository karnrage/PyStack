from flask import Flask, render_template, request, redirect    # Import Flask to allow us to create our app.
app = Flask(__name__)                       # Global variable __name__ tells Flask whether or not we are running the file
                                            # directly, or importing it as a module.
@app.route('/')                             # The "@" symbol designates a "decorator" which attaches the following
def hello_world():
    return render_template('landing_form.html')  # function to the '/' route. This means that whenever we send a request to
                                            # localhost:5000/ we will run the following "hello_world" function.
                                            # Return the string 'Hello World!' as a response.
@app.route('/process', methods=['POST'])
def process():
    print request.form['name']

    name = request.form['name']
    email = request.form['email']
    return redirect('/show/' + name)

# @app.route('/dojos/new')
# def dojo_new():
#     return render_template('dojos.html')

#############done above

app.run(debug=True)      # Run the app in debug mode.