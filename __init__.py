from flask import Flask, render_template, url_for, redirect, request, jsonify, make_response, abort
import requests
app = Flask(__name__)

@app.route('/authors')
def getAuthorsPosts():
	author_url = 'https://jsonplaceholder.typicode.com/users'
	authors = requests.get(author_url).json()
	post_url = 'https://jsonplaceholder.typicode.com/posts'
	posts = requests.get(post_url).json()
	objects = []
	for author in authors:
		count = 0
		for post in posts:
			if author['id'] == post['userId']:
				count+=1
		objects.append({'name':author['name'],'posts':count})
		
	return render_template('auth.html',list = objects)
	
@app.route('/setcookie')
def showCookieForm():
	return render_template('setcookie.html')
	
	
@app.route('/setcookie' , methods = ['POST','GET'])
def setCookie():
	if request.method == 'POST':
		name = request.form['name']
		age = request.form['age']
		response = make_response(render_template('setcookie.html'))
		response.set_cookie('name',name)
		response.set_cookie('age',age)
		return response
	else:
		return redirect(url_for('setcookie'))
	
@app.route('/getcookie')
def getCookies():
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return '<h3>Name is: </h>' +name + '<br><h3>Age is: </h>' + age
	
@app.route('/robots.txt')
def deny():
	abort(403)
	
@app.route('/html')
def renderHTML():
	return render_template('hobbies.html')
	
@app.route('/input')
def showForm():
	return render_template('form.html')
	
@app.route('/input' , methods = ['POST'])
def logData():
	if request.method == 'POST':
		comment = request.form['comment']
		print (comment)
		return redirect('/input')	
	
@app.route('/')
def index():
    return "Hello World - Venkat"

if __name__ == "__main__":
    app.run(debug='true')
