import imp
from flask import Flask, redirect, render_template, url_for
from wtform_fields import *
from models import *
from flask_login import LoginManager
#Конфигурация приложения
app = Flask(__name__)
app.secret_key = 'позже'

#Конфигурация БД
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
db=SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = Registration_form()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        hashd_pass=pbkdf2_sha512.hash(password)
        #Добавление полей реги в мою БД
        user = User(username=username, password=hashd_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('index.html', form=reg_form)
@app.route('/login.html',methods=['GET','POST'])
def login():
    log_form=Login_form()
    #Если подтверждение произошло и ошибок не возникло, то:
    if log_form.validate_on_submit(): 
        return 'Добро пожаловать'
    return render_template('login.html', form=log_form)
if __name__ == "__main__":
    
    app.run(debug=True)