# flaskapp.py
# This is a "hello world" app sample for flask app. You may have a different file.
from flask import Flask
app = Flask(__name__)
@app.route('/') 
def hello_world():
   return 'Hello from Flask!' 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
