from orm import model
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:qweasd@localhost/project", encoding='utf8', echo=True)

from sqlalchemy.orm import sessionmaker

session = sessionmaker()()


def insertUser(username, password):
    session.add(model.User(username=username, password=password))
    session.commit()
    session.close()


def checkUser(username, password):
    result = session.query(model.User).filter(model.User.username == username).filter(model.User.password==password).first()
    if result:
        return True
    else:
        return False


def insertHero(hero, herodesc):
    session.add(model.Hero(heroname=hero, heroderc=herodesc))
    session.commit()
    session.close()


def selectHero():
    result = session.query(model.Hero).all()
    return result


def selectHeroOne(heroname):
    result = session.query(model.Hero).filter(model.Hero.id == heroname).first()
    return result


def deleteHero(heroid):
    hero = session.query(model.Hero).filter(model.Hero.id == heroid).first()
    session.delete(hero)
    hero_all_id = get_hero_id()
    auto_increment_id(hero_all_id)
    session.commit()
    session.close()


def inserHero(heroname, derchero,detail,userid):
    session.add(model.Hero(heroname=heroname, heroderc=derchero,datil=detail, userid=userid))
    hero_all_id = get_hero_id()
    auto_increment_id(hero_all_id)
    session.commit()
    session.close()


def get_hero_id():
    hero = session.query(model.Hero).all()
    return hero


def auto_increment_id(all_id_list):
    i = 0
    for hero in all_id_list:
        i += 1
        hero.id = i
