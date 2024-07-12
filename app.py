from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
db = SQLAlchemy(app)  
#class to make the databases
class ToDo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"
    
       
@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=ToDo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
         
    allTodo=ToDo.query.all()
    return render_template('index.html',allTodo=allTodo)

@app.route('/Delete/<int:sno>')
def Delete(sno):
    todo=ToDo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)
    