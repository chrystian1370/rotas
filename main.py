from flask import Flask , render_template , request
app = Flask('app')

@app.route('/')
def index():
 return '<h1>Olá Mundo!</h1>'
  
@app.route('/unifran')
def unifran():
 return '<h2>Universidade de Franca</h2>'

@app.route('/dashboard/<name>')
def user(name):
 return f'<h1>Olá, {name}</h1>'

  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)