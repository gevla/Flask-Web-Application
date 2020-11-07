from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

dbconn = pymysql.connect('localhost', 'user3', 'password3', 'blogdata')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/submit', methods=["POST","GET"])
def submit():
	#form = request.form
	if request.method=="POST":
		print(request.form)
		
		email = request.form['mail']
		message = request.form['message']
		fn = request.form['first']
		ln = request.form['last']

		dbconn = pymysql.connect('localhost', 'user3', 'password3', 'blogdata')
		curs = dbconn.cursor()
		curs.execute("""INSERT INTO submissions values("%s","%s","%s","%s")"""%(fn, ln, email, message))
		dbconn.commit()
		dbconn.close()
		return render_template("submit.html")
	
@app.route('/responses')
def fetch():
	dbconn = pymysql.connect('localhost', 'user3', 'password3', 'blogdata')
	curs = dbconn.cursor()
	curs.execute("SELECT * FROM submissions")
	values = curs.fetchall()
	dbconn.close()
	print(values)
	return render_template("responses.html", result=values)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 80, debug=True)

