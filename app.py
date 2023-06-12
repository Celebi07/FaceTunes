from flask import *
import cv2
app = Flask(__name__)
from emotions import video_detection

def generate_frames_web():
    output = video_detection()
    for detection_ in output:
        ref,buffer=cv2.imencode('.jpg',detection_)

        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_page')
def new_page():
    return render_template('new-page.html')

@app.route('/webapp')
def webapp():
    return Response(generate_frames_web(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)