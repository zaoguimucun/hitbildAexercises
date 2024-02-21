from flask import Flask, abort, redirect, render_template, request, session, url_for
from flask.views import MethodView
from databaseManager import Student,dbSession

app = Flask(__name__)
app.secret_key = b'hit'

@app.route('/newpage')
def newdital():
    return render_template('newdetail.html')

@app.route('/new',methods=['GET','POST'])
def send_post():
    if request.method== 'GET' :
        return render_template('newdetail.html')
    if request.method== 'POST':
        
        fomr_hurigana = request.form.get('hurigana')
        form_name = request.form.get('kname')
        form_gender = request.form.get('gender')
        form_age = request.form.get('age')
        form_birthday = request.form.get('birthday')
        form_classname = request.form.get('classname')
        form_adress = request.form.get('adress')
        form_email = request.form.get('email')
        form_gmail = request.form.get('gmail')
        form_tel = request.form.get('tel')
        form_bikou = request.form.get('bikou')

        student = Student(
                        hurigana = fomr_hurigana,
                        name=form_name,
                        gender=form_gender,
                        age=form_age,
                        birthday=form_birthday,
                        classname=form_classname,
                        adress=form_adress,
                        email =form_email,
                        gmail = form_gmail,
                        tel =form_tel,
                        bikou=form_bikou
                        )
        
        ses = dbSession()
        ses.add(student)
        ses.commit()
    return redirect(url_for('newdital'))

@app.route('/new',methods=['GET','POST'])
def send_post():
    if request.method== 'GET' :
        return render_template('newdetail.html')
    if request.method== 'POST':
        
        fomr_hurigana = request.form.get('hurigana')
        form_name = request.form.get('kname')
        form_gender = request.form.get('gender')
        form_age = request.form.get('age')
        form_birthday = request.form.get('birthday')
        form_classname = request.form.get('classname')
        form_adress = request.form.get('adress')
        form_email = request.form.get('email')
        form_gmail = request.form.get('gmail')
        form_tel = request.form.get('tel')
        form_bikou = request.form.get('bikou')

        student = Student(
                        hurigana = fomr_hurigana,
                        name=form_name,
                        gender=form_gender,
                        age=form_age,
                        birthday=form_birthday,
                        classname=form_classname,
                        adress=form_adress,
                        email =form_email,
                        gmail = form_gmail,
                        tel =form_tel,
                        bikou=form_bikou
                        )
        
        ses = dbSession()
        ses.add(student)
        ses.commit()
    return redirect(url_for('dital'))



@app.route('/list')
def listload():
    ses= dbSession() 
    students = ses.query(Student).order_by(Student.id).all()
    return render_template('list.html',students=students)

@app.route('/detail/<id>',methods=['GET','POST'])
def leadDb(id):
    if request.method== 'GET' :
        ses = dbSession()
        student = ses.query(Student).get(id).getData()
        return render_template('detail.html',stu=student)
    if request.method== 'POST':
        ses = dbSession()
        student =ses.query(Student).get(id)
        return render_template('detail.html',stu=student)
      

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')




