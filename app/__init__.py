# app/__init__.py
from flask import Flask, render_template, request, redirect, url_for
from .config import Config
from .models import db, Message
import re

app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.template_filter('nl2br')
def nl2br(value):
    return re.sub(r'(\r\n|\r|\n)', '<br>', value)

@app.route('/')
def chat():
    messages = Message.query.order_by(Message.timestamp).all()
    return render_template('chat.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    username = request.form.get('username')
    content = request.form.get('content')
    if username and content:
        new_message = Message(username=username, content=content)
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for('chat'))