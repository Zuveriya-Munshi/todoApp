from flask import Flask,render_template,redirect,request,Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime , default= datetime.utcnow)

def __repr__(self):
    return f"Title : {self.title} , Description : {self.desc}"

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    desc = request.form.get('desc')
    # date_created = request.form.get('date_created')
    if title != "" and desc != "" :
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/') 
    else:
        return redirect('/') 

@app.route('/delete/<int:id>')
def delete(id):
    data = Todo.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>' , methods=['POST', 'GET']) 
def update(id):
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
    # date_created = request.form.get('date_created')
        if title != "" and desc != "" :
            data = Todo.query.filter_by(id=id).first()
            data.title = title
            data.desc = desc
            db.session.commit()
            return redirect('/') 
        else:
            return redirect('/') 
    data = Todo.query.filter_by(id=id).first()
    return render_template('update.html', data=data)

# @app.route('/update_todo' , methods=['POST'])
# def update_todo():
   
if __name__ == '__main__':
    app.run(debug=True)