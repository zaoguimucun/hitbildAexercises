from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Modelの定義
Base = declarative_base()
class Student(Base):
    __tablename__ ='student'
    id = Column(Integer, primary_key=True)
    hurigana=Column(String(50))
    name = Column(String(20))
    gender = Column(String(10))
    age = Column(Integer)
    classname= Column(String(20))
    birthday = Column(String(20))
    adress = Column(String(100))
    email = Column(String(40))
    gmail = Column(String(40))
    tel = Column(String(15))
    bikou = Column(String(400))

     #　カラム内のデータの取得(辞書型) 
    def getData(self):
        return {
            'id':int(self.id),
            'hurigana':str(self.hurigana),
            'name':str(self.name),
            'gender':str(self.gender),
            'age':int(self.age),
            'classname':str(self.classname),
            'birthday':str(self.birthday),
            'adress':str(self.adress),
            'email':str(self.email),
            'gmail':str(self.gmail),
            'tel':str(self.tel),
            'bikou':str(self.bikou)
                    }
    
db = create_engine('sqlite:///DB/ds2.db',echo=True)
Base.metadata.create_all(bind=db)
dbSession = sessionmaker(bind=db)

if __name__ == "__main__":
# エンジンオブジェクトの生成
    ses = dbSession()
    res = ses.query(Student).all()

    for data in res:
        dictData = data.getData()
        print('id:'+str(dictData['id']))
        print('name:'+str(dictData['name']))
        print('gender:'+str(dictData['gender']))
        print('age:'+str(dictData['age']))

    # データの挿入
    p1 = Student()
    ses.add(p1)
    ses.commit()

    # データベースから接続を切る
    ses.close()
