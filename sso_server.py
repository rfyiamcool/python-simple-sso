#coding: utf8
import os
from datetime import timedelta
from flask import Flask, session, render_template, request, redirect
import urllib

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=30 * 24 * 60 * 60)

@app.route('/')
def toindex():
    return "nima"

@app.route('/login')
def login():
    session.permanent = True
    referer = request.args.get('referer', None)
    if referer is not None:
        referer = referer.strip()
    if 'name' in session:
        if referer is not None:
            return redirect(referer + '?ticket=' + _makeTicket())
    return render_template('login.html', **dict(referer=referer))

@app.route('/dologin')
def doLogin():
    '''这里其实忽略了判断是否登录的流程'''
    session.permanent = True
    referer = request.args.get('referer', None)
    if referer is not None:
        referer = urllib.unquote(referer.strip())
    #不实现登录功能，直接设置登录态
    _setLoginState()
    if referer:
        return redirect(referer + '?ticket=' + _makeTicket())
    else:
        return 'error'

def _setLoginState():
    session['name'] = 'goal'

def _makeTicket():
    '''生成ticket，这里只是简单返回用户名，真实场景中可以使用des之类的加密算法'''
    return 'goal'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int("8888"),debug=True)
