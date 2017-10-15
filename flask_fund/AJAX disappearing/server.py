from flask import Flask, render_template, request, redirect    # Import Flask to allow us to create our app.
app = Flask(__name__)                       # Global variable __name__ tells Flask whether or not we are running the file
                                            # directly, or importing it as a module.
@app.route('/')                             # The "@" symbol designates a "decorator" which attaches the following
def landing():
    return render_template('index.html')  

    # function to the '/' route. This means that whenever we send a request to
                                            # localhost:5000/ we will run the following "hello_world" function.
                                            # Return the string 'Hello World!' as a response.
# @app.route('/ninja')
# def familyPic():
#     return render_template('ninja.html')

# @app.route('/ninja/<color>')
# def ninja_color(color):
#     if (color == "blue"):
#         return render_template('blue.html')
#     elif (color == "orange"):
#         return render_template('orange.html')
#     elif (color == "red"):
#         return render_template('red.html')
#     elif (color == "purple"):
#         return render_template('purple.html')
#     else:
#         return render_template('notapril.html')

app.run(debug=True)
#############done above
    # name = request.form['name']
    # email = request.form['email']
    # return redirect('/show/' + name)

# @app.route('/dojos/new')
# def dojo_new():
#     return render_template('dojos.html')



# app.run(debug=True)      # Run the app in debug mode.