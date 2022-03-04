from flask import g, request
from flask import Flask
from flask_babelex import Babel, format_datetime
# from flask.ext.babelex import format_datetime
from datetime import datetime




app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@app.route('/')
@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['de', 'fr', 'en'])

@app.route('/timezone/')
@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
    else:
        return format_datetime(datetime(1987, 3, 5, 17, 12))
    
    
if __name__ == "__main__":
    app.run(debug=True)

# print(get_locale())
# print(get_timezone())

# print(format_datetime(datetime(1987, 3, 5, 17, 12)))





