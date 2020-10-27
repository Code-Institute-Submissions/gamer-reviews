# GamerReviews
Gamer-reviews is a gaming review website, where users can write a review on games they have played. They can also read reviews, written by fellow gamers, on games they may intend to play in the future 
so they can make an informed decision before purchasing. Gamer-Reviews also has a news section. This page keeps users updated on all upcoming and new releases.
Link to [deployed applictation](https://git.heroku.com/gamer-review.git)
## UX
### User stories
The majority of users on this site will be people who are trying to decide what game to buy next. Gamer-reviews can help users to achieve this goal by reading reviews and articles available on the site.
* As a user, I want a site where I can read player reviews on a game so I can decide what I want to play.
* As a user, I want a site where I can write a game review, so i can help other players decide what they want to play.
* As a user, I want a site where I can edit and delete my reviews, so I can help other players decide what they want to play.
* As a user, I want a site where I can get info about a game and buy the game.
* As a user, I want a site where I can find out news on upcoming and new releases so I can make an informed decision before making a purchase.
* As a user, I want to be fit login to write and edit my reviews
* As a user, I want to be fit to register to write and edit my reviews

link to whimsical [wireframe](https://whimsical.com/GF3LwR3awwcbkpBAMFhj32)

## Features
### Existing Features:
* Read Review button home page - Allows user to read reviews for their specific platform.
* Owl-carousel - Displays all reviews in a carousel to show what reviews are available.
* Articles - Is a section which shows the articles that are available. Users can click on button and a link for the full article is shown.  
* Write a review page allows users to write a review by filling out a simple form.
* Search bar - The search bar allows user to find a specific review that they might be looking for.
* My reviews page - The my reviews page has all of a users reviews in one place so they can keep track of them.
* Edit and Delete buttons - The edit and delete buttons on the my-reviews page allows users to edit and delete reviews if they want.
* Contact page - On the contact page the user can fill out a form and send a message if they have any issues.
* Watch on twitch button - The watch on twitch button takes users to twitch so the user can watch the game before purchasing.
* Buy Game button - The buy game button takes users to gamestop if they want to buy the game.

### Features left to implement:
* Forum where users can discuss games
* A filter by button that gives users the option to filter games by total score, developer name etc.
* Profile page where users can store a list of their favorite games and some personal details, like their steam user name etc.

## Technologies Used:
- [HTML5](https://www.html5tutorial.info/)
    - Used to write the code of the website.
- [CSS3](http://www.css3.info/)
    - Used to style the website.
- [Bootstrap](https://getbootstrap.com/)
    - Used the grid system for the layout of the website.
- [Jquery](https://jquery.com/)
    - Used for DOM traversing.
- [Googlefonts](https://fonts.google.com/)
    - Used for additional fonts.
- [Fontawesome](https://fontawesome.com/)
    - Used to add icons to the website.
- [Javascript](https://www.javascript.com/)
    - Used for the functionality of the website.
- [whimsical](https://whimsical.com/)
    - Used for wireframe.
- [jshint.com](https://jshint.com/)
    - Used to validate javascript.
- [validator.w3.org](https://validator.w3.org/)
    - Used to validate html and css3
- [AWS cloud9](https://aws.amazon.com/cloud9/)
    - Used to Write all code. 
- [Gamespot API](http://gamespot.com/api/)
	- Used for the articles.
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
	- Used to let flask and mongodb communicate.
* [MongoDB](https://www.mongodb.com/)
	- Used as a database for website.
* [Flask-paginate](https://pythonhosted.org/Flask-paginate/)
	- Used for pagination of reviews.
* [Bcrypt](https://pypi.org/project/bcrypt/)
	- Used to encode user passwords
* [EmailJS](https://www.emailjs.com/)
	- Used to send emails.

## Testing
* Login Form:
	- Does not allow user to enter spaces.
	- Stops users from submitting an empty form.
	- If password or username is incorrect shows an error.
* Register Form:
	-  Does not allow user to enter spaces.
	- Stops users from submitting an empty form.
	- If password or username is incorrect shows an error.
* Logout button:
	- logs out user.
* Edit button:
	 - takes user to edit reviews page.
	 - All data is preloaded in form.
	 - Saves changes when submitted.
* Delete button: 
	- When clicked asks user if they are sure.
	- when delete button is clicked removes review
* Write review page:
	- If user is not logged in, stops user from loading page.
	- stops user posting an empty form.
	- when submit button is clicked, adds review to database.
* My reviews page: 
	- If user is not logged in stops the user loading the page.
	- Only shows reviews that user has written.
	- if user has no reviews shows an error.
* Read review button home page:
	- Takes user to reviews.html that only shows corresponding reviews for platform.
* Contact Form:
	- Stops user from submitting empty form.
	- Sends email when submit button is clicked.
* Articles page:
	- Loads articles from api and displays them.
	- When read article button is clicked a modal pops up containing a link to full article.
* Buy game button:
	- When clicked takes user to gamestop.
* Watch on twitch button: 
	- When clicked takes user to twitch.

### Bugs
After performing the above tests i found a few bugs that have since been resolved. They include:
#### Login form:
* Users were allowed to enter spaces into form. To prevent this i wrote some javascript that prevents spaces in the input.

#### Registration Form:
* Users were allowed to enter spaces into form. To prevent this i wrote some javascript that prevents spaces in the input.
#### Write Review form:
* When page was loaded the form submitted an empty review to database. To stop this I created a separate route in my app.py file called post_review.
#### Articles: 
* When I started using the gamespot api I was getting a CORS error. To fix this I added the cors anywhere proxy url, which fixes the issue but can leave the articles slow to load.

### Browser tests
I tested the website on three different browsers to see if each page looked like it should.


| Browser       | Microsoft Edge | Google Chrome | Firefox |
|---------------|----------------|---------------|---------|
| Articles      | pass           | pass          | pass    |
| Contact       | pass           | pass          | pass    |
| Edit-Reviews  | pass           | pass          | pass    |
| Index         | pass           | pass          | pass    |
| Login         | pass           | pass          | pass    |
| Must-login    | pass           | pass          | pass    |
| My-reviews    | pass           | pass          | pass    |
| Register      | pass           | pass          | pass    |
| Reviews       | pass           | pass          | pass    |
| Write-reviews | pass           | pass          | pass    |

### Device Sizes
To test the site on different devices I used all the sizes on google developer tools to test the appearance and it's responsiveness.

| Device Size       | Articles | Contact | Edit-reviews | Index | Login | Must-login | My-reviews | Register | Reviews | Write-Review |
|-------------------|----------|---------|--------------|-------|-------|------------|------------|----------|---------|--------------|
| Moto G4           | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Galaxy S5         | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Pixel 2           | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Pixel 2 XL        | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Iphone 5/SE       | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Iphone 6/7/8      | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Iphone 6/7/8 Plus | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Iphone X          | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Ipad              | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Ipad pro          | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Surface Duo       | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |
| Galaxy Fold       | pass     | pass    | pass         | pass  | pass  | pass       | pass       | pass     | pass    | pass         |

### Online Validation
#### CSS3
|File     |Valid     |
|---------|----------|
|Style.css|pass      |

#### Javascript
| File                   | Valid |
|------------------------|-------|
| Carousel.js            | pass  |
| formValidationLogin.js | pass  |
| formValidationReg.js   | pass  |
| get-articles-index.js  | pass  |
| get-articles-news.js   | pass  |
| hideLogin.js           | pass  |
| range.js               | pass  |
| sendEmail.js           | pass  |
| checkbox.js            | pass  |

#### HTML5

| File              | Valid |
|-------------------|-------|
| articles.html     | pass  |
| contact.html      | pass  |
| edit-reviews.html | pass  |
| index.html        | pass  |
| login.html        | pass  |
| must-login.html   | pass  |
| my-reviews        | pass  |
| register.html     | pass  |
| reviews.html      | pass  |
| write-review.html | pass  |
| base.html         | pass  |


#### Python

| File   | Valid |
|--------|-------|
| env.py | pass  |
| app.py | pass  |

## Deployment
### Deploying to heroku:
I deployed the website to heroku. I did this by:
* Sign in or sign up if you havent already.
* Created a new app by clicking the create app button.
* In heroku go to settings and set config variables.
* Then in the terminal of your IDE type the command "heroku login" and provide your login details.
* Then use the command "git add ."
* Then use the command "git commit -am 'message' " with an appropriate commit message.
* Then use the command "git push heroku master"
* Then go back to heroku and click the open app button in the top right of the site.

### Cloning Locally:
* Under the repository's name, click Clone or download.
* In the Clone with HTTPs section copy the given url.
* In your IDE of choice, open git bash.
* Change the current working directory to the location where you want the cloned to go.
* Type git clone, and then paste the URL copied from Github.
* Press enter and the local clone will be created.
* Create a env.py file and set the environment for SECRET_KEY, MONGO_URI and MONGO_DBNAME.

## Credits
### Contents
* The carousels were taken from [Bootstrap](https://getbootstrap.com/) and [Owl carousel](https://owlcarousel2.github.io/OwlCarousel2/)
* The modals were taken from [Bootstrap](https://getbootstrap.com/)
* The articles were taken from [Gamespot API](https://www.gamespot.com/api/)

### Media
* All images were taken from google images.

### Acknowledgements
* The layout for this page was inspired by a color [Color Libs Template](https://colorlib.com/wp/template/egames/)
* I got help from my code institute mentor Precious Ijege.
* I also got help from [w3schools](https://www.w3schools.com/) and [developer.mozilla](https://developer.mozilla.org/en-US/).
