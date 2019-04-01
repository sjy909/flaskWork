class Book():
    id = None
    name = None
    price = None

    def __str__(self):
        return "编号：%s 书名：%s 价格： %s" % (self.id, self.name, self.price)


from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
engine = create_engine("mysql+mysqlconnector://root:qweasd@localhost/project", encoding='utf8', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)


class Hero(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    heroname = Column(String(20), nullable=False)
    heroderc = Column(String(20), nullable=False)
    userid = Column(Integer, ForeignKey(User.id), nullable=False)
    datil = Column(String(99), default='暂无信息')


if __name__ == "__main__":
    Base.metadata.create_all()
