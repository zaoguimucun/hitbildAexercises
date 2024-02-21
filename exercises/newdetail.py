from flask import Blueprint, redirect, render_template, request, session
from flask.views import MethodView

newDetail = Blueprint('detail',__name__,url_prefix='/detail')

class NewDetail(MethodView):
    def get(self):
        # 詳細取得処理
        return render_template('newdetail.html')
    
    def post(self):
        # 挿入処理、更新処理
        return render_template('newdetail.html')

newDetail.add_url_rule('/new',view_func=NewDetail.as_view('newDetail'))