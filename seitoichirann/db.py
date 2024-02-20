from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# エンジンオブジェクトの作成
eng = create_engine('sqlite:///ds.db')

# ベースクラスの作成
base = declarative_base()

# モデルクラスの作成
class Test_data(base):
    __tablename__ = 'student'

    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    classname = Column(String(30))
    gender =  Column(String(5))

    # データを辞書型で取得する
    def getData(self):
        return {
            'id':int(self.id),
            'name':str(self.name),
            'classname':str(self.classname),
            'age':int(self.age),
            'gender':str(self.gender),
        }


# Sessionの作成
mak = sessionmaker(bind=eng)
ses = mak()

# for文で１レコードずつ取得
for r in ses.query(Test_data).order_by(Test_data.id).all():
    r=r.getData()
    print('id:'+str(r['id']))
    print('name:'+str(r['name']))
    print('gender:'+str(r['gender']))
    print('age:'+str(r['age']))


# #対象レコードをすべてリストで取得
# list_a = ses.query(Test_data).order_by(Test_data.id).all()
# for r in list_a:
#     print(r.id, r.name, r.price)

# 終了
ses.close()
