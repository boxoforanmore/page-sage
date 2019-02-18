from flask import render_template, session, abort, redirect, url_for
from app import app, models
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.google import make_google_blueprint, google
import requests


####################
## Landing Routes ##
####################

@app.route('/')
@app.route('/index')
@app.route('/welcome')
def index():
    return render_template('landing/welcome.html')

@app.route('/about')
def about():
    return render_template('landing/about.html')

@app.route('/terms')
@app.route('/tos')
@app.route('/terms-of-service')
def terms():
    return render_template('landing/terms.html')

@app.route('/privacy')
def privacy():
    return render_template('landing/privacy.html')



##################
## AuthN Routes ##
##################

@app.route('/login')
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    account_info = google.get('/oath2/v2/userinfo')
    if account_info.ok:
        account_info_json = account_info.json()
        return redirect(url_for("user"))
    return render_template('landing/welcome.html')

@app.route('/signup')
def signup():
    return render_template('authn/signup.html')


#################
## User Routes ##
#################

## All user routes should eventually be modified to have dynamic links
## such that the urls are /<username>/profile, etc.
@app.route('/user')
@app.route('/profile')
def profile():
    '''
    resp_json = google.get("/oauth2/v2/userinfo").json()
    if resp_json["hd"] != blueprint.authorization_url_params["hd"]:
        requests.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token["access_token"]}
        )
        session.clear()
        abort(403)
    return "You are @{login} on Google".format(login=resp_json["login"])
    '''
    return render_template('user/profile.html')

## Book should appear as /user/<book>
## Should book be moved to a more general page?
@app.route('/user/book')
def user_book():
    return render_template('user/book.html')

@app.route('/my-shelf')
def my_shelf():
    return render_template('user/my-shelf.html')

@app.route('/user/search')
def search():
    return render_template('user/search.html')

@app.route('/user/settings')
def user_settings():
    return render_template('user/settings.html')


#####################
## Bookclub Routes ##
#####################

## Bookclub routes should eventually be: /bookclub/<club_name>
@app.route('/bookclub')
@app.route('/club')
def bookclub():
    return render_template('bookclub/club.html')

@app.route('/bookclub/forums')
def forums():
    return render_template('bookclub/forums.html')

## This should eventually be <bookclub_name>/<forum_name>
@app.route('/bookclub/forum')
def forum():
    return render_template('bookclub/forum.html')

@app.route('/bookclub/settings')
def bookclub_settings():
    return render_template('bookclub/settings.html')

@app.route('/bookclub/search')
def bookclub_search():
    return render_template('bookclub/search.html')

@app.route('/bookclub/shelf')
@app.route('/bookclub/bookshelf')
def bookclub_shelf():
    return render_template('bookclub/shelf.html')

@app.route('/bookclub/suggestions')
def bookclub_suggestions():
    return render_template('bookclub/suggestions.html')

@app.route('/bookclub/book')
def bookclub_book():
    return render_template('bookclub/book.html')
