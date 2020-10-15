import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter, get_page_args
import bcrypt
from bson.objectid import ObjectId



app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'gamer-reviews'
app.config["MONGO_URI"] = 'mongodb+srv://joe:Drumgoon6894@gamerreview.85ibj.mongodb.net/gamer-reviews?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", reviews=mongo.db.reviews.find())
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form.get('username')})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return render_template('index.html')
        else:
            return "invalid login details"

    return render_template('login.html')
    
@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return render_template('index.html')
            
        return 'that username already exists!'
        
    return render_template('register.html')
    
@app.route('/articles')
def articles():
    return render_template("articles.html")

@app.route('/single_article')
def single_article():
    return render_template("single-article.html")
    
page, pe_page, offset = get_page_items()

(total, processed_text1) = DBQueries.processQuery(query, offset, per_page)
pagination = get_pagination(page=page,
                            per_page=per_page,
                            total=total,
                            format_total=True,
                            format_number=True,
                            record_name='reviews'
                            )
    
@app.route('/reviews')
def reviews():
    return render_template("reviews.html", 
                            page=page,
                            total=total,
                            per_page=pe_page,
                            pagination=pagination,
                            reviews=mongo.db.reviews.find()
                            )

def get_css_framework():
    return 'bootstrap4'
    
def get_link_size():
    return 'sm'
    
def show_single_page_or_not():
    return False
    
def get_page_items():
    page= int(request.args.get('page', 1))
    per_page=request.args.get('per_page')
    if not per_page:
        per_page = PER_PAGE
    else:
        per_page=int(per_page)
    offset=(page-1)*per_page
    return page, per_page, offset
    
def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'reviews')
    return Pagination(css_framework=get_css_framework())

@app.route('/single_review')
def single_review():
    return render_template("single-review.html", reviews=mongo.db.reviews.find())
    
@app.route('/write_review', methods=["POST", "GET"])
def write_review():
    if 'username' not in session:
        return render_template('must-login.html')
    reviews = mongo.db.reviews
    reviews.insert_one({"name": request.form.get('username'),
        "game_name": request.form.get('game-name'),
        "dev_name": request.form.get('dev-name'),
        "genre": request.form.get('genre'),
        "image": request.form.get('image'),
        "gameplay": request.form.get('gameplay'),
        "story": request.form.get('story'),
        "production-quality": request.form.get('production-quality'),
        "price": request.form.get('price'),
        "platform": request.form.get('platform'),
        "body": request.form.get('body')
    })
    return render_template("write-review.html")

@app.route('/contact')
def contact():
    return render_template('contact.html', reviews=mongo.db.reviews.find())
    
@app.route('/my_reviews')
def my_reviews():
    if 'username' not in session:
        return render_template('must-login.html')
    return render_template('my-reviews.html', reviews=mongo.db.reviews.find())
    
@app.route('/must_login')
def must_login():
    return render_template('must-login.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
