from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ihogozavava14@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    msg = Message("Hello",
                  sender="ihogozavava14@gmail.com",
                  recipients=["ihogozavava13@gmail.com", "nkakayves515@gmail.com"])
    
    mail.send(msg)
    return 'Message sent'

if __name__ == '__main__':
    app.run()