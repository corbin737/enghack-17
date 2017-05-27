from flask import render_template, flash, redirect, jsonify
from app import app, db, models
from .forms import MessageForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    messages = models.Message.query.all()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           messages=messages)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    form = MessageForm()
    if form.validate_on_submit():
        m = models.Message(
            recipient=form.recipient.data,
            message=form.message.data
        )
        db.session.add(m)
        db.session.commit()
        flash('Message sent to ' + str(form.recipient.data))
        return redirect('/index')
    return render_template('message.html',
                            title='Send Message',
                            form=form)

@app.route('/get_data')
def get_data():
    messages = models.Message.query.all()
    return jsonify([
        {'recipient': m.recipient, 'message': m.message}
        for m in messages
    ])
