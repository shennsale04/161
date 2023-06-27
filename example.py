@app.route('/')
def index():
   return render_template('index.html')

@app.route('/reg',methods = ['POST', 'GET'])
def reg():
   if request.method == 'POST' and
   request.form['username'] == 'admin' :
   return redirect(url_for('success'))
   return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'
	
if __name__ == '__main__':
   app.run(debug = True)