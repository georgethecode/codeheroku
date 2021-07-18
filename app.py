from flask import Flask
app=Flask(__name__)

# run_with_ngrok(app)

 @app.route('/')
 def hello():
  return('Hello world!')
