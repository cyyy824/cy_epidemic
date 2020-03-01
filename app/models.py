from datetime import datetime
from . import db

class Department(db.Model):

    __tablename__="department"

    id = db.Column(db.Integer,primary_key=True)
    dname = db.Column(db.String(128),unique=True)
    persons = db.relationship('Epidemic',backref="department")

    @staticmethod
    def insert_departments():
        departments = [
            "部门1",
            "部门2",
            "部门3",
            "部门4",
            "部门5",
            "部门6",
            "部门7",
            "部门8",
            "部门9"
        ]
        for d in departments:
            dep = Department(dname=d)
            db.session.add(dep)
        db.session.commit()

class Epidemic(db.Model):
    __tablename__="epidemic"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    health =db.Column(db.String(64))
    goout =db.Column(db.String(64))
    gather =db.Column(db.String(64))
    other =db.Column(db.String(64))
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    department_id = db.Column(db.Integer,db.ForeignKey('department.id'))

    @staticmethod
    def generate_fake(count=10):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            epid = Epidemic(name = forgery_py.name.full_name(),
                            health = "健康",
                            goout = "集团办公",
                            gather = "未聚集",
                            other = "无异常",
                            department_id = 5)
            db.session.add(epid)
        db.session.commit()
        


class Article(db.Model):

    __tablename__="article"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text,unique=True)
    category = db.Column(db.Integer)
    body =db.Column(db.Text)
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    @staticmethod
    def generate_fake(count=20):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            art = Article(title = forgery_py.lorem_ipsum.title(),
                          body=forgery_py.lorem_ipsum.paragraph())
            db.session.add(art)
        db.session.commit()



