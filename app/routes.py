from app.blueprints.auth.models import User
from app import db
from flask import render_template, request, redirect, url_for, flash, current_app as app
from app.models import Post



@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        p = Post(
                body=request.form.get('body'),
                user_id=1
            )
        db.session.add(p)
        db.session.commit()
        flash('Post created successfully', 'success')

        return redirect(url_for('home'))

    context = {
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    # return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/route1')
def route1():
    return render_template('route1.html')

@app.route('/route2')
def route2():
    return render_template('route2.html')

@app.route('/route3')
def route3():
    return render_template('route3.html')
