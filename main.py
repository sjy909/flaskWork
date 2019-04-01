from flask import Flask, render_template, request, redirect, make_response
from orm import model, ormmanger as manger

app = Flask(__name__)


# 将http://127.0.0.1:5000/和index视图绑定
@app.route('/')
def index():
    user = request.cookies.get("name")
    return render_template('index.html', userinfor=user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        manger.insertUser(username, password)
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        result = manger.checkUser(username, password)
        print(result)
        if result:

            infoarray = manger.selectHero()
            res = make_response(render_template('choice.html', userfor=username, infoarray= infoarray))
            res.set_cookie("name", username)
            return res
        else:
            return render_template('index.html')


@app.route('/choice<userfor>')
def choice(userfor):
    infoarray = manger.selectHero()
    return render_template('choice.html', userfor=userfor, infoarray=infoarray)


@app.route('/choice<int:useid>')
def deleteHero(useid):
    manger.deleteHero(useid)
    infoarray = manger.selectHero()
    userfor = request.cookies['name']
    return render_template('choice.html', userfor=userfor, infoarray=infoarray)


@app.route('/quit')
def quit_login():
    res = make_response(redirect("/"))
    res.delete_cookie("name")
    return res



@app.route('/detail/<int:num>')
def detail(num):
    num -= 1
    infoarray = manger.selectHero()[num]
    datil = infoarray.datil
    userfor = request.cookies['name']
    return render_template('detail.html', id=infoarray.heroname, detail= datil, userfor = userfor)


@app.route('/update/<int:hero>', methods=['GET', 'POST'])
def update(hero):
    if request.method == 'GET':
        hero_info = manger.selectHeroOne(hero)

        return render_template('update.html', hero=hero_info)

    elif request.method == 'POST':
        hero_info = manger.selectHeroOne(hero)
        hero_info.heroname = request.form["heroname"]

        hero_info.datil = request.form["datil"]

        hero_info.heroderc = request.form["heroderc"]
        userfor = request.cookies['name']
        return render_template('detail.html', id=hero_info.heroname, detail=hero_info.datil, userfor=userfor)


@app.route('/addhero', methods=['GET', 'POST'])
def addhero():
    if request.method == 'GET':
        return render_template('addhero.html')

    elif request.method == 'POST':
        userfor = request.cookies['name']
        heroname = request.form["heroname"]
        detail = request.form["datil"]
        heroderc = request.form["heroderc"]
        userid = 1
        manger.inserHero(heroname, heroderc, detail, userid)
        infoarray = manger.selectHero()
        print(request.form)
        return render_template('choice.html', userfor=userfor, infoarray=infoarray)


if __name__ == "__main__":
    app.run()
