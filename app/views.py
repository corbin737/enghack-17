from flask import render_template, flash, redirect
from app import app
from .forms import MessageForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    form = MessageForm()
    if form.validate_on_submit():
        flash('Message sent to' + str(form.recipient.data))
        return redirect('/index')
    return render_template('message.html',
                            title='Send Message',
                            form=form)
