from flask import render_template, flash, redirect, jsonify, send_file, request
from app import app, db, models
from .forms import MessageForm

@app.route('/')
@app.route('/dashboard')
def dashboard():
    user = {'nickname': 'Miguel'}  # fake user
    messages = models.Message.query.all()
    broadcasts = models.Broadcast.query.all()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           messages=messages,
                           broadcasts=broadcasts)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    messages = models.Message.query.all()
    form = MessageForm()
    if form.validate_on_submit():
        m = models.Message(
            recipient=form.recipient.data,
            message=form.message.data
        )
        db.session.add(m)
        db.session.commit()
        flash('Message sent to ' + str(form.recipient.data))
        return redirect('/messages')
    return render_template('message.html',
                            title='Send Message',
                            form=form,
                            messages=messages)

@app.route('/get_data')
def get_data():
    messages = models.Message.query.all()
    return jsonify([
        {'recipient': m.recipient, 'message': m.message}
        for m in messages
    ])

@app.route('/post_data', methods=['POST'])
def post_data():
    res = request.data
    data = json.loads(res)
    m = models.Broadcast(
        message=data.content[0].message
    )
    db.session.add(m)
    db.session.commit()
    return redirect('/')

@app.route('/download')
def download():
    return send_file('../Assets.zip', as_attachment=True)
