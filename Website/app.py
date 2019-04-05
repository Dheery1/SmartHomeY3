from flask import Flask, render_template, abort, Response
import sys

import PythonVideoStreamingOnline

app = Flask(__name__)

run_flag = False

@app.route('/')
def index():
    return render_template('index.html')

 
        
@app.route('/stop')
def stop():
    abort(403)

@app.route('/video')
def video():
    return 



if __name__ == '__main__':
    app.run(debug=False, threaded=True,host='0.0.0.0')
