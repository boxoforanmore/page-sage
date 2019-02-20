from flask import render_template
from app import app
from app.forms import SearchForm


###########
## Forms ##
###########

def search_form(form):
    if form.validate_on_submit():
        return redirect('/user/search')


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
    return render_template('authn/login.html')

@app.route('/signup')
def signup():
    return render_template('authn/signup.html')


#################
## User Routes ##
#################

## All user routes should eventually be modified to have dynamic links
## such that the urls are /<username>/profile, etc.
@app.route('/user')
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = SearchForm()
    search_form(form)
    return render_template('user/profile.html', form=form)

## Book should appear as /user/<book>
## Should book be moved to a more general page?
@app.route('/user/book', methods=['GET', 'POST'])
def user_book():
    form = SearchForm()
    search_form(form)
    return render_template('user/book.html', form=form)

@app.route('/my-shelf', methods=['GET', 'POST'])
def my_shelf():
    form = SearchForm()
    search_form(form)
    return render_template('user/my-shelf.html', form=form)

@app.route('/user/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Search requested for {}'.format(form.search_item.data))
        return redirect('/user/search')
    return render_template('user/search.html', form=form)

@app.route('/user/settings', methods=['GET', 'POST'])
def user_settings():
    form = SearchForm()
    search_form(form)
    return render_template('user/settings.html', form=form)


#####################
## Bookclub Routes ##
#####################

## Bookclub routes should eventually be: /bookclub/<club_name>
@app.route('/bookclub')
@app.route('/club', methods=['GET', 'POST'])
def bookclub():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/club.html', form=form)

@app.route('/bookclub/forums', methods=['GET', 'POST'])
def forums():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/forums.html', form=form)

## This should eventually be <bookclub_name>/<forum_name>
@app.route('/bookclub/forum', methods=['GET', 'POST'])
def forum():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/forum.html', form=form)

@app.route('/bookclub/settings', methods=['GET', 'POST'])
def bookclub_settings():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/settings.html', form=form)

@app.route('/bookclub/search', methods=['GET', 'POST'])
def bookclub_search():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/search.html', form=form)

@app.route('/bookclub/shelf', methods=['GET', 'POST'])
@app.route('/bookclub/bookshelf')
def bookclub_shelf():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/shelf.html', form=form)

@app.route('/bookclub/suggestions', methods=['GET', 'POST'])
def bookclub_suggestions():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/suggestions.html', form=form)

@app.route('/bookclub/book', methods=['GET', 'POST'])
def bookclub_book():
    form = SearchForm()
    search_form(form)
    return render_template('bookclub/book.html', form=form)
