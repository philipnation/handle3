from flask import Flask,render_template,url_for,request,redirect
# For database
from flask_sqlalchemy import SQLAlchemy
# For date and time
from datetime import datetime
from random import *
from uiautomator import Device,device as d
device = Device()

# Creating an object for the class Flask
app = Flask(__name__)

# Adding a configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# //// -> Absolute path
# /// -> Relative path -> In the project folder

# Initializing the database
db = SQLAlchemy(app)

# This class will be called to add new task
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # This function is to give reponse when the todo is ran
    def __repr__ (self):
        return '<Task %r' % self.id

# Route to home, the first function will run
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your details'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

# Route to about, the about function will run
# Note: it is not letter sensitive meaning that 
# You can name the function another thing but make
# Sure it is immediatly after the app.route

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'{e}There was an error deleting a row'
    
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            'An error occured'
    else:
        return render_template('update.html', task=task)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/fb')
def open_facebook():
    # Use UI Automator to launch the Facebook app
    d.press.home()
    d(text='Facebook').click()
    return 'Facebook app opened!'


@app.route('/sms', methods=['POST','GET'])
def send_message():
    phone_number = '09060507076'
    #message = request.form['message']

    # Open Notepad and copy all text
    device(text="Notepad").click()
    device.press("menu")
    device(text="Select all").click()
    device.press("menu")
    device(text="Copy").click()

    # Open Message app and compose a new message
    device(text="Message").click()
    device(resourceId="com.android.messaging:id/recipient_text_view").set_text(phone_number)
    device(resourceId="com.android.messaging:id/contact_picker_create_group").click()

    # Paste the copied text and send the message
    device(resourceId="com.android.messaging:id/compose_message_text").long_click()
    device.press("menu")
    device(text="Paste").click()
    device(resourceId="com.android.messaging:id/send_message_button_container").click()

    return "Message sent!"
# with app.app_context():
#    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
