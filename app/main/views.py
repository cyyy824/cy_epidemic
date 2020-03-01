# coding:utf8

from flask import Flask,url_for,render_template,request,redirect
from . import main
from .. import db
from ..models import Department,Epidemic,Article
from sqlalchemy import or_,and_,extract
from .forms import EpidForm,EditorForm
import json
import datetime

@main.route('/status')
def status_list():
    nowdate=datetime.datetime.now()
    sdate = request.args.get('sdate') or nowdate.strftime("%Y-%m-%d")

    date_tuple = datetime.datetime.strptime(sdate, "%Y-%m-%d")
    epids = Epidemic.query.filter(and_(
                extract("year", Epidemic.created) == date_tuple.year,
                extract("month", Epidemic.created) == date_tuple.month,
                extract("day", Epidemic.created) == date_tuple.day)).all()
    return render_template('status.html', epids=epids)

@main.route('/addstatus', methods=('GET', 'POST'))
def add_status():
    form = EpidForm()
    if form.validate_on_submit():
        name = form.name.data
        health = form.health.data
        goout = form.goout.data
        gather = form.gather.data
        other = form.other.data
        department = form.department.data
        print(form.department.data)
        epid = Epidemic(name=name, health=health,goout=goout,gather=gather,other=other,department_id=department)
        db.session.add(epid)
        db.session.commit()
        return redirect(url_for('.status_list'))
    return render_template('addstatus.html',form=form)

@main.route('/editstatus')
def edit_status():
    pass

@main.route('/news')
def news_list():
    rs = Article.query.all()
    return render_template('news.html', news=rs)

@main.route('/addnews', methods=('GET', 'POST'))
def add_news():
    form = EditorForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.content.data
        art = Article(title=title,body=body)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for('.news_list'))
    return render_template('addnews.html',form=form)

@main.route('/editnews')
def edit_news():
    pass

@main.route('/shownews/<newsid>')
def show_news(newsid):
    news = Article.query.filter_by(id=newsid).first_or_404()
    return render_template('shownews.html', title=news.title, body= news.body)



