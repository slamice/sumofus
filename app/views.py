from flask import render_template, flash, redirect, session, url_for, request, g
from app import app


@app.route('/')
@app.route('/About-You')
def index():
    bgStyle='css/sumofus.css'
    return render_template('AboutYou.html',
                           title='About You',
                           bgStyle=bgStyle)


@app.route('/AboutMe')
def aboutMe():
    bgStyle='css/issam.css'
    return render_template('AboutMe.html',
                           title='About Me',
                           bgStyle=bgStyle)

@app.route('/AboutUs')
def aboutUs():
    bgStyle='other'
    return render_template('AboutUs.html',
                           title='About Us',
                           bgStyle=bgStyle)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500