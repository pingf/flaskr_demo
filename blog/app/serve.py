from flask import Flask, render_template, session, abort, request, flash, redirect, url_for
from sqlalchemy.orm import Session

from blog.db import Post

app = Flask('blog')#, template_folder='blog/templates', static_folder='blog/static')

@app.route('/add', methods=['POST'])
def add_post():
    if not session.get('logged_in'):
        abort(401)
    ses = Session()
    post = Post(title=request.form['title'], content=request.form['content'])
    ses.add(post)
    ses.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_posts'))


@app.route('/')
def show_posts():
    ses = Session()
    query = ses.query(Post).order_by(Post.create_at.desc())
    posts = query.all()
    return render_template('show_posts.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_posts'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_posts'))



if __name__ == '__main__':
    app.config.update(dict(
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    #
    #
    app.run()