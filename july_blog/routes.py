from  july_blog import app
from flask import render_template

# Import for Forms
from july_blog.forms import UserInfoForm

# Home route
@app.route('/')
def home():
    customer_name = "Brian"
    order_number = 1
    item_dict = {1:"Ice Cream", 2:"Bread", 3:"Lemons", 4:"Cereal"}
    return render_template("home.html", customer_name=customer_name, order_number=order_number, item_dict = item_dict)

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()
    return render_template("register.html", form=form)