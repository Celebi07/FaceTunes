from flask import Flask,url_for,render_template
import cv2
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_page')
def new_page():
    return render_template('new-page.html')

if __name__ == "__main__":
    app.run(debug=True)