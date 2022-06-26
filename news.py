#!/usr/bin/env python3
import threading
import subprocess
import json

INTO = 'python into.py'
subprocess.Popen(INTO, shell=True)

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def foo():
  #DATA INPUT FROM DATA.JSON FILE
  DATA_FILE = 'data.json'
  with open(DATA_FILE) as f:
        DATA = json.load(f) 

  if DATA['STATUS']=='S':
    NEWS = 'python web.py'
    subprocess.Popen(NEWS, shell=True)
    POST_FILE = 'post.json'
    with open(POST_FILE) as POST_DATA:
        POST = json.load(POST_DATA)
    POST["TITLE"] = ""
    POST['DESCROPTION'] = ""
    POST['IMAGES'] = ""
    POST['CONTENT'] = ""
    POST['LEBALS'] = ""
    json.dump(POST, open(POST_FILE, "w"), indent = 2)

  
  if DATA['STATUS']=='E':
    NEWS = 'python replace.py'
    subprocess.Popen(NEWS, shell=True) 

  if DATA['STATUS']=='U':
    NEWS = 'python upload.py'
    subprocess.Popen(NEWS, shell=True)

  if DATA['STATUS']=='P':
    NEWS = 'python perm.py'
    subprocess.Popen(NEWS, shell=True)

  if DATA['STATUS']=='B':
    NEWS = 'python blogger.py'
    subprocess.Popen(NEWS, shell=True)
  
setInterval(foo,10)



