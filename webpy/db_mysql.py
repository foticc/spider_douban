import web
import json



db = web.database(dbn='mysql',host='127.0.0.1', user='root', pw='', db='data',charset='utf8',use_unicode=0)

table = 'user'


def getpass(username):
    user = dict(user=username)
    password = db.select(table,user,where='username=$user',what='password')
    return password

def add_article(title,content):
    tid = db.insert('article',title=title,content=content,ctime=web.SQLLiteral('NOW()'))
    return tid

def get_article_list(page):
    #every page show 10 record
    row = 10
    article_list = db.select('article',what='tid,title,ctime',offset=page*row,limit=row)
    return article_list

def get_article_count():
    count = db.query('select count(1) as num from article')
    return count
