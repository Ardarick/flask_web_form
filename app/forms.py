from wtforms import Form, StringField


class MyForm(Form):
    name = StringField('Name')
