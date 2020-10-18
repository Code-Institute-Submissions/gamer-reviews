import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination
import bcrypt

app = Flask( __name__)

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
    
@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return render_template('index.html')
    
@app.route('/read_reviews_ps4', methods=["GET"])
def read_reviews_ps4():
    reviews = mongo.db.reviews
    reviews = reviews.find({'platform': 'ps4'})
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page

    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)
    
@app.route('/read_reviews_pc', methods=["GET"])
def read_reviews_pc():
    reviews = mongo.db.reviews
    reviews = reviews.find({'platform': 'pc'})
    print(reviews)
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page

    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)

@app.route('/read_reviews_xbox', methods=["GET"])
def read_reviews_xbox():
    reviews = mongo.db.reviews
    reviews = reviews.find({'platform': 'xbox'})
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page

    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)
    
@app.route('/read_reviews_wii', methods=["GET"])
def read_reviews_wii():
    reviews = mongo.db.reviews
    reviews = reviews.find({'platform': 'wii u'})
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page

    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)

@app.route('/articles')
def articles():
    return render_template("articles.html")

@app.route('/single_article')
def single_article():
    return render_template("single-article.html")
    
@app.route('/reviews', methods=['GET'])
def reviews():
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    allreviews = mongo.db.reviews.find()
    reviews_for_render = allreviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = allreviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)
    
@app.route('/single_review')
def single_review():
    return render_template("single-review.html", reviews = mongo.db.reviews.find())
    
@app.route('/write_review')
def write_review():
    return render_template("write-review.html")

@app.route('/post_review', methods=["POST", "GET"])
def post_review():
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
        "production_quality": request.form.get('production-quality'),
        "price": request.form.get('price'),
        "total": request.form.get('total'),
        "platform": request.form.get('platform'),
        "body": request.form.get('body')
    })
    return redirect(url_for('my_reviews'))

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/my_reviews', methods=["post", "GET"])
def my_reviews():
    if 'username' not in session:
        return render_template('must-login.html')
    
    username = session['username']
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    myreviews = mongo.db.reviews.find({'name': username})
    reviews_for_render = myreviews.limit(per_page).skip(offset)
    
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = myreviews.count(), css_framework = 'bootstrap4')
    
    return render_template('my-reviews.html', reviews = reviews_for_render, pagination = pagination)
    
@app.route('/edit_reviews/<review_id>')
def edit_reviews(review_id):
    the_review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('edit-reviews.html', review = the_review)
    
@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId(review_id)},
    {   "name": request.form.get('username'),
        "game_name": request.form.get('game-name'),
        "dev_name": request.form.get('dev-name'),
        "genre": request.form.get('genre'),
        "image": request.form.get('image'),
        "gameplay": request.form.get('gameplay'),
        "story": request.form.get('story'),
        "production_quality": request.form.get('production-quality'),
        "price": request.form.get('price'),
        "total": request.form.get('total'),
        "platform": request.form.get('platform'),
        "body": request.form.get('body')
    })
    username = session['username']
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    myreviews = mongo.db.reviews.find({'name': username})
    reviews_for_render = myreviews.limit(per_page).skip(offset)
    
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = myreviews.count(), css_framework = 'bootstrap4')
    return render_template('my-reviews.html', reviews = reviews_for_render, pagination=pagination)
    
@app.route('/delete_reviews/<review_id>')
def delete_reviews(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    
    username = session['username']
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    myreviews = mongo.db.reviews.find({'name': username})
    reviews_for_render = myreviews.limit(per_page).skip(offset)
    
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = myreviews.count(), css_framework = 'bootstrap4')
    return render_template('my-reviews.html', reviews = reviews_for_render, pagination=pagination)
    
@app.route('/must_login')
def must_login():
    return render_template('must-login.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
