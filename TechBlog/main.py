import os
from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)

#DATABASE location
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



# ruta odgovorna za logiranje


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle=db.Column(db.String(50))
    author= db.Column(db.String(20))
    date_posted=db.Column(db.DateTime)
    content=db.Column(db.Text)


@app.route('/')
def index():
    posts=BlogPost.query.all()

    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def logIn():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('add'))
    return render_template('login.html', error=error)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    
    post=BlogPost.query.filter_by(id=post_id).one()

    date_posted = post.date_posted.strftime('%B %d %Y')

    return render_template('post.html', post=post, date_posted=date_posted)



@app.route('/add')
def add():
   
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addPost():
    title=request.form['title']
    subtitle=request.form['subtitle']
    author=request.form['author']
    content=request.form['blogContent']
    
    post = BlogPost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
