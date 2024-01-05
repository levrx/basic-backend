# make sure all your html and css files are placed in a folder named templates (idk why it just works)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # Change this to your main html file name

if __name__ == '__main__':
    app.run(debug=True) # Set to False to remove un-necessary output in console
