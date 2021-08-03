from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError


class contactForm(FlaskForm):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter a valid email."), validators.email("Please enter a valid email.")])
    subject = TextField("Subject (Optional)")
    message = TextAreaField("Message", [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
