from app import db

from sqlalchemy_utils import PasswordType

ROLE_USER = 0
ROLE_ADMIN = 1


class UserAdvertisement(db.Model):
    __tablename__ = 'user_advertisement'
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'),
                        primary_key=True)
    advertisement_id = db.Column(db.Integer(),  db.ForeignKey('advertisement.id'),
                                 primary_key=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(length=64), nullable=False, unique=True)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(12))
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    status = db.Column(db.Boolean(), default=False)

    advertisements = db.relationship('Advertisement', secondary='user_advertisement')


class Advertisement(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=64), nullable=False)
    description = db.Column(db.Text())

    start = db.Column(db.DateTime() or None)
    end = db.Column(db.DateTime() or None)
    status = db.Column(db.Boolean(), default=True)

