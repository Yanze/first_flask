from first_flask import app
from flask import render_template
# content of the page

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Dragon', lengend='Gragon Glass')

@app.route("/coucou")
def coucou():
    print(' coucou Requested')
    return render_template('coucou.html')

