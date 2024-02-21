from flask import Flask, redirect, render_template, session, url_for
from flask_login import LoginManager, login_required 
from databaseManagement import Student
app = Flask(__name__)
app.secret_key = b'hit'
login_manager = LoginManager()
login_manager.init_app(app)
# ログインシステムの登録
from loginSystem import loginSystem
app.register_blueprint(loginSystem)
# indexページの表示
@app.route('/')
@login_required
def index():
    return redirect(url_for('list'))
@app.route('/list')
def list():
    students = Student.get() 
    return render_template('list.html',students=students)

# ログインが必要なページで未ログインの場合はログインページにリダイレクト
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('LoginSystem.LoginSystem'))
# リクエストのたびにセッションの寿命を更新する
@app.before_request
def before_request():
    session.permanent = True
    #app.permanent_session_lifetime = timedelta(minutes=15) # セッションの寿命を15分に設定
    session.modified = True












