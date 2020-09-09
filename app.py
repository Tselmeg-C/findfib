from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from findfib.PossibleCombOfFibNum import PossibleCombOfFibNum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///fiblogs.db'

# initialize the database
db = SQLAlchemy(app)

# create database model
class Fiblogs(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	target = db.Column(db.Integer, nullable=False)
	result = db.Column(db.String(2000), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	# create function to return a strng when we add 
	def __repr__(self):
		return 'datetime: {}, id:{}, target: {}, result: {}'.format(self.datetime,self.id,self.target,self.result)


# create routes
@app.route("/")
def home():
	return "This web app is to find all possible combination of fibonacci numbers that sum up to a given integer. \
	Please enter the number at the end of the URL bar using the format: /fib/number"

@app.route('/fib/<int:number>') 
def fib(number):
	fib_num_finder = PossibleCombOfFibNum(number)
	fib_num_finder.find_fib_combinations_sum_to_target()
	result = fib_num_finder.fib_combinations_sum_to_target
	
	# log the result into the database
	new_fiblog = Fiblogs(target=number,result=str(result))
	db.session.add(new_fiblog)
	db.session.commit()
	return str(result)

@app.route('/health')
def health():
	fiblogs = Fiblogs.query.order_by(Fiblogs.date_created)
	return render_template("health.html",title="health check",fiblogs=fiblogs)

app.run(host='0.0.0.0')
