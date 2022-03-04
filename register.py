from flask import Flask, redirect, session, url_for
# from flask_dance.contrib.twitter import make_twitter_blueprint, twitter 
from flask_dance.contrib.github import make_github_blueprint, github
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
import os 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobeasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '0'

# twitter_blueprint = make_twitter_blueprint(api_key='Wxheh706myGRPdIzg1UG8NCmD', api_secret='z2gPTdT8v1pCTNEX7xxtf0bbqLwLJgfiqgdgDa03GTf7M5m13T')

github_blueprint = make_github_blueprint(client_id='****', client_secret='*****')

# app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

github_blueprint.storage = SQLAlchemyStorage(OAuth, db.session, user=current_user, user_required=False)

# @app.route('/twitter')
# def twitter_login():
#     if not twitter.authorized:
#         return redirect(url_for('twitter.login'))

#     account_info = twitter.get('account/settings.json')
#     account_info_json = account_info.json()

#     return '<h1>Your Twitter name is @{}'.format(account_info_json['screen_name'])

@app.route('/github')
def github_login():
    # if not github.authorized:
    return redirect(url_for('github.login'))
    

    # account_info = github.get('/user')
    # account_info_json = account_info.json()
    # return '<h1>Your Github name is {}'.format(account_info_json['login'])



@oauth_authorized.connect_via(github_blueprint)
def github_logged_in(blueprint, token):

    account_info = blueprint.session.get('/user')

    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['login']

        query = User.query.filter_by(username=username)

        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        login_user(user)




@app.route('/')
@login_required
def index():
    return '<h1> This is index and You are logged in as {}</h1>'.format(current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

