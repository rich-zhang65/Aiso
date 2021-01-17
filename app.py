
from flask import Flask, render_template

# mouse keyboard stuff
# https://www.thepythoncode.com/article/control-mouse-python

# flask setup
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('aisoDrawingPad.html')

if __name__ == "__main__":
  app.run()








