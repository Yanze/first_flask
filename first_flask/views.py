from first_flask import app
from flask import render_template, redirect, url_for, flash
from .forms import MessageForm
# content of the page

messages = []

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', # render : affiche sth on screen
                           title='title_sample',
                           messages = messages)

@app.route("/message", methods=['GET', 'POST'])
def message():
    form = MessageForm()
    if form.validate_on_submit(): # if true, execute this code using POST
        print('Post done: {}'.format(form.new_message.data)) # show input value
        messages.append(form.new_message.data)
        flash('Message sent!')
        return redirect(url_for('index'))
    return render_template('message.html', form=form) # if false, execute using GET
