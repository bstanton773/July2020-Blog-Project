from  july_blog import app
from flask import render_template, request

# Import for Forms
from july_blog.forms import UserInfoForm, BlogPostForm

# Import for Models
from may_blog.models import User, Post

# Home route
@app.route('/')
def home():
    customer_name = "Brian"
    order_number = 1
    item_dict = {1:"Ice Cream", 2:"Bread", 3:"Lemons", 4:"Cereal"}
    return render_template("home.html", customer_name=customer_name, order_number=order_number, item_dict = item_dict)

# Register route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information from POST request
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username, password, email)
        # Create an instance of User
        user = User(username,email,password)
        # Open and insert into database
        db.session.add(user)
        # Save info into database
        db.session.commit()
    return render_template("register.html", form=form)

# Create Post route
@app.route('/createposts', methods=['GET', 'POST'])
def createposts():
    form = BlogPostForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        print("\n", title, content)
    return render_template('createposts.html', form=form)