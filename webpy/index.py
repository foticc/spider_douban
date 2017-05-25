# -*- coding: utf-8 -*-
import web
from web import template
from url import urls
import db_mysql
#debug=false
web.config.debug=False
#session time out
web.config.session_parameters['timeout']=600

app = web.application(urls,globals())
session = web.session.Session(app,web.session.DiskStore('sessions'),initializer={'user':''})
ren = template.render('templates')

class login:
    def GET(self):
        return ren.login(msg='')


class index:
    def POST(self):
        uap = web.input()
        password = db_mysql.getpass(uap['username'])
        if password:
            password = password[0]
        if any(password):
            if uap['password']==password['password']:
                session.user = uap['username']
                return ren.home(uap['username'])
            else:
                return ren.login(msg=1)
        else:
            return ren.login(msg=2)
    def GET(self):
        if session.user =='':
            return ren.login(msg='')
        else:
            return ren.home(session.user)

class article:
    def POST(self):
        uap = web.input()
        title = uap['title']
        content = uap['content']
        tid =  db_mysql.add_article(title,content)
        if tid!=None:
            return ren.add(msg='success')
        else:
            return ren.add(msg='fail')

class list:
    def GET(self):
        #input(page) args is default when not page is send page=0
        page = web.input(page=0)['page']
        art_list = db_mysql.get_article_list(int(page))
        count = db_mysql.get_article_count()
        return ren.list(art_list,count[0]['num'])

class add:
    def GET(self):
        return ren.add(msg='')


if __name__ == '__main__':
    app.run()