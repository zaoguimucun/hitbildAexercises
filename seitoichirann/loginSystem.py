from flask import Blueprint, redirect, render_template, request, url_for
from flask.views import MethodView
from flask_login import current_user, login_user, logout_user
from databaseManagement import User, ses
from main import login_manager
# ブループリントの準備
loginSystem = Blueprint('LoginSystem', __name__, url_prefix='/LoginSystem')
# ログインシステムクラス
class LoginSystem(MethodView):
    def get(self):
        # ログイン済みの場合はトップページにリダイレクト
        if current_user.is_authenticated:
            return redirect('/')
        print(1)
        return render_template('login.html', error=False)
    
    def post(self):
        userid = request.form.get('id')
        password = request.form.get('password')
        # ユーザーの照合
        user = ses.query(User).filter_by(id=userid, loginpass=password).first()
        if user:
            login_user(user)
            return redirect('/')
        print(2)
        return render_template('login.html', error=True)
    @login_manager.user_loader
    def load_user(userid):
        return ses.query(User).get(userid)
@loginSystem.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('LoginSystem.LoginSystem'))
loginSystem.add_url_rule('/login', view_func=LoginSystem.as_view('LoginSystem'))














