from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    passwod = StringField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Войти')


def validate_username(self, username):
    user = User.query.filter_by(username=username.data)

    if user:
        flash('Это имя уже занято. Пожалуйста выберите другое', 'danger')
        raise ValidationError('That username is taken.Please choose a different one')


def validate_email(self, email):
    user = User.query.filter_by(email=email.data)

    if user:
        flash('Это имя уже занято. Пожалуйста выберите другое', 'danger')
        raise ValidationError('That username is taken.Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')