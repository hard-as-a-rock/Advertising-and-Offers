from flask_wtf import Form

from wtforms import StringField, DateTimeField, ValidationError, IntegerField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, optional, Email, Length, NumberRange, EqualTo

from models import User, Advertisement


class UniqueValidator(object):

    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'Already exists'
        self.message = message

    def __call__(self, form, field):
        existing = self.model.query.filter(self.field == field.data).first()
        if existing:
            raise ValidationError(self.message)


class UserForm(Form):
    class Meta:
        model = User

    first_name = StringField(
        'first_name',
        validators=[
            DataRequired(),
            Length(max=128)
        ]
    )
    last_name = StringField(
        'last_name',
        validators=[
            DataRequired(),
            Length(max=128)
        ]
    )
    nickname = StringField(
        'nickname',
        validators=[
            DataRequired(),
            Length(max=128),
            UniqueValidator(User, User.nickname)
        ]
    )
    password = PasswordField(
        'password',
        validators=[
            DataRequired()
        ]
    )
    confirm_password = PasswordField(
        'repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )
    email = StringField(
        'email',
        validators=[
            DataRequired(),
            Length(max=255),
            Email(),
            UniqueValidator(User, User.email)
        ]
    )
    phone = StringField(
        'phone',
        validators=[
            DataRequired(),
            Length(min=5, max=12),
            UniqueValidator(User, User.phone)]
    )
