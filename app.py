import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'gamer-reviews'
app.config["MONGO_URI"] = 'mongodb+srv://joe:Drumgoon6894@gamerreview.85ibj.mongodb.net/gamer-reviews?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", reviews=mongo.db.reviews.find())
    
@app.route('/articles')
def articles():
    return render_template("articles.html", reviews=mongo.db.reviews.find())

@app.route('/single_article')
def single_article():
    return render_template("single-article.html", reviews=mongo.db.reviews.find())
    
@app.route('/reviews')
def reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())

@app.route('/single_review')
def single_review():
    return render_template("single-review.html", reviews=mongo.db.reviews.find())
    
@app.route('/write_review')
def write_review():
    return render_template("write-review.html", review=mongo.db.reviews.find())

@app.route('/contact')
def contact():
    return render_template('contact.html', reviews=mongo.db.reviews.find())
    
@app.route('/my_reviews')
def my_reviews():
    return render_template('my-reviews.html', reviews=mongo.db.reviews.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
