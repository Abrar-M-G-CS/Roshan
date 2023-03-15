import datetime
import os
import urllib.request
import urllib.parse
import threading
import time
from flask import (
    Flask,
    render_template,
    request,
    Response,
    flash,
    redirect,
    session,
    url_for,
    abort,
    jsonify,
    send_file,
    send_from_directory)


app=Flask(__name__)





@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers',
                         'GET, POST, PATCH, DELETE, OPTION')
    return response


    
@app.route('/')
def index():
    #form= sign_up_form()
    return render_template('pages/index.html')




#------------------------Launching the program---------------------------

# Default port:
if __name__ == '__main__':
    app.run()




