from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, DataRequired, Length, Email, Regexp,Optional
from ..models import Department

class EpidForm(FlaskForm):

    name = StringField("姓名",validators=[DataRequired()])
    department = SelectField("部门",coerce=int)
    health = StringField("健康情况",validators=[DataRequired()])
    goout = StringField("外出情况",validators=[DataRequired()])
    gather = StringField("聚集情况",validators=[DataRequired()])
    other = StringField("其他",validators=[DataRequired()])
    submit = SubmitField("添加")

    def __init__(self,*args):
        super(EpidForm, self).__init__(*args)
        self.department.choices = [(dep.id,dep.dname) for dep in Department.query.all()]

class EditorForm(FlaskForm):
    title = StringField("标题",validators=[DataRequired()])
    content = TextAreaField('', id = 'content')
    submit = SubmitField('添加')

class EpidDateForm(FlaskForm):
    date = StringField("日期",validators=[DataRequired()])
    submit = SubmitField('查找')
