import web



db = web.database(dbn='mysql',host='127.0.0.1', user='root', pw='', db='data')

table = 'user'


def getpass(username):
    user = dict(user=username)
    password = db.select(table,user,where='username=$user',what='password')
    return password

def add_article(title,content):
    tid = db.insert('article',title=title,content=content,ctime=web.SQLLiteral('NOW()'))
    return tid
