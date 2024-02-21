from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_login import UserMixin

# Modelの定義
db = create_engine('sqlite:///db.db')
Session = sessionmaker(bind=db)
ses = Session()

Base = declarative_base()

class BaseMixin(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    # CRUD操作
    # データの追加
    @classmethod
    def add(cls, **kwargs):
        data = cls(**kwargs)
        ses.add(data)
        ses.commit()
        ses.close()

    # データの読み込み
    @classmethod
    def get(cls, **kwargs):
        if not kwargs:
            all_data = ses.query(cls).all()
        else:
            all_data = ses.query(cls).filter_by(**kwargs).all()
        if all_data is None:
            return None
        return [data.getData() for data in all_data]

    # データの更新
    @classmethod
    def update(cls, id, **kwargs):
        data = ses.query(cls).filter_by(id=id).first()
        for key, value in kwargs.items():
            setattr(data, key, value)
        ses.commit()
        ses.close()
    
    # データの削除
    @classmethod
    def delete(cls, id):
        data = ses.query(cls).filter_by(id=id).first()
        ses.delete(data)
        ses.commit()
        ses.close()

# 生徒テーブル
class Student(BaseMixin):
    __tablename__ = 'student'
    name = Column(String(20))
    kanme =Column(String(30))
    gender = Column(String(5))
    age = Column(Integer)
    birthday =Column(String(30))
    adress =  Column(String(50))
    email = Column(String(50))
    gmail = Column(String(50))
    tel = Column(String(20))
    bikou = Column(String(400))



    # データを辞書型で取得する
    def getData(self):
        return {
            'id': int(self.id),
            'name': str(self.name),
            'kanme':str(self.kanme),
            'gender': str(self.gender),
            'age': int(self.age),
            'birthday':str(self.birthday),
            'adress':str(self.adress),
            'email':str(self.email),
            'gmail':str(self.gmail),
            'tel':str(self.tel),
            'bikou':str(self.bikou)


        }

# ユーザーテーブル
class User(BaseMixin, UserMixin):
    __tablename__ = 'user'
    
    loginpass  = Column(String(20))

    # データを辞書型で取得する
    def getData(self):
        return {
            'id': int(self.id),
            'loginpass': str(self.loginpass)
        }


# テーブルの作成
Base.metadata.create_all(bind=db)

# ユーザーの追加
if not User.get(): # データがない場合
    User.add(id=1, loginpass ='admin')

# 生徒の追加
if not Student.get(): # データがない場合
    Student.add(name='藤田',kanme='フジタ', gender='男', age=38, birthday='19851215',adress='九条南2-6-10',email='yoalnfdfoaka.jp',gmail='kjflkajofjfffa.jp',tel='0897568885',bikou='青紙')