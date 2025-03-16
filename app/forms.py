from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired, DataRequired, Regexp
from flask_wtf.file import FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class UploadForm(FlaskForm):
    file = FileField('Image File', validators=[
        DataRequired(),
        Regexp(r'^[^/\\]\.jpg$|^[^/\\]\.png$', message=".jpg and .png files")
    ])
