import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination
import bcrypt

app = Flask( __name__)

# reviews database name
app.config["MONGO_DBNAME"] = 'gamer-reviews'
# uri for database
app.config["MONGO_URI"] = 'mongodb+srv://joe:Drumgoon6894@gamerreview.85ibj.mongodb.net/gamer-reviews?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
# index route
@app.route('/index')
def index():
    return render_template("index.html", reviews=mongo.db.reviews.find())
    
@app.route('/login')
def login():
    return render_template("login.html")
    
# login page route
@app.route('/login_user', methods=['POST'])
def login_user():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form.get('username')})
    login = users.find_one({'name': request.form.get('username')})
    
    if login is None:
        error_message = "Invalid login details, please try again"
        return render_template('login.html', error_message=error_message)
    
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return render_template('index.html')
        else:
            error_message = "Invalid login details, please try again"
            return render_template('login.html', error_message=error_message)
    
# route for register.html
@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        # varible that stores users data 
        users = mongo.db.users
        # variable that checks to see if username exists already
        existing_user = users.find_one({'name': request.form['username']})
        
        if existing_user is None:
            #encodes user password
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # inserts username and password to database
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            # returns user to home page
            return render_template('index.html')
            
            # message that displays if username already exists
        error_message = "User already exists, please sign in"
        return render_template("register.html", error_message=error_message)
        
    return render_template('register.html')
    
# route for logout
@app.route("/logout")
def logout():
    #checks to see if username is in session
    if 'username' in session:
        # logsout if username is in session
        session.pop('username')
        #returns user to home page
    return render_template('index.html')
    
# read-reviews-ps4 route
@app.route('/read_reviews_ps4', methods=["GET"])
def read_reviews_ps4():
    # variable that stores all reviews
    reviews = mongo.db.reviews
    #variable that stores reviews on ps4 platform
    reviews = reviews.find({'platform': 'ps4'})
    #variable that determines the number of pages to paginate
    page = int(request.args.get('page', 1))
    # how many reviews on each page
    per_page = 5
    # tells function how many reviews to skip 
    offset = (page - 1) * per_page
    
    # variable that stores the specified reviews and how many on each page and how many items to skip
    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)
    
# read-reviews-pc route
@app.route('/read_reviews_pc', methods=["GET"])
def read_reviews_pc():
    # variable that stores all reviews
    reviews = mongo.db.reviews
    #variable that stores reviews on pc platform
    reviews = reviews.find({'platform': 'pc'})
    #variable that determines the number of pages to paginate
    page = int(request.args.get('page', 1))
    # how many reviews on each page
    per_page = 5
    # tells function how many reviews to skip 
    offset = (page - 1) * per_page
    
    # variable that stores the specified reviews and how many on each page and how many items to skip
    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)

# read-reviews-xbox route
@app.route('/read_reviews_xbox', methods=["GET"])
def read_reviews_xbox():
    # variable that stores all reviews
    reviews = mongo.db.reviews
    #variable that stores reviews on xbox platform
    reviews = reviews.find({'platform': 'xbox'})
     #variable that determines the number of pages to paginate
    page = int(request.args.get('page', 1))
    # how many reviews on each page
    per_page = 5
     # tells function how many reviews to skip 
    offset = (page - 1) * per_page

    # variable that stores the specified reviews and how many on each page and how many items to skip
    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)

# read-reviews-wii route    
@app.route('/read_reviews_wii', methods=["GET"])
def read_reviews_wii():
    # variable that stores all reviews
    reviews = mongo.db.reviews
    #variable that stores reviews on wii platform
    reviews = reviews.find({'platform': 'wii u'})
    #variable that determines the number of pages to paginate
    page = int(request.args.get('page', 1))
    # how many reviews on each page
    per_page = 5
    # tells function how many reviews to skip
    offset = (page - 1) * per_page
    
    # variable that stores the specified reviews and how many on each page and how many items to skip
    reviews_for_render = reviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = reviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)

# articles route
@app.route('/articles')
def articles():
    return render_template("articles.html")
    
