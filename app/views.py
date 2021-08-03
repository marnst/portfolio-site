from flask import render_template, request, flash
from app import app
from app.forms import contactForm
from flask_mail import Message, Mail
import os

mail = Mail()
app.secret_key = os.getenv('SECRET_KEY')

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'arnstbot@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')

mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')

def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = contactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required')
            return render_template('contact.html', form = form)
        else:
            psub = form.subject.data
            subject = "You got a Message!" if (psub == None or psub =='') else psub



            msg = Message(subject, sender = 'arnstbot@gmail.com', recipients = ['marnstt@gmail.com'])
            msg.body = """
            From: %s <%s>

            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form = form)
