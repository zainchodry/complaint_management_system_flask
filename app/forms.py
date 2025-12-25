from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Login")

class ComplaintForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Submit Complaint")

class CommentForm(FlaskForm):
    message = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Add Comment")

class AdminReviewForm(FlaskForm):
    admin_review = TextAreaField("Review / Comment", validators=[DataRequired()])
    submit_approve = SubmitField("Approve")
    submit_reject = SubmitField("Reject")
