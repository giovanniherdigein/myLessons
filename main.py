# flaskapp test
#!/usr/bin/python3
# @author 'Giovanni Herdigein'
# @Version '1.0'
# @description 
"""
	HARVARD LECTURE 1 PYTHON/FLASK
 Deze applicatie is puur gemaakt voor studie doeleinde
 Ik test hiermee flask 's mogelijkheden met sessies en andere features
"""
# ####################################################################
# imports
# ####################################################################
from flask import Flask,render_template,request,url_for
from flask_session import Session

# ####################################################################
# app config
# ####################################################################
app = Flask(__name__)
# bepaald het type sessie
SESSION_TYPE = 'filesystem' 
# Neemt de configuratie over van de global app
app.config.from_object(__name__) 
# Maakt een nieuw sessie object aan
Session(app) 
# We maken een container voor notities
notes = [] 

# ####################################################################
# routes
# ####################################################################
@app.route('/')
def index():
	"""
		Mijn basis method
		Hiermee begint dat programma 
	"""
	base = {
		'title':'Index'
	}
	return render_template("index.html",base=base)

@app.route('/answer',methods=['GET','POST'])
def answer():
	"""
		Deze method maakt een notie aan in een Global Session object
	"""
	base = {
		'title':'answer'
	}
	if (request.method == "POST") and (request.form['name'] !=''):
		name = request.form['name']
		notes.append(name)
	return render_template("answer.html",base=base,notes=notes)

# ####################################################################
# app start
# ####################################################################
if __name__ == "__main__":
	app.run(debug=True,port=8070)
