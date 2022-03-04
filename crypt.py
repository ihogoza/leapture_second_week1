from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


pw_hash = bcrypt.generate_password_hash('ihogoza')
print(pw_hash)
print(bcrypt.check_password_hash(pw_hash, 'ihogoza'))