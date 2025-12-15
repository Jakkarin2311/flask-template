from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="My Home Page")

@app.route('/about')
def about():
    title="About Page"
    name="jakkarin"
    email="jakkarink544@gmail.com"
    phone="099-456-7890"
    return render_template('about.html',
                           title=title,
                           name=name,
                           email=email,
                           phone=phone)

@app.route('/favorite/foods')
def favorite_foods():
    title=" Favorite Foods Page"
    foods = ['ส้มตำ', 'ต้มยำกุ้งน้ำข้น', 'ก๋วยเตี๋ยวต้มยำ', 'กระเพราไก่+ไข่ดาว', 'ข้าวผัดปู']
    return render_template('fav_foods.html',
                           title=title,
                           foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
    title=" Favorite Sports Page"
    sports = ['ฟุตบอล', 'บาสเกตบอล', 'วอลเลย์บอล', 'แบดมินตัน', 'ว่ายน้ำ']
    return render_template('fav_sports.html',
                           title=title,
                           sports=sports)

@app.route('/greeting/<username>')
def greeting(username):
    title = 'Welcome Page'
    return render_template('welcome.html',
                           title=title,
                            username=username)