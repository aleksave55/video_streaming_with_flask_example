#!/usr/bin/env python
#
# Project: Video Streaming with Flask
# Author: Log0 <im [dot] ckieric [at] gmail [dot] com>
# Date: 2014/12/21
# Website: http://www.chioka.in/
# Description:
# Modified to support streaming out with webcams, and not just raw JPEGs.
# Most of the code credits to Miguel Grinberg, except that I made a small tweak. Thanks!
# Credits: http://blog.miguelgrinberg.com/post/video-streaming-with-flask
#
# Usage:
# 1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.

from flask import Flask, render_template, Response
from camera import VideoCamera, ScreenShot
import rest
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    # return Response(gen(VideoCamera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(gen(ScreenShot()),
                     mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    server_url = 'http://0.0.0.0:8081'
    user_name = input("unesi user_name: ")
    sifra = input("unesi sifru: ")

    stream_url = server_url+'/start_stream'
    stream_dict = '{"user_name": %s, "sifra": %s}' % (user_name, sifra)
    podaci = {"user_name":user_name, "sifra":sifra}
    p = json.dumps(podaci)
    provera = rest.send('POST', stream_url, p, {'Content-Type': 'application/json'})
    if provera['status'] == 'ok':
        print('uspesno')
    else:
        print('neuspesno')

    #app.run(host='0.0.0.0', debug=True)