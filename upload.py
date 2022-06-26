import json
import requests
from datetime import datetime
try:
    #DATA INPUT FROM DATA.JSON FILE
    DATA_FILE = 'data.json'
    with open(DATA_FILE) as f:
        DATA = json.load(f)
    TOKEN_FILE = 'credentials_drive.dat'
    with open(TOKEN_FILE) as TOKEN_DATA:
        TOKEN = json.load(TOKEN_DATA)

    if DATA['IMAGES']:
        headers = {"Authorization": "Bearer "+ TOKEN['access_token']}
        para = {
            "name": datetime.now().strftime("%y%m%d%H%M%S") + ".jpg",
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': (open("./"+DATA['IMAGES'], "rb"))
            }        
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files)
        print(r.text)

        with open('image.json', 'w') as IMAGE_FILE:
            IMAGE_FILE.write(r.text)
        
        with open('image.json') as IMAGE_FILE_DATA:
            UPLOAD_DATA = json.load(IMAGE_FILE_DATA)
            if UPLOAD_DATA['id']:
                print("[+] IMAGE iD: "+UPLOAD_DATA['id'])
                DATA['STATUS'] = 'P'
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
            else:
                print("IMAGES UPLOAD PROBLOAME")    
    else:
        print("IMAGES ARE NOT AVALABLE")
        DATA['STATUS'] = 'U'
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 

except Exception as e:   
        print("ERROR FROM FILE NAME upload.py: ") 
        print("https://developers.google.com/oauthplayground/") 
        print(e)
