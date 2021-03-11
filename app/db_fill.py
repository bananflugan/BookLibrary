# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root_email@domain.example', password='password', major='administrator',
             headline=u"Temporary administrator", about_me=u"Info about me.")
user1 = User(name=u'user', email='user_email@domain.example', password='123456')

book1 = Book(title=u"Test Book", subtitle=u"Subtitle", author=u"Miguel Grinberg", isbn='9787115373991',
             tags_string=u"Tags", image='http://img3.douban.com/lpic/s27906700.jpg',
             summary=u"""
Summary text about the book.
""")

logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