# reviews route
@app.route('/reviews', methods=['GET'])
def reviews():
    #variable that determines the number of pages to paginate
    page = int(request.args.get('page', 1))
    # how many reviews on each page
    per_page = 5
    # tells function how many reviews to skip
    offset = (page - 1) * per_page
    
    # variable that stores all reviews
    allreviews = mongo.db.reviews.find()
    # variable that stores the specified reviews and how many on each page and how many items to skip
    reviews_for_render = allreviews.limit(per_page).skip(offset)
        
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = allreviews.count(), css_framework = 'bootstrap4')
    return render_template('reviews.html', reviews = reviews_for_render, pagination = pagination)

@app.route('/search', methods=['GET', 'POST'])
def search():
    gameName = mongo.db.reviews.find({'game_name': request.form.get('search')})
    gameForRender = mongo.db.reviews.find({'game_name': request.form.get('search')})
    allGameNames = mongo.db.reviews.distinct('game_name')
    #variable that determines the number of pages to paginate
    page = int(request.args.get('page', 1))
    # how many reviews on each page
    per_page = 5
    # tells function how many reviews to skip
    offset = (page - 1) * per_page
    reviews_for_render = gameForRender.limit(per_page).skip(offset)
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = gameForRender.count(), css_framework = 'bootstrap4')
    gameNameList = list(gameName)
    game = [i['game_name'] for i in gameNameList]
    if set(game).intersection(allGameNames):
        return render_template('reviews.html', pagination=pagination, reviews = reviews_for_render)
    else:
        error_message="No results found!"
        return render_template('reviews.html', pagination=pagination, reviews = reviews_for_render, error_message=error_message)
 
    return render_template('reviews.html', pagination=pagination, reviews = reviews_for_render )

# route for write-review
@app.route('/write_review')
def write_review():
    #if user is not logged in, takes user to must login page
    if 'username' not in session:
        return render_template('must-login.html')
    return render_template("write-review.html")

# post review route
@app.route('/post_review', methods=["POST", "GET"])
def post_review():
    # stores gamer-review data base in variable
    reviews = mongo.db.reviews
    # inserts form data into the database
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

#contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
# my-reviews route
@app.route('/my_reviews', methods=["post", "GET"])
def my_reviews():
    # takes user to must login page if user isnt logged in
    if 'username' not in session:
        return render_template('must-login.html')
    
    # stores session username in a variable
    username = session['username']
    # variable that determines how many pages to paginate
    page = int(request.args.get('page', 1))
    # variable that stores how many reviews per page
    per_page = 5
    # variable that tells function how many reviews to skip
    offset = (page - 1) * per_page
    
    # variable that stores all the reviews for the corresponding username
    myreviews = mongo.db.reviews.find({'name': username})
     # variable that stores the specified reviews and how many on each page and how many items to skip
    reviews_for_render = myreviews.limit(per_page).skip(offset)
    total = myreviews.count()
    
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = myreviews.count(), css_framework = 'bootstrap4')
    if total == 0:
        error_message = "Sorry but you have no reviews yet"
        return render_template('my-reviews.html', error_message=error_message, pagination=pagination, reviews = reviews_for_render)
    
    return render_template('my-reviews.html', reviews = reviews_for_render, pagination = pagination)

# route for edit reviews    
@app.route('/edit_reviews/<review_id>')
def edit_reviews(review_id):
    # stores reviews corresponding _id
    the_review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('edit-reviews.html', review = the_review)
   
# update-review route
@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    # stores all reviews in a variable
    reviews = mongo.db.reviews
    # updates the review using the form output
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
    # returns user to my reviews
    return render_template('my-reviews.html', reviews = reviews_for_render, pagination=pagination)
    
# delete-review route
@app.route('/delete_reviews/<review_id>')
def delete_reviews(review_id):
    # finds the clicked on reviews _id
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    
    username = session['username']
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    myreviews = mongo.db.reviews.find({'name': username})
    reviews_for_render = myreviews.limit(per_page).skip(offset)
    
    pagination = Pagination(page = page, per_page = per_page, offset = offset, total = myreviews.count(), css_framework = 'bootstrap4')
    # returns user to my reviews.html
    return render_template('my-reviews.html', reviews = reviews_for_render, pagination=pagination)
  
# must login route
@app.route('/must_login')
def must_login():
    return render_template('must-login.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT'),),
            debug=True)
