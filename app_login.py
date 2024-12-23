from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///profile.db"
db = SQLAlchemy(app)

migrate = Migrate(app,db)

#Model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20),nullable=False)
    lname = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer,nullable=False)

def __repr__(self):
    f"Name : {self.fname} {self.lname} Age : {self.age} "


@app.route('/')
def index():
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)

@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')


@app.route('/add' , methods=['POST'])
def profile():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    age = request.form.get('age')
    if fname != "" and lname != "" and age is not None:
        p = Profile(fname=fname, lname=lname, age=age)
        db.session.add(p)
        db.session.commit()  
        return redirect('/')
    else:
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)